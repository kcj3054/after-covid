from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from datetime import datetime, timedelta
import jwt
import hashlib
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('3.36.69.62', 27017, username="test", password="test")
db = client.aftercovid


@app.route('/')
def load():
    # return render_template("index.html")
    return render_template("login.html")

@app.route('/main')
def main():
    # return render_template("index.html")
    return render_template("index.html")


@app.route('/detail')
def detail():
    return render_template("test.html")


@app.route('/bookmark')
def bookmark():
    return render_template("bookmark.html")


@app.route('/diary')
def diary():
    return render_template("diary.html")


@app.route('/show_diary', methods=['GET'])
def show_diary():
    diaries = list(db.diary.find({}, {'_id': False}))
    return jsonify({'all_diary': diaries})


@app.route('/save_diary', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    mytime2 = today.strftime('%Y-%m-%d')

    filename = f'file-{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'title': title_receive,
        'content': content_receive,
        'file': f'{filename}.{extension}',
        'time': mytime2
    }

    db.diary.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('index.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash,
        "profile_name": username_receive,
        "profile_pic": "",
        "profile_pic_real": "profile_pics/profile_placeholder.png",
        "profile_info": ""
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    # print(value_receive, type_receive, exists)
    return jsonify({'result': 'success', 'exists': exists})

# @app.route('/search_venues', methods=["POST"])
# def search_venues():
#     venue_receive = request.form['venue_give']
#
#     doc = {
#         'venue': venue_receive
#     }
#
#     db.pac_input.insert_one(doc)
#
#     return jsonify({'msg': 'POST 연결되었습니다!'})
#
# @app.route('/get_venues', methods=["GET"])
# def get_venues():
#     pac_input = list(db.pac_input.find({}, {'_id': False}))
#     db.pac_input.drop()
#     return jsonify({'pac_input': pac_input})

@app.route('/save_venues', methods=["POST"])
def save_venues():
    url_receive = request.form['url_give']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    description = soup.select_one('meta[property="og:description"]')['content']
    doc = {
        'title': title,
        'image': image,
        'description': description,
        'url': url_receive
    }

    db.bookmark.insert_one(doc)

    return jsonify({'msg': 'POST 연결되었습니다!'})

@app.route('/post_venues', methods=["GET"])
def post_venues():
    venues = list(db.bookmark.find({}, {'_id': False}))
    return jsonify({'all_venues': venues})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)