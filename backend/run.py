# -*- coding: utf-8 -*-#
"""
 FileName:     run
 Author:       jynnezhang
 Date:         2019/6/5
 Description:  
"""

from flask import Flask, render_template, jsonify
from flask_cors import CORS
#处理跨域请求
from random import randint

app = Flask(__name__, static_folder = "../dist/static", template_folder = "../dist")

CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	#if app.debug:
	#	return requests.get('http://localhost:5001/{}'.format(path)).text
	return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
	return 'test ok!'

@app.route('/api/random')
def random_number():
	response = {
		'randomNumber': randint(1,100)
	}
	return jsonify(response)

if __name__ == '__main__':
    # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
    app.run('127.0.0.1',port=5001,debug=True)
