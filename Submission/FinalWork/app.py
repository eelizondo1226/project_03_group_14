from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper


app = Flask(__name__)
sql = SQLHelper()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/chartjs')
def chartjs():
    return render_template('chartjs.html')

@app.route('/workcited')
def workcited():
    return render_template('workcited.html')

@app.route("/api/storms_by_month")
def storms_by_month():
    data = sql.query_storms_by_month()
    return jsonify(data)
@app.route("/api/hurricane_number")
def hurricane_number():
    data = sql.query_hurricane_number_bar()
    return jsonify(data)
@app.route("/api/hurricane_by_decade")
def hurricane_by_decade():
    data = sql.query_hurricane_by_decade()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
