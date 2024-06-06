from flask import Flask, jsonify, render_template
import subprocess
from pymongo import MongoClient
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['GET'])
def run_script():
    subprocess.run(['python', 'twitter_trends.py'])

    client = MongoClient('mongodb://localhost:27017/')
    db = client['twitter_trends']
    collection = db['trends']

    index_name = "trends_text_index"
    existing_indices = collection.index_information()
    for index in existing_indices.values():
        if index.get('name') == index_name:
            collection.drop_index(index_name)

    collection.create_index(
        [
            ("trend1", "text"),
            ("trend2", "text"),
            ("trend3", "text"),
            ("trend4", "text"),
            ("trend5", "text")
        ],
        name=index_name
    )

    result = collection.find().sort('_id', -1).limit(1)

    if collection.count_documents({}) > 0:
        result = result[0]
    else:
        result = {} 

# Check if 'unique_id' key exists in result dictionary
    if 'unique_id' in result:
        unique_id = result['unique_id']
    else:
        unique_id = None  

    return jsonify({
        'unique_id': result['unique_id'],
        'trend1': result['trend1'],
        'trend2': result['trend2'],
        'trend3': result['trend3'],
        'trend4': result['trend4'],
        'trend5': result['trend5'],
        'date_time': result['date_time'],
        'ip_address': result['ip_address']
    })
