import json

path = "godhand/data/diff-history.json"

with open(path, "r") as f:
    data = json.load(f)

removed = 0

for name in data:
    for diff in data[name]:
        history = data[name][diff]

        if not history:
            continue

        new_history = [history[0]]

        for point in history[1:]:
            if point["rating"] != new_history[-1]["rating"]:
                new_history.append(point)
            else:
                removed += 1

        data[name][diff] = new_history

with open(path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Removed {removed} redundant data points.")