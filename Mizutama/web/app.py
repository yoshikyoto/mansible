# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, jsonify
import sys

#rootディレクトリでgunicornした時に正しく動くようにする
sys.path.append('web')
sys.path.append('.')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(port=port, debug=True)
