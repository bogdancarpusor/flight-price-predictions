from datetime import date, timedelta
from pprint import pprint
from _common import kiwi_api

locations = [
    # {'name': 'Iasi', 'code': 'iasi_ro'},
    # {'name': 'Marrakech', 'code': 'marrakech_poi'},
    # {'name': 'Reykjavik', 'code': 'reykjavik_is'},
    {'name': 'New York', 'code': 'new-york-city_ny_us'},
    # {'name': 'Bucharest', 'code': 'bucharest_ro'},
    {'name': 'Berlin', 'code': 'berlin_de'},
    # {'name': 'Barcelona', 'code': 'barcelona_es'},
    # {'name': 'Paris', 'code': 'paris_fr'},
    {'name': 'London', 'code': 'london_gb'},
    {'name': 'Frankfurt', 'code': 'frankfurt_de'},
    {'name': 'Amsterdam', 'code': 'amsterdam_nl'},
    # {'name': 'Vienna', 'code': 'vienna_at'},
    # {'name': 'Bangkok', 'code': "bangkok_th"},
    # {'name': 'Ibiza', 'code': "palma_es"},
    # {'name': 'Las Palmas', 'code': "gran-canaria_poi"},
    # {'name': 'Krakow', 'code': 'krakow_pl'},
]


def map_flight_data(flight_data):
    return {
        'city_from': flight_data['cityFrom'],
        'city_to': flight_data['cityTo'],
        'distance': flight_data['distance'],
        'airport_from': flight_data['flyFrom'],
        'airport_to': flight_data['flyTo'],
        'kiwi_flight_id': flight_data['id'],
        'price': flight_data['price'],
        'departure_time': flight_data['route'][0]['dTimeUTC'],
        'arrival_time': flight_data['route'][0]['aTimeUTC'],
        'flight_number': flight_data['route'][0]['flight_no'],
        'cabin_class': flight_data['route'][0]['cabinClass'],
        'airline_code': flight_data['route'][0]['airline'],
    }


def test_flight_info(departure_date):
    result = []
    for departure_location in locations:
        # print('Getting flight info for {}'.format(departure_location['name']))
        for arrival_location in locations:
            # print('  Finding flights to {}'.format(arrival_location['name']))
            flights = kiwi_api.get_flight_prices_for_specific_date(departure_location['code'], arrival_location['code'], departure_date)
            result.extend([ map_flight_data(flight) for flight in flights])
    return result


def print_flight_info():
    reference_date = date(2019, 6, 6)
    current_date = date.today()
    delta = reference_date - current_date

    for i in range(delta.days):
        departure_date = current_date + timedelta(days=i)
        pprint(test_flight_info(departure_date.strftime("%d/%m/%Y")))
