import re

def optToken():    
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
    
    data = ""
    with open("data","r") as f:
        data = f.read()
    
    
    splits = data.split("\n")
    
    newData = []
    
    ignores = [
        "comments: ",
        "---",
        "difficulty: ",
        "edit_url: ",
        "README.md",
        "<!-- ",
        "####",
    ]
    
    count = 0
    isWithinSnip = False
    codeType = ""
    for x in splits:
        for y in ignores:
            if y in x:
                count+=1
                break
        else:
            if "```" in x:
                # Code snip
                if not isWithinSnip:
                    codeType = x[3:]
                else:
                    codeType = ""
                isWithinSnip = not isWithinSnip
            if not isWithinSnip:
                x=remove_html_tags(x)
            if codeType in ("","java","mysql","sql","python") and x != "":
                newData.append(x)
    
    with open("data","w") as f:
        f.write("\n".join(newData))
    