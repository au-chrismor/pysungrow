import logging
from sglogin import sglogin
from sgservicelist import sgservicelist


APP_KEY=None
SECRET_KEY=None
URL='https://augateway.isolarcloud.com'
LOGIN=None
PS_LIST=None
DEV_LIST=None
INVERTER_DATA=None

class PySungrow:
    def __init__(self, appKey=None, secretKey=None, url=None):
        if url is not None:
            URL=url
        LOGIN = f'{URL}/openapi/login'
        PS_LIST = f'{URL}/openapi/getPowerStationList'
        DEV_LIST = f'{URL}/openapi/getDeviceList'
        INVERTER_DATA = f'{URL}/openapi/getPVInverterRealTimeData'

        if appKey is not None:
            APP_KEY=appKey
        else:
            logging.error('PySungrow: app_key MUST be specified')
            return
        if secretKey is not None:
            SECRET_KEY=secretKey
        else:
            logging.error('PySungrow: secret_key MUST be specified')



    def login(self, user_account, user_password):
        return sglogin(app_key=APP_KEY, secret_key=SECRET_KEY, user_account=user_account, user_password=user_password, url=LOGIN)


    def service_list(self, token):
        return sgservicelist(app_key=APP_KEY, secret_key=SECRET_KEY, token=token, url=PS_LIST)
