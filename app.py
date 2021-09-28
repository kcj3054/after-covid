from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

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