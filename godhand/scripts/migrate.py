import json
import glob
from datetime import datetime

data_path = "godhand/data"
output_path = "godhand/data/diff-history.json"

data = {}

for path in sorted(glob.glob(f"{data_path}/godhand_stats_*.txt")):
    filename = path.split("/")[-1]

    # godhand_stats_20260830-193017.txt
    timestamp_str = filename.removeprefix("godhand_stats_").removesuffix(".txt")

    # Convert filename timestamp to ISO 8601 UTC
    timestamp = datetime.strptime(
        timestamp_str,
        "%Y%m%d-%H%M%S"
    ).isoformat() + "Z"

    print(f"Processing {filename} -> {timestamp}")

    with open(path, "r") as f:
        for line in f:
            name, diff, rating = line.strip().split(",")
            rating = int(rating)

            if name not in data:
                data[name] = {}

            if diff not in data[name]:
                data[name][diff] = []

            data[name][diff].append({
                "time": timestamp,
                "rating": rating
            })

with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Migrated {len(glob.glob(f'{data_path}/godhand_stats_*.txt'))} files.")