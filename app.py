from flask import Flask, render_template, jsonify, request
from data_crawl import data_crawl, data_crawl_recommend

app = Flask(__name__)


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/showPlace')
def search():
    return render_template('showPlace.html')


# API 역할을 하는 부분


@app.route('/api/recommend', methods=['GET'])
def show_recommend():
    data = data_crawl_recommend()
    return jsonify({'result': 'success', 'recommend_list': data})


@app.route('/api/userWant', methods=['POST'])
def api_register():
    where_receive = request.form['where_give']
    what_receive = request.form['what_give']
    keyword = where_receive + " " + what_receive

    return jsonify({'result': 'success', 'msg': '검색'})

@app.route('/api/showPlace', methods=['GET'])
def show_Place():

    data = data_crawl(keyword)
    return jsonify({'result': 'success', 'recommend_list': data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
