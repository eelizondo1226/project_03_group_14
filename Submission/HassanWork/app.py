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

@app.route('/cameras')
def cameras():
    return render_template('cameras.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chartjs')
def chartjs():
    return render_template('chartjs.html')



@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/single')
# def single():
#     return render_template('single.html')



@app.route('/bar-chart')
def bar_chart():
    return render_template('bar_chart.html')

@app.route('/workcited')
def workcited():
    return render_template('workcited.html')

@app.route('/api/data')
def api_data():
    data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'values': [10, 20, 15, 30, 25]
    }
    return jsonify(data)

# SQL Queries
@app.route("/api/v1.0/get_dashboard/<min_attempts>/<region>")
def get_dashboard(min_attempts, region):
    min_attempts = int(min_attempts) # cast to int

    bar_data = sql.get_bar(min_attempts, region)
    pie_data = sql.get_pie(min_attempts, region)
    table_data = sql.get_table(min_attempts, region)

    data = {
        "bar_data": bar_data,
        "pie_data": pie_data,
        "table_data": table_data
    }
    return(jsonify(data))





# @app.route('/api/filter-data', methods=['GET'])
# def filter_data():
#     all_data = [
#         {'category': 'A', 'value': 10},
#         {'category': 'B', 'value': 20},
#         {'category': 'A', 'value': 15},
#         {'category': 'C', 'value': 30},
#         {'category': 'B', 'value': 25}
#     ]
#     category = request.args.get('category', default='A', type=str)
#     filtered_data = [item for item in all_data if item['category'] == category]
#     return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
