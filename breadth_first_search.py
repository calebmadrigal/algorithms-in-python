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
from collections import deque


def unroll_shortest_path(current, optimal_parent_map, path=()):
    if current is None:  # Reached the start node
        return path
    else:
        return unroll_shortest_path(optimal_parent_map[current], optimal_parent_map, (current,) + path)


def breadth_first_search(from_city, to_city, city_data):
    to_visit = deque([from_city])
    visited = set([from_city])
    parent_map = {from_city: None}

    while to_visit != []:
        current = to_visit.popleft()  # Treat to_visit as queue
        print("Visiting:", current)
        neighbors = city_data[current].keys()

        for n in neighbors:
            if n == to_city:
                parent_map[n] = current
                return unroll_shortest_path(to_city, parent_map)

            elif n not in visited:
                parent_map[n] = current
                visited.add(n)
                to_visit.append(n)

    return None


def get_city_data():
    city_data = None
    with open("city_data.json","r") as f:
        city_data = json.loads(f.read())
    return city_data


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

    print(breadth_first_search(city_from, city_to, city_data))

