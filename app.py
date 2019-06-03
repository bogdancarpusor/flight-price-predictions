import os
from automation.automation import start_automation
from api.api import start_api

if __name__ == '__main__':
    app_name = os.environ['APP_NAME']
    if app_name == 'automation':
        start_automation()
    elif app_name == 'api':
        start_api()