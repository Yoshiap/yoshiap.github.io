import requests
from datetime import datetime

url = "https://anarch.games/godhand/wiki/diff.txt"
upload_path = "godhand/data/godhand_stats_"+datetime.now().strftime("%Y%m%d-%H:%M:%S")+".txt"

response = requests.get(url)

if response.status_code == 200:
  with open(upload_path, "wb") as file:
    file.write(response.content)