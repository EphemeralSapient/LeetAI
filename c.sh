#/bin/bash

# apt-get update && apt-get install -y wget unzip mysql-client python3 python3-pip

echo "Downloading the leetcode data"
wget -q -nv https://github.com/doocs/leetcode/archive/refs/heads/main.zip
echo "Downloaded, now extracting"
unzip -qq main.zip
rm main.zip

echo "Extracted, now processing"
cat ./leetcode-main/solution/*/*/README_EN.md > data.txt
rm leetcode-main -rf

sed 's/[^\x00-\x7F]//g' data.txt > data
rm data.txt
