import google.generativeai as genai

# Set the API key
genai.configure(api_key="AI################")

# Get the data from file
data = ""
with open("data", "r") as f:
    data = f.read()

data.replace("```","")

# Count the tokens 
model = genai.GenerativeModel('models/gemini-1.5-pro')
count = model.count_tokens(data)

print("API Count : ",count)
