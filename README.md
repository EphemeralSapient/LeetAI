I will update this markdown file later for full details and as for now,

It currently fetches question [ including tags ] and solutions; then stores it on MySQL database

I'm planning to complete python script complete AI process for creating collection of series for each topic so that it'll be easier to understand DSA or so.

Front-end, I'm not sure when but then it's planned to be go with React and Ant design.

# Docker

  - `docker-compose up -d` will perform required process
  - `docker exec -it leetdb mysql -u"root" -p"password"` will open up mysql shell [use leet database]

# Without docker

  - **Required** : python3, pip3, unzip, wget, mariadb-client (or) mysql-client ; And set env MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD
  - `python3 start.py` will perform the process
  - use mysql client to connect with server and use leet database in it.

