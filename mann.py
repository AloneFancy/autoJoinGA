import requests, json
from requests_html import HTMLSession
from dotenv import load_dotenv
import os
import logging
from pathlib import PurePosixPath
from setup_logger import setup_logger

class giveaways:
    def __init__(self):
        self.headers = {"Cookie": os.environ.get("MannCookie")}
    def send_req(self):
        for url in self.url:
            payload = {"mode": "join", "url": url["url"]}
            try:
                logger.info(
                    "https://mannco.store/requests/raffle.php?mode=join&url="
                    + url["url"]
                    + " "
                    + str(
                        self.session.get(
                            "https://mannco.store/requests/raffle.php?mode=join&url="
                            + url["url"],
                            headers=self.headers,
                            data=payload,
                        ).text
                    )
                )
            except:
                logger.critical("Tokens are expired")
    def gather_info(self):

        self.content = requests.post(
            "https://mannco.store/requests/raffle.php?mode=getPublic"
        )
        self.session = HTMLSession()
        r = self.session.get("https://mannco.store/requests/raffle.php?mode=getPublic")
        self.url = json.loads(r.content)              
        self.send_req()
        
        r = self.session.get("https://mannco.store/requests/raffle.php?mode=getPrivate",headers=self.headers)
        logger.info(r.content)
        self.url = json.loads(r.text)              
        self.send_req()


def getFilePath():
    filePath = ""
    if not os.path.exists("logs/"):
        os.makedirs("logs")
    if os.environ.get("logsPath") == None:
        filePath = "./logs/mann.log"
    else:
        filePath = str(PurePosixPath(os.environ.get("logsPath")))+"/logs/mann.log"
    return filePath
    
def logger_config():
    global logger
    formatter = logging.Formatter("%(asctime)s::%(levelname)s::%(message)s")
    filePath = getFilePath()                            
    logger = setup_logger(__name__,log_file=filePath,formatter=formatter)

def main():    
    logger_config()
    a = giveaways()
    a.gather_info()

if __name__ == "__main__":
    load_dotenv()
    main()
