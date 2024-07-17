FROM python:slim

# To download leetcode data
RUN apt-get update && apt-get install -y wget unzip mariadb-client 

# Env are set on .yml file, please do refer it

COPY . /app
WORKDIR /app

# Requirements for python
RUN pip install --no-cache-dir -r requirements.txt

# Optional I guess
EXPOSE 3306

CMD ["python", "start.py"]
