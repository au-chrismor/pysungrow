from . import APP_KEY, SECRET_KEY
import requests

def sglogin(app_key, secret_key, user_account, user_password, url=None):
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
                "user_account": user_account,
                "user_password": user_password
            }

        )
#        logging.debug(f'login(): Response={r.text}')
        json_data = r.json()
        sec_token = json_data['result_data']['token']
    except Exception as ex:
        sec_token = None
    return sec_token
