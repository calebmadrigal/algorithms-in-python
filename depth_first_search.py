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


def depth_first_search_iter(from_city, to_city, city_data):
    to_visit = [from_city]
    visited = set([from_city])
    parent_map = {from_city: None}

    while to_visit != []:
        current = to_visit.pop()
        visited.add(current)
        neighbors = city_data[current].keys()

        for n in neighbors:
            if n == to_city:
                parent_map[n] = current
                return unroll_shortest_path(to_city, parent_map)

            elif n not in visited:
                parent_map[n] = current
                to_visit.append(n)

    return None


def depth_first_search(from_city, to_city, city_data):
    visited = set()

    def _depth_first_search(from_city, to_city, city_data, path=(from_city,)):
        # If destination found, return the path hereto compiled
        if from_city == to_city:
            return path
        else:
            visited.add(from_city)
            neighbors = city_data[from_city].keys()
            unvisited_neighbors = [n for n in neighbors if n not in visited]

            # If there are no more unvisited neighbors, this path doesn't lead to the goal
            if unvisited_neighbors == []:
                return None

            # Else, for each unvisited neighbor, recursively try to reach the solution
            # from it as the "from_city". Also update the path
            for n in unvisited_neighbors:
                result = _depth_first_search(n, to_city, city_data, path+(n,))
                if result is not None:
                    return result

    return _depth_first_search(from_city, to_city, city_data)


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

    print("Recursive:", depth_first_search(city_from, city_to, city_data))
    print("\nIterative:", depth_first_search_iter(city_from, city_to, city_data))

