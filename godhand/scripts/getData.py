import json
import requests
from datetime import datetime, timezone

url = "https://anarch.games/godhand/wiki/diff.txt"
# upload_path = "godhand/data/godhand_stats_"+datetime.now().strftime("%Y%m%d-%H%M%S")+".txt"
path = "godhand/data/diff-history.json"
timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

response = requests.get(url)
with open(path, "r") as f:
  data = json.load(f)

if response.status_code == 200:
  # with open(upload_path, "wb") as file:
  #   file.write(response.content)
  pulled_raw_data = response.text
  pulled_raw_data = pulled_raw_data.splitlines()
  pulled_data = {}
  for line in pulled_raw_data:
    name,diff,rating = line.split(',')
    rating = int(rating)
    if name not in data:
      data[name] = {}
    if diff not in data[name]:
      data[name][diff] = []
    data[name][diff].append({"time": timestamp, "rating": rating})
  with open(path, "w") as f:
    json.dump(data, f)

  