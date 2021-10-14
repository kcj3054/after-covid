from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.aftercovid


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/detail')
def detail():
    return render_template("detail.html")


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


# @app.route('/bookmark', methods=["GET"])
# def save_venues():
#     return jsonify({'result': 'success'})

# @app.route('/save_venues', methods=["POST"])
# def save_venues():
#
#     return jsonify({'result': 'success', 'msg': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
