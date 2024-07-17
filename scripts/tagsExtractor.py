data = ""
with open("data", "r") as file:
    data = file.read()

# Split
splits = data.split("\n")

# Extract
tags = set()

for x in splits:
    if x.startswith("    - ") and x[6:].isalpha():
        tags.add(x[6:])

for x in tags: print(x)
