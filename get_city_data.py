""" Horrible run-once code to download city data. """

import time
import json
import itertools
from urllib.request import urlopen, quote

MAPS_API_TEMPLATE = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode=car&units=metric"
STRAIGHT_DISTANCE_TEMPLATE = "http://www.travelmath.com/flying-distance/from/{}/to/{}"


def miles_to_meters(miles):
    return miles / 0.00062137


def get_straight_distance(city_from, city_to):
    city_from = '+'.join(city_from.split(' '))
    city_to = '+'.join(city_to.split(' '))
    url = STRAIGHT_DISTANCE_TEMPLATE.format(city_from, city_to)
    raw_response = urlopen(url).read().decode(encoding='UTF-8')
    miles = raw_response.find("miles", 20000)-10
    start_index=raw_response.find(r'"', miles)+2
    end_index = raw_response.find(r' ', start_index+1)
    straight_distance = raw_response[start_index:end_index]
    num = int(straight_distance.replace(',',''))
    return miles_to_meters(num)


def get_city_distance(city_from, city_to):
    url = MAPS_API_TEMPLATE.format(quote(city_from), quote(city_to))
    raw_response = urlopen(url).read().decode(encoding='UTF-8').replace('\n','')
    parsed_response = json.loads(raw_response)
    distance_in_meters = parsed_response['rows'][0]['elements'][0]['distance']['value']
    return distance_in_meters


adjacency_list = {
    "Milwaukee, WI": ["Chicago, IL", "Minneapolis, MN"],
    "Chicago, IL": ["Milwaukee, WI", "St. Louis, MO", "Indianapolis, IN", "Detroit, MI", "Cleveland, OH"],
    "Detroit, MI": ["Chicago, IL", "Cleveland, OH"],
    "St. Louis, MO": ["Chicago, IL", "Kansas City, MO", "Indianapolis, IN", "Atlanta, GA", "Dallas, TX"],
    "Kansas City, MO": ["St. Louis, MO", "Dallas, TX", "Denver, CO"],
    "Minneapolis, MN": ["Milwaukee, WI", "Seattle, WA"],
    "Seattle, WA": ["Minneapolis, MN", "Portland, OR"],
    "Portland, OR": ["Seattle, WA", "Denver, CO", "San Francisco, CA"],
    "Denver, CO": ["Portland, OR", "Las Vegas, NV", "Albuquerque, NM", "Kansas City, MO", "San Francisco, CA"],
    "San Francisco, CA": ["Portland, OR", "Los Angeles, CA", "Denver, CO"],
    "Los Angeles, CA": ["San Francisco, CA", "Las Vegas, NV", "Phoenix, AZ"],
    "Las Vegas, NV": ["Los Angeles, CA", "Phoenix, AZ", "Denver, CO"],
    "Phoenix, AZ": ["Las Vegas, NV", "Los Angeles, CA", "Albuquerque, NM"],
    "Albuquerque, NM": ["Phoenix, AZ", "Denver, CO", "Dallas, TX"],
    "Dallas, TX": ["Albuquerque, NM", "Houston, TX", "St. Louis, MO", "Atlanta, GA", "Kansas City, MO", "Austin, TX"],
    "Houston, TX": ["Dallas, TX", "San Antonio, TX"],
    "Austin, TX": ["San Antonio, TX", "Dallas, TX"],
    "San Antonio, TX": ["Austin, TX", "Houston, TX"],
    "Atlanta, GA": ["Dallas, TX", "St. Louis, MO", "Jacksonville, FL", "Cincinnati, OH"],
    "Cincinnati, OH": ["Atlanta, GA", "Indianapolis, IN", "Pittsburgh, PA", "Cleveland, OH"],
    "Cleveland, OH": ["Chicago, IL", "Detroit, MI", "Pittsburgh, PA", "Cincinnati, OH"],
    "Indianapolis, IN": ["Chicago, IL", "Cincinnati, OH", "St. Louis, MO"],
    "Pittsburgh, PA": ["Cleveland, OH", "Cincinnati, OH", "Philadelphia, PA"],
    "Philadelphia, PA": ["Pittsburgh, PA", "New York, NY"],
    "New York, NY": ["Philadelphia, PA", "Boston, MA"],
    "Boston, MA": ["New York, NY"],
    "Jacksonville, FL": ["Atlanta, GA", "Orlando, FL"],
    "Orlando, FL": ["Jacksonville, FL", "Miami, FL"],
    "Miami, FL": ["Orlando, FL"],
}

def get_in_between_distances():
    adjacency_list_with_distance = {}
    for city_from in adjacency_list:
        distances_to_adjacent_cities = {}
        for city_to in adjacency_list[city_from]:
            distance = get_city_distance(city_from, city_to)
            distances_to_adjacent_cities[city_to] = distance
            print("Distance from {} to {}: {}".format(city_from, city_to, distance))
            time.sleep(.5)
        adjacency_list_with_distance[city_from] = distances_to_adjacent_cities
    print(adjacency_list_with_distance)
    with open("city_data.json", "w") as f:
        f.write(json.dumps(adjacency_list_with_distance))


def get_straight_distances():
    all_cities = list(adjacency_list.keys())
    straight_distances = dict([(key, {}) for key in all_cities])
    for (city_from, city_to) in itertools.permutations(all_cities, 2):
        distance = get_straight_distance(city_from, city_to)
        straight_distances[city_from][city_to] = distance
        print("Straight distance from {} to {} is {}".format(city_from, city_to, distance))

    with open("straight_city_distances.json", "w") as f:
        f.write(json.dumps(straight_distances))

if __name__ == '__main__':
    get_in_between_distances()
    #get_straight_distances()

