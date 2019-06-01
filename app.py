import os
from automation.automation import print_flight_info
from rest_api.api import start_api_server

def run_automation():
    print_flight_info()


if __name__ == '__main__':
    # run_automation()
    app_name = os.environ['APP_NAME']
    if app_name == 'api':
        start_api_server()