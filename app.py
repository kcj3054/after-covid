from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

from _google_flight_project import insert_all

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

#API 역할을 하는 부분
@app.route('/info', methods=['GET'])
def show_info():
    air_info = list(db.mydb.find({}, {'_id' : False}))
    return jsonify({'my_air_info' : air_info})


@app.route('/info', methods=['POST'])
def update_info():
    info_receive = request.form['info_give']


@app.route('/info', methods=['DELETE'])
def delete_info():

    return jsonify({'msg': '삭제완료'})

from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient('localhost', 27017, username="test", password="test")
db = client.dbproject

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/popup')
def popup():
    return render_template("popup.html")

@app.route('/detail')
def detail():
    return render_template("detail.html")

@app.route('/api/save_flight', methods=['POST'])
def save_flight():
    go_want = request.form['go_want']
    go_desti = request.form['go_desti']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    insert_all(go_want, go_desti, start_time, end_time)

    return jsonify({'result': 'success', 'msg': '저장 성공!'})

@app.route('/api/delete_flight', methods=['POST'])
def delete_flight():
    data_receive = request.form['data_give']
    db.flightinfo.delete_one({'data': data_receive})
    return jsonify({'result': 'success', 'msg': '삭제 성공!'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
