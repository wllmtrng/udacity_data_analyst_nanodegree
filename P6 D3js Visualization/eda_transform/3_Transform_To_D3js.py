import json
import collections
with open("./output.json") as f:
    jsonfile = json.loads(f.read())

#sorted_by_score = sorted(jsonfile, key=lambda x: (x["ProsperScore"], -x["count"]))
sorted_by_score = sorted(jsonfile, key=lambda x: (x["ProsperScore"], x["Occupation"]))

score_to_occupations = collections.OrderedDict()

# For loop to create this
# {
#   1: {
#      A: 2,
#      B: 1,
#      C: 3
#   }
#   ...
# }
#
#
for row in sorted_by_score:
    score = str(row["ProsperScore"])
    if score not in score_to_occupations:
        score_to_occupations[score] = collections.OrderedDict()
    score_to_occupations[score][row["Occupation"]] = row["count"]

result = [dict(zip(("ProsperScore", "freq"), x)) for x in score_to_occupations.iteritems()]

with open("./d3output.json", 'w') as of:
    json.dump(sorted(result, key=lambda x:int(x["ProsperScore"])), of, indent=2)
