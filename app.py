from flask import Flask, Response, render_template, request, redirect, url_for
import subprocess, os
import mann, skinsmonkey
from dotenv import load_dotenv


app = Flask(__name__, template_folder="templates")

# subprocess.run(["make"])
load_dotenv()


def print_logs(path):
    f = open(path, "r")
    content = f.read()
    if content:
        return Response(content, mimetype="text/plain")
    return Response("**Empty**", mimetype="text/plain")


@app.route("/mann")
def _mann():
    return print_logs("logs/mann.log")


@app.route("/skinsmonkey", methods=["GET", "POST"])
def _skinsmoneky():
    return print_logs("logs/skinsmonkey.log")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global SkinsCookie, XRecaptchaToken, MannCookie
        SkinsCookie = request.form["skins-cookie"]
        XRecaptchaToken = request.form["XRecaptchaToken"]
        MannCookie = request.form["MannCookie"]
        if SkinsCookie:
            os.environ["Cookie"] = SkinsCookie
        if XRecaptchaToken:
            os.environ["XRecaptchaToken"] = XRecaptchaToken
        if MannCookie:
            os.environ["MannCookie"] = MannCookie
        try:
            skinsmonkey.main()
            mann.main()
        except:
            return Response("A token is wrong", mimetype="text/plain")
        return "Form submitted!"
    return render_template("index.html", message="error")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
