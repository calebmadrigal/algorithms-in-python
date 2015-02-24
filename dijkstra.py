""" Dijkstra's shortest-path algorithm implementation

This implementation is admittedly tightly-coupled to my particular city_data data set
(to add clarity in understanding by making it tied to concrete data).

The city_data is a list of 28 large cities in the United States, with some considered
neighbors of the others. This would be the case in, say, a bus system which only
travels between major cities. Using the shortest path on this data outputs
the best path through these major cities.

The format of city_data is like this:

{   "Milwaukee, WI": {"Minneapolis, MN": 542093, "Chicago, IL": 148198},
    "Minneapolis, MN": {"Seattle, WA": 2665735, "Milwaukee, WI": 541660}, ... }

So it can be used like this: city_data["Milwaukee, WI"]["Chicago, IL"] to find the distance
from Chicago, IL to Milwaukee, WI.

Also, this implementation does NOT use a heap, which would be the optimal data structure
for storing unvisited nodes in. So in-place of a heap, it uses a sorted list of this structure:

unvisited = [ [distance_to_a, a], [distance_to_b, b] ]

It also uses a city_node_lookup dictionary in order to quickly access each of the [distance_to_a, a]
lists in O(1) time. It can use this to change the distance to a given node in the unvisited
list quickly. The unvisited list is re-sorted after each node is visited.

"""

import json
import sys


def unroll_shortest_path(current, optimal_parent_map, path=()):
    if current is None:  # Reached the start node
        return path
    else:
        return unroll_shortest_path(optimal_parent_map[current], optimal_parent_map, (current,) + path)


def dijkstra(start_city, end_city, city_data, verbose=False):
    if start_city == end_city:
        return (start_city,)

    # Inefficiency: should be implemented as a priority queue
    start_city_distance_entry = [0, start_city]
    city_node_lookup = {start_city: start_city_distance_entry}
    unvisited = [start_city_distance_entry]
    visited = set()
    optimal_parent = {start_city: None}
    for city_name in city_data.keys():
        if city_name != start_city:
            city_distance_entry = [999999999, city_name]
            city_node_lookup[city_name] = city_distance_entry
            unvisited.append(city_distance_entry)
            
    destination_reached = False
    while not destination_reached and unvisited != []:
        (distance_to_current, current) = unvisited.pop(0)
        if verbose:
            print("CURRENT: {}, DISTANCE: {:,} meters".format(current, distance_to_current))
        visited.add(current)
        neighbors = city_data[current].keys()
        if verbose:
            print("\tNEIGHBORS:", list(neighbors))
        for neighbor in neighbors:
            if verbose:
                print("\t\tNEIGHBOR: {}".format(neighbor))
            if neighbor == end_city:
                destination_reached = True
                optimal_parent[neighbor] = current
                break
            elif neighbor not in visited:
                total_distance_to_neighbor = distance_to_current + city_data[current][neighbor]
                # Changing the distance here changes the distance in unvisited
                city_distance_entry = city_node_lookup[neighbor]
                if city_distance_entry[0] > total_distance_to_neighbor:
                    if verbose:
                        print("\t\t\tNEW OPTIMAL PARENT ({}) TO {}".format(current, neighbor))
                    city_distance_entry[0] = total_distance_to_neighbor
                    optimal_parent[neighbor] = current

        unvisited.sort()  # Needed in the abscence of heap

    if destination_reached:
        return unroll_shortest_path(end_city, optimal_parent)
    else:
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

    print(dijkstra(city_from, city_to, city_data, False))

