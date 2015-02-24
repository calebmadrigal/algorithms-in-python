""" Breadth-first search

This ignores the distance between the city data, and just cares about number of hops.

This implementation is admittedly tightly-coupled to my particular city_data data set
(to add clarity in understanding by making it tied to concrete data).

The city_data is a list of 28 large cities in the United States, with some considered
neighbors of the others. This would be the case in, say, a bus system which only
travels between major cities. Using the shortest path on this data outputs
the best path through these major cities.

The format of city_data is like this:

{   "Milwaukee, WI": {"Minneapolis, MN": 542093, "Chicago, IL": 148198},
    "Minneapolis, MN": {"Seattle, WA": 2665735, "Milwaukee, WI": 541660}, ... }

So the neighbors of a city node can be found like this: list(city_data["Milwaukee, WI"].keys())

"""

import json
import sys


def unroll_shortest_path(current, optimal_parent_map, path=()):
    if current is None:  # Reached the start node
        return path
    else:
        return unroll_shortest_path(optimal_parent_map[current], optimal_parent_map, (current,) + path)


def get_city_data():
    city_data = None
    with open("city_data.json","r") as f:
        city_data = json.loads(f.read())
    return city_data


def depth_first_search(from_city, to_city, city_data):
    visited = set()

    def _depth_first_search(from_city, to_city, city_data, path=()):
        print("Checking: {}".format(from_city))
        if from_city == to_city:
            return path
        elif len(visited) == len(city_data):
            print("HIT")
            return None
        else:
            neighbors = list(city_data[from_city].keys())
            visited.add(from_city)
            for n in neighbors:
                if n not in visited:
                    result = _depth_first_search(n, to_city, city_data, path+(n,))
                    if result is not None:
                        return result

    return _depth_first_search(from_city, to_city, city_data)


if __name__ == '__main__':
    city_data = get_city_data()
    try:
        city_from = sys.argv[1]
        city_to = sys.argv[2]
    except IndexError:
        print("Usage:", sys.argv[0], "\"from city\" \"to city>\"")
        print("City choices:")
        for city in city_data:
            print("   -", city)
        sys.exit(1)

    print(depth_first_search(city_from, city_to, city_data))

