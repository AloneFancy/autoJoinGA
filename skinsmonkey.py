from tarfile import NUL
import requests, re, json, chompjs
from dotenv import load_dotenv
import os 
from datetime import date, datetime

from sympy import true
from torch import NoneType

load_dotenv()


class API_tasking:
    def __init__(self, apis):
        self.apis = apis
        self.headers = {
            "Cookie": os.environ.get("Cookie"),
            "X-Recaptcha-Token": os.environ.get("X-Recaptcha-Token"),
            "Content-Type": "application/x-www-form-urlencoded",
        }

    def doTask(self, giveaway, task):
        payload = os.environ.get("Twitter")
        print(
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

    def read_giveaway(self):
        for api in self.apis:
            content = json.loads(
                requests.get(
                    "https://skinsmonkey.com/api/giveaway/" + api, headers=self.headers
                ).content
            )
            for task in content["requirements"]:
                if "userUnlockedAt" in task:
                    unlockedAt = datetime.timestamp(datetime.fromisoformat(task["userUnlockedAt"]))                    
                        
                    if check_COME_BACK(unlockedAt,task["repetitiveIntervalSeconds"]):
                        self.doTask(api, task["id"])
                else:
                    self.doTask(api, task["id"])

def check_COME_BACK(unlockedAt, repeat):
    if (repeat is None):
        return False
    now = datetime.timestamp(datetime.now())
    if now < unlockedAt + repeat:
        return False
    return True


# url = "https://skinsmonkey.com/free-csgo-skins"
# cd = {}
# r = requests.get(url, cookies=cd)
# regex = r"window\.(.+)tasks"
# regexGA = r"giveaways:(.+)]"

# js_obj = (
#     "{giveaways:" + re.search(regexGA, re.findall(regex, r.text)[0]).group(0)[10:] + "}"  # type: ignore
# )
# py_obj = chompjs.parse_js_object(js_obj)

url = "https://skinsmonkey.com/api/giveaway/"
r = requests.get(url, cookies={}).content
apis = []

for giveaway in json.loads(r):
    apis.append(giveaway["id"])
print(apis)

test = API_tasking(apis)
test.read_giveaway()
