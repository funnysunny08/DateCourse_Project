from flask import Flask, render_template, jsonify, request
from data_crawl import data_crawl, data_crawl_recommend

app = Flask(__name__)


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/showPlace')
def search():
    where = request.args.get("where")
    what = request.args.get("what")
    return render_template('showPlace.html', where=where, what=what)


# API 역할을 하는 부분


@app.route('/api/recommend', methods=['GET'])
def show_recommend():
    data = data_crawl_recommend()
    return jsonify({'result': 'success', 'recommend_list': data})



@app.route('/api/showPlace', methods=['GET'])
def show_Place():
    keyword = request.args.get("keyword")
    data = data_crawl(keyword)
    return jsonify({'result': 'success', 'place_list': data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
