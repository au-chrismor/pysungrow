import requests
import logging


def sginverterdata(self, app_key=None, secret_key=None, token=None, ps_id=None, ser_num=None, ps_key=None, url=None):
    try:
        r = requests.request(
            method="POST",
            url=url,
            headers={
                "Content-Type": "application/json",
                "x-access-key": secret_key,
                "sys_code": "901"
            },
            json={
                "appkey": app_key,
                "token": token,
                "ps_id": ps_id,
                "ps_key_list": [ps_key],
                "sn_list": [ser_num]
            }
        )
        json_data = r.json()
        ret_data = json_data['result_data']
    except Exception as ex:
        ret_data = None
        logging.error(ex)
    return ret_data
