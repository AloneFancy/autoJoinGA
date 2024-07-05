import requests, re, json
from dotenv import load_dotenv
import os
from datetime import date, datetime
from requests_html import HTMLSession
from pathlib import PurePosixPath
import logging
from setup_logger import setup_logger


class API_tasking:
    def __init__(self, apis):
        self.apis = apis
        self.headers = {
            "Cookie": os.environ.get("Cookie"),
            "X-Recaptcha-Token": os.environ.get("XRecaptchaToken"),
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self.payload = os.environ.get("Twitter")

    def doTask(self, giveaway, task):
        payload = self.payload
        try:
            logger.info(
                requests.post(
                    "https://skinsmonkey.com/api/giveaway/"
                    + giveaway
                    + "/requirement/"
                    + task
                    + "/complete",
                    headers=self.headers,
                    data=payload,
                ).content
            )
        except:
            logger.critical("Tokens are expired")

    def read_giveaway(self):
        for api in self.apis:
            content = json.loads(
                requests.get(
                    "https://skinsmonkey.com/api/giveaway/" + api, headers=self.headers
                ).content
            )
            for task in content["requirements"]:
                if "userUnlockedAt" in task:
                    unlockedAt = datetime.timestamp(
                        datetime.fromisoformat(task["userUnlockedAt"])
                    )

                    if check_COME_BACK(unlockedAt, task["repetitiveIntervalSeconds"]):
                        self.doTask(api, task["id"])
                else:
                    self.doTask(api, task["id"])


def check_COME_BACK(unlockedAt, repeat):
    if repeat is None:
        return False
    now = datetime.timestamp(datetime.now())
    if now < unlockedAt + repeat:
        return False
    return True


def getFilePath():
    filePath = ""
    if not os.path.exists("logs/"):
        os.makedirs("logs")
    if os.environ.get("logsPath") == None:
        filePath = "./logs/skinsmonkey.log"
    else:
        filePath = (
            str(PurePosixPath(os.environ.get("logsPath"))) + "/logs/skinsmonkey.log"
        )
    return filePath
    

def logger_config():
    global logger
    formatter = logging.Formatter("%(asctime)s::%(levelname)s::%(message)s")
    filePath = getFilePath()                            
    logger = setup_logger(__name__,log_file=filePath,formatter=formatter)

def main():
    
    logger_config()
    url = "https://skinsmonkey.com/api/giveaway/"
    r = requests.get(url, cookies={}).content
    apis = []

    for giveaway in json.loads(r):
        apis.append(giveaway["id"])
    logger.info(apis)

    test = API_tasking(apis)
    test.read_giveaway()


if __name__ == "__main__":
    load_dotenv()
    main()
