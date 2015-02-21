import time
import json
from urllib.request import urlopen, quote

MAPS_API_TEMPLATE = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode=car&units=metric"


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
    "Kansas City, MO": ["St. Louis, MO", "Dallas, TX"],
    "Minneapolis, MN": ["Milwaukee, WI", "Seattle, WA"],
    "Seattle, WA": ["Minneapolis, MN", "Portland, OR"],
    "Portland, OR": ["Seattle, WA", "Denver, CO", "San Francisco, CA"],
    "Denver, CO": ["Portland, OR", "Las Vegas, NV", "Albuquerque, NM"],
    "San Francisco, CA": ["Portland, OR", "Los Angeles, CA"],
    "Los Angeles, CA": ["San Francisco, CA", "Las Vegas, NV", "Phoenix, AZ"],
    "Las Vegas, NV": ["Los Angeles, CA", "Phoenix, AZ", "Denver, CO"],
    "Phoenix, AZ": ["Las Vegas, NV", "Los Angeles, CA", "Albuquerque, NM"],
    "Albuquerque, NM": ["Phoenix, AZ", "Denver, CO", "Dallas, TX"],
    "Dallas, TX": ["Albuquerque, NM", "Houston, TX", "St. Louis, MO", "Atlanta, GA", "Kansas City, MO", "Austin, TX"],
    "Houston, TX": ["Dallas, TX", "San Antonio, TX"],
    "Austin, TX": ["San Antonio, TX", "Dallas, TX"],
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

if __name__ == '__main__':
    adjacency_list_with_distance = {}
    for city_from in adjacency_list:
        list_for_city_from = []
        for city_to in adjacency_list[city_from]:
            distance = get_city_distance(city_from, city_to)
            list_for_city_from.append({city_to: distance})
            print("Distance from {} to {}: {}".format(city_from, city_to, distance))
            time.sleep(.5)
        adjacency_list_with_distance[city_from] = list_for_city_from
    print(adjacency_list_with_distance)
    with open("city_data.json", "w") as f:
        f.write(json.dumps(adjacency_list_with_distance))

