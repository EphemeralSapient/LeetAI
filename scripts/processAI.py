import mysql.connector as sql
import zlib
import google.generativeai as genai


db = sql.connect(
    host="localhost",
    user="softwares",
    password="password",
    database="leetcode"
)

cur = db.cursor(prepared=True)  # Use prepared statements for better security

cur.execute("select data from tags_cache where tag = 'String';")

# Decompress the data
data = ""
for x in cur:
    for y in x:
        data+= zlib.decompress(bytes(y)).decode().replace("```","")

with open("data","w") as f:
    f.write(data)

# Set the API key
genai.configure(api_key="")


data.replace("```","")

model = genai.GenerativeModel('models/gemini-1.5-flash', system_instruction="Respond only to given problem numbers with given parameter.")

count = model.count_tokens(data)

print("API Count : ",count)
# Array contains 

resp = model.generate_content(data + "\n Give response by id-difficulty_rating{0-100} also do difficulty rating based on solution and problem usage with 0 as easy and 100 as really hard critical thinking involved. Give only id-rating format, no name or anything else.")
print(resp)

#print("Custom Count [words] : ", len(data.split(" ")))
