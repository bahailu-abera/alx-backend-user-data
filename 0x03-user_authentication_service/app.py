#!/usr/bin/env python3
"""
Basic App
"""
from flask import Flask
from flask import Blueprint
from flask import jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """
    Landing page.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
