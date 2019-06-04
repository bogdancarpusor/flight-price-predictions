import os
import backend


if __name__ == '__main__':
    app_name = os.environ['APP_NAME']
    if app_name == 'api':
        backend.start_api()
    elif app_name == 'automation':
        backend.start_automation()
