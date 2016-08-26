import json
import collections
with open("./output.json") as f:
    jsonfile = json.loads(f.read())

sorted_by_score = sorted(jsonfile, key=lambda x: x["ProsperScore"])

score_to_occupations = collections.defaultdict(lambda: {})
for row in sorted_by_score:
    score_to_occupations[str(row["ProsperScore"])][row["Occupation"]] = row["count"]

result = [dict(zip(("ProsperScore", "freq"), x)) for x in score_to_occupations.iteritems()]

with open("./d3output.json", 'w') as of:
    json.dump(sorted(result, key=lambda x:int(x["ProsperScore"])), of, indent=2)
