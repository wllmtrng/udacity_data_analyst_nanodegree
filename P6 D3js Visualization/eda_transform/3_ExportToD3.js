/**
 * Created by wtruong on 8/28/16.
 */

var
  _ = require("lodash"),
  children = require("./output.json"),
  root = {
    "name": "Occupations",
    "children": []
  };

root["children"] = _(children)
  .groupBy("Occupation")
  .mapValues((innerChildren) => {
    return innerChildren.map((child) => {
      return {
        "name": String(child["ProsperScore"]),
        "size": child["count"]
      }
    });
  })
  .toPairs()
  .map((pair) => _.zipObject(["name", "children"], pair))
  .value();

//  x = _.zipObject(["name", "children"], byOccupation);

//
//
// _.each(byOccupation.keys(), occupation => ()
//
// _.reduce(byOccupation.values(), (acc, child) => {return acc}, {name: child[0]["Occupation"]})
//       .value();

require("fs").writeFileSync("./d3output.json", JSON.stringify(root, null, 2));
