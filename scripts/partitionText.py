from json import dumps as jsonify
import zlib # Compressing solution data
import mysql.connector as sql
import re

def process(host,userdata,password,ALLOW_COMPRESS = True): # Compress the solution codes data
    
    db = sql.connect(
        host=host,
        user=userdata,
        password=password,
        database="leet"
    )
    
    cur = db.cursor(prepared=True)  # Use prepared statements for better security
    
    def execute(query, params=None, out=False):
        cur.execute(query, params)
    
    def compress(data):
        if not ALLOW_COMPRESS:
            return data
        return zlib.compress(data.encode())
    
    # debug 
    # execute("show tables;", out=True) 
    
    
    data = ""
    with open("data", "r") as f:
        data = f.read()
    
    data = data.split("\n")
    
    tagBased = {
    
    }
    
    count = 1
    partitions = []
    givenNum = 1
    curr = "tags"
    tags = ""
    desc = ""
    name = ""
    sol=""
    link = ""
    regex = re.compile(r'\[.*?\]')
    for x in data[1:]:
        if x=="tags:":
            # New problem data
            count+=1
            tags = tags[:-1]
    
            for tag in tags.split(","):
                if tag in tagBased:
                    tagBased[tag].append(givenNum)
                else:
                    tagBased[tag] = [givenNum]
    
            # Edge case 
            if name != "Find Subarray With Bitwise AND Closest to K": # Duplicate change
                partitions.append((givenNum,name,tags,desc,sol,link))
            tags,desc,sol = "","",""
            curr = "tags"
        else:
            if curr=="tags":
                if "    - " in x:
                    tags+=x[len("    - "):]+","
                else:
                    curr = "name"
    
            if curr == "name":
                # Parse
                parse = [x for x in regex.finditer(x)][0].group(0)[1:-1]
                splits = parse.split(".")
                givenNum = splits[0]
                name = splits[1][1:]
                link = x.split("(")[1][:-1]
                curr = "none"
            
            if curr == "desc":
                desc += x +"\n"
            if curr == "sol":
                sol += x + "\n"
    
            if x.startswith("## Descr"):
                curr="desc" 
            if x.startswith("## Sol") and curr != "sol":
                curr = "sol"
    
    print("Processed ",count," leetcode problem data")
    tagCache={}
    for data in partitions:
        id,name,tag,desc,sol,link = data
    
        desc = desc.replace("## Solutions","")
    
    
        langSample = {"py" : "python", "sql" : "mysql", "java" : "java"}
        lang = dict()
        for key in langSample:
            val = langSample[key]
            lang[key] = val
            lang[val] = val
    
        solutions = []
    
        # Splitting solutions and their respective language types
        for sols in sol.split("### Solution ")[1:]:
            solution = []
            solution.append(sols)
    
            solLangs = {}
    
            processed = [x for x in sols.split("```")[1:] if x != "\n"]
    
            for x in processed:
                if x[:x.find("\n")] == "": continue
                language = lang[x[:x.find("\n")]] # Converts to full form
                solLangs[language] = x[x.find("\n")+1:]
    
            solution.append(solLangs)
    
            solutions.append(solution)
    
            
        # Inserting id to names
        execute("INSERT INTO names (id, name) VALUES (%s, %s)", (id, name))
    
        # Inserting id to url
        execute("INSERT INTO url (id, info) VALUES (%s, %s)", (id, link))
    
        # Inserting tags and ids
        for t in tag.split(","):
            execute("INSERT INTO tags (id, tag) VALUES (%s, %s)", (id, t))
    
        # Inserting id to question
        execute("INSERT INTO question (id, info) VALUES (%s, %s)", (id, desc[:13999]))
    
        # Inserting id to solutions
        langSet = set()
        solFull = ""
        langStr = ""
        for sols in solutions:
            data = sols[0]
            solFull += data
            solName = data[:data.find("\n")+1]
            solData = compress( data[data.find("\n")+1:].replace("```\n","") )
    
            for langType in sols[1].keys():
                data = sols[1][langType]
                langSet.add(langType)
                execute("INSERT INTO " + langType + " (id, code) VALUES (%s, %s)", (id, compress(data)))
            
            langStr = ",".join(langSet)
            # This contains full data (all language solutions)
            execute("INSERT INTO sol (id, title, details, langs) VALUES (%s, %s, %s, %s)", (id, solName, solData, langStr))  
    
        wholeData = id +". " + name + " \n " + desc + " \n " + solFull + "\n\n"
    
        for t in tag.split(","):
            if t in tagCache:
                tagCache[t] += wholeData
            else:
                tagCache[t] = "" + wholeData
    
    
    
    # Tag cache
    for key in tagCache:
        execute("INSERT INTO tags_cache (tag, data) VALUES (%s, %s)", (key, compress(tagCache[key])))
    
    db.commit()
