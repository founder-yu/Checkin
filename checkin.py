import json
import logging
import requests
import argparse

class CheckIn(object):
    client = requests.Session()
    login_url = "https://w1.v2free.net/auth/login"
    sign_url = "https://w1.v2free.net/user/checkin"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_in(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
            "Referer": "https://w1.v2free.net/auth/login",
        }
        data = {
            "email": self.username,
            "passwd": self.password,
            "code": "",
        }
        self.client.post(self.login_url, data=data, headers=headers)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
            "Referer": "https://w1.v2free.net/user",
        }
        response = self.client.post(self.sign_url, headers=headers)

        logging.info(self.username +" "+ response.json()["msg"])


if __name__ == "__main__":
    LOG_FORMAT = "%(asctime)s\t%(levelname)s\t%(message)s"
    logging.basicConfig(filename='flow.log',
                        level=logging.INFO, format=LOG_FORMAT)

    parser = argparse.ArgumentParser(description='V2ray签到脚本')
    parser.add_argument('--username', type=str, help='账号')
    parser.add_argument('--password', type=str, help='密码')
    args = parser.parse_args()
    helper = CheckIn(args.username, args.password)
    helper.check_in()
