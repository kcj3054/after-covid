from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from pymongo import MongoClient
import jwt
import requests
import datetime
import hashlib

app = Flask(__name__)
CORS(app)

client = MongoClient('3.36.69.62', 27017, username="test", password="test")
db = client.dbproject

SECRET_KEY = 'end'

@app.route('/voice')
def voice():
    return render_template("voice.html")

@app.route('/image')
def main():
    return render_template("index.html")

# login이 기본페이지
@app.route('/')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.dbproject.insert_one({'id': id_receive, 'pw': pw_hash })

    return jsonify({'result': 'success'})

@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.dbproject.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
        }
        # 문자열객체는 decode가 없다네 ? ~
        token = jwt.encode(payload, 'end', algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.dbproject.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success'})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

@app.route('/popup')
def popup():
    return render_template("popup.html")

@app.route('/detail')
def detail():
    return render_template("detail.html")

@app.route('/api/save_flight', methods=['POST'])
def save_flight():
    go_want = request.form['current_loc_give']
    go_desti = request.form['destination_give']
    start_time = request.form['dep_date_give']
    end_time = request.form['arr_date_give']
    print("i'm here")
    # 돌아갈때 시간이 텀시간이있다.
    # insert_all(go_want, go_desti, start_time, end_time)
    return jsonify({'result': 'success', 'msg': '북마크를 확인하세요!'})

@app.route('/api/add_flight', methods=['GET'])
def add_flight():
    articles = list(db.mydb.find({}, {'_id': False}))
    return jsonify({'all_articles': articles})

@app.route('/api/delete_flight', methods=['POST'])
def delete_flight():

    go_want = request.form['go_want_give']
    db.flightinfo.delete_one({'go_want': go_want})

    return jsonify({'result': 'success', 'msg': '삭제 성공!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)