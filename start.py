import os
from scripts.optimizeToken import optToken
from scripts.partitionText import process



# SQL info
host = os.environ.get("MYSQL_HOST")
user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')

# Get the leetcode data
if os.path.isfile("data") == False:
    os.system("/bin/bash c.sh") 

# Remove needless strings and stuff
optToken()

# Create the table and db [already used if not exist]
os.system(f'/bin/mysql -h"{host}" -u"{user}" -p"{password}" < scripts/createTable.sql')

# Extract and append the data into database
process(host,user,password)
