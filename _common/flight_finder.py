import requests
import json
from pprint import pprint

url = 'https://api.skypicker.com/umbrella/graphql?featureName=calendar'
data = {
    "query": """
query AggregationFlights ($parameters: AggregationParameters!, $pagination: Pagination) {
get_aggregation_flights(
  parameters: $parameters
  pagination: $pagination
) {
  currencyRate
  currency
  connections
  allStopoverAirports
  allAirlines
  data {
    map {
      cityId
      sortOrder
      price
    }
    calendar {
      date
      price
    }
  }
}
}   
  """,
    "variables": {
        "parameters": {
            "adult_hand_bag": [0],
            "adult_hold_bag": [0],
            "adults": 1,
            "affilid": "skypicker",
            "asc": 1,
            "child_hand_bag": [],
            "child_hold_bag": [],
            "children": 0,
            "dateFrom": "01/06/2019",
            "dateTo": "01/01/2021",
            "featureName": "calendar",
            "flyFrom": "airport:OTP",
            # "flyFrom": "airport:IAS",
            "infants": 0,
            "locale": "US",
            "one_per_date": True,
            "oneforcity": False,
            "partner": "skypicker",
            "refresh": "fast",
            "sort": "quality",
            # "to": "45.76-4.84-250km",
            "to": "airport:RAK",
            "typeFlight": "oneway",
            "v": 3,
            "vehicle_type": ["aircraft", "bus", "train"]
        }
    }
}
headers = {
    'Content-Type': 'application/json',
    'Origin': 'https://www.kiwi.com',
    'Referer': 'https://www.kiwi.com/us/search/tiles/iasi-international-iasi-romania/lyon-france-250km/2019-08-19/no-return',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'X-Agent': 'web',
    'X-API-Version': "3",
}
# r = requests.post(url, json=data, headers=headers)

# print(r.status_code, r.reason)

# Add support for cities, areas instead of only airports
arrival_places = [
    {'name': 'Marrakech', 'airport': 'RAK', 'city_code': 'marrakech_poi'},
    {'name': 'New York', 'airport': 'JFK', 'city_code': 'new-york-city_ny_us'},
    # {'name': 'Tel Aviv', 'airport': 'TLV'},
    # {'name': 'Tokyo', 'airport': 'NRT'},
    {'name': 'Lisbon', 'airport': 'LIS', 'city_code': 'lisbon_pt'},
    {'name': 'Reykjavik', 'airport': 'KEF', 'city_code': 'reykjavik_is'},
    {'name': 'Vienna', 'airport': 'VIE', 'city_code': 'vienna_at'},
    # {'name': 'Vienna', 'airport': 'VIE'},
    # {'name': 'Larnaca', 'airport': 'LCA'},
    {'name': 'Bangkok', 'airport': 'DMK', 'city_code': "bangkok_th"},
    # {'name': 'Hanoi', 'airport': 'HAN'},
    # {'name': 'Mumbai', 'airport': 'BOM'},
    # {'name': 'Colombo', 'airport': 'CMB'},
    {'name': 'Ibiza', 'airport': 'IBZ', 'city_code': "palma_es"},
    {'name': 'Las Palmas', 'airport': 'LPA', 'city_code': "gran-canaria_poi"},
    {'name': 'Krakow', 'airport': 'KRK', 'city_code': 'krakow_pl'},
    # {'name': 'Istanbul', 'airport': 'LCA'},
]

# result = json.loads(r.text)

def get_price(a):
    return a['price']

results = {}

departure_places = [
    {'name': 'Iasi', 'airport': 'IAS', 'city_code': 'iasi_ro'},
    {'name': 'Bucharest', 'airport': 'OTP', 'city_code': 'bucharest_ro'},
    {'name': 'Berlin', 'airport': 'TXL', 'city_code': 'berlin_de'},
    {'name': 'Barcelona', 'airport': 'BCN', 'city_code': 'barcelona_es'},
    {'name': 'Paris', 'airport': '?', 'city_code': 'paris_fr'},
    {'name': 'Milano', 'airport': '?', 'city_code': 'milan_it'},
    {'name': 'London', 'airport': '?', 'city_code': 'london_gb'},
    {'name': 'Frankfurt', 'airport': '?', 'city_code': 'frankfurt_de'},
    {'name': 'Amsterdam', 'airport': '?', 'city_code': 'amsterdam_nl'},
]
for arrival_place in arrival_places:
    arrival_place_name = arrival_place['name']
    print('Processing {}'.format(arrival_place_name))
    results[arrival_place_name] = {}
    data['variables']['parameters']['to'] = arrival_place['city_code']
    for departure_place in departure_places:
        departure_place_name = departure_place['name']
        print('From {}'.format(departure_place_name))
        data['variables']['parameters']['flyFrom'] = departure_place['city_code']
        response = requests.post(url, json=data, headers=headers)
        results[arrival_place_name][departure_place_name] = json.loads(response.text)['data']['get_aggregation_flights']['data']['calendar']
        results[arrival_place_name][departure_place_name].sort(key=lambda x: x['price'])

# pprint(results)
final_result = {}
for arrival_city, departure_flights in results.items():
    final_result[arrival_city] = []
    for departure_city, flights in departure_flights.items():
        # string_result = "From {}: {}EUR in {} | {}EUR in {} | {}EUR in {}".format(departure_city, flights[0]['price'], flights[0]['date'], flights[1]['price'], flights['date'], flights[2]['price'], flights[2]['date'])
        # final_result[arrival_city][departure_city] = flights[:3]
        try:
            final_result[arrival_city].append({ 'city': departure_city, 'date': flights[0]['date'], 'price': flights[0]['price'] })
        except KeyError:
            print('error')
    final_result[arrival_city].sort(key=lambda x: x['price'])

pprint(final_result)

def ananlyze_flights():
    departure_cities = [
        {'name': 'Iasi', 'airport': 'IAS', 'city_code': 'iasi_ro'},
        {'name': 'Bucharest', 'airport': 'OTP', 'city_code': 'bucharest_ro'},
        {'name': 'Berlin', 'airport': 'TXL', 'city_code': 'berlin_de'},
        {'name': 'Barcelona', 'airport': 'BCN', 'city_code': 'barcelona_es'},
        {'name': 'Paris', 'airport': '?', 'city_code': 'paris_fr'},
        {'name': 'Milano', 'airport': '?', 'city_code': 'milan_it'},
        {'name': 'London', 'airport': '?', 'city_code': 'london_gb'},
        {'name': 'Frankfurt', 'airport': '?', 'city_code': 'frankfurt_de'},
        {'name': 'Amsterdam', 'airport': '?', 'city_code': 'amsterdam_nl'},
    ]
    arrival_cities = [
        {'name': 'Marrakech', 'airport': 'RAK', 'city_code': 'marrakech_poi'},
        {'name': 'New York', 'airport': 'JFK', 'city_code': 'new-york-city_ny_us'},
        # {'name': 'Tel Aviv', 'airport': 'TLV'},
        # {'name': 'Tokyo', 'airport': 'NRT'},
        {'name': 'Lisbon', 'airport': 'LIS', 'city_code': 'lisbon_pt'},
        {'name': 'Reykjavik', 'airport': 'KEF', 'city_code': 'reykjavik_is'},
        {'name': 'Vienna', 'airport': 'VIE', 'city_code': 'vienna_at'},
        # {'name': 'Vienna', 'airport': 'VIE'},
        # {'name': 'Larnaca', 'airport': 'LCA'},
        {'name': 'Bangkok', 'airport': 'DMK', 'city_code': "bangkok_th"},
        # {'name': 'Hanoi', 'airport': 'HAN'},
        # {'name': 'Mumbai', 'airport': 'BOM'},
        # {'name': 'Colombo', 'airport': 'CMB'},
        {'name': 'Ibiza', 'airport': 'IBZ', 'city_code': "palma_es"},
        {'name': 'Las Palmas', 'airport': 'LPA', 'city_code': "gran-canaria_poi"},
        {'name': 'Krakow', 'airport': 'KRK', 'city_code': 'krakow_pl'},
        # {'name': 'Istanbul', 'airport': 'LCA'},
    ]

if __name__ == '__main__':
    pprint(ananlyze_flights())
