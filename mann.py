import requests, json, re
from requests_html import HTMLSession
from dotenv import load_dotenv
import os


load_dotenv()


class giveaways:
    def __init__(self):
        self.headers = {"Cookie": os.environ.get("MannCookie")}

    def gather_info(self):

        self.content = requests.post(
            "https://mannco.store/requests/raffle.php?mode=getPublic"
        )
        session = HTMLSession()
        r = session.get("https://mannco.store/requests/raffle.php?mode=getPublic")
        self.url = json.loads(r.content)

        print(list)
        for url in self.url:
            payload = {"mode": "join", "url": url["url"]}
            print(
                "https://mannco.store/requests/raffle.php?mode=join&url="
                + url["url"]
                + " "
                + str(
                    session.get(
                        "https://mannco.store/requests/raffle.php?mode=join&url="
                        + url["url"],
                        headers=self.headers,
                        data=payload,
                    ).text
                )
            )


a = giveaways()
a.gather_info()
