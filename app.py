# app.py
from flask import Flask, request  # import main Flask class and request object
import subprocess
import os

app = Flask(__name__)  # create the Flask app


@app.route("/get_route")
def get_route():
    city = request.args.get("city")  # if key doesn't exist, returns None
    difficulty = request.args.get("difficulty")  # if key doesn't exist, returns None
    points_of_interest = subprocess.run(
        #example test run
        [
            "python3 point_selector.py --city=Berlin --difficulty=1"
        ],
        stdout=subprocess.PIPE,
        check=True,
        shell=True,
        env={"G_API_KEY": "api__key"},
    ).stdout
   
    return points_of_interest
