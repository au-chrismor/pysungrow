import logging
from sglogin import sglogin
from sgservicelist import sgservicelist
from sgdevicelist import sgdevicelist


APP_KEY=None
SECRET_KEY=None
URL='https://augateway.isolarcloud.com'
LOGIN=None
PS_LIST=None
DEV_LIST=None
INVERTER_DATA=None

class PySungrow:
    def __init__(self, app_key=None, secret_key=None, url=None):
        if url is not None:
            URL=url
        LOGIN = f'{URL}/openapi/login'
        PS_LIST = f'{URL}/openapi/getPowerStationList'
        DEV_LIST = f'{URL}/openapi/getDeviceList'
        INVERTER_DATA = f'{URL}/openapi/getPVInverterRealTimeData'

        if app_key is not None:
            APP_KEY=app_key
        else:
            logging.error('PySungrow: app_key MUST be specified')
            return
        if secret_key is not None:
            SECRET_KEY=secret_key
        else:
            logging.error('PySungrow: secret_key MUST be specified')


    def login(self, user_account, user_password):
        return sglogin(app_key=APP_KEY, secret_key=SECRET_KEY, user_account=user_account, user_password=user_password, url=LOGIN)


    def service_list(self, token):
        return sgservicelist(app_key=APP_KEY, secret_key=SECRET_KEY, token=token, url=PS_LIST)


    def device_list(self, token, ps_id):
        return sgdevicelist(app_key=APP_KEY, secret_key=SECRET_KEY, token=token, ps_id=ps_id, url=DEV_LIST)
