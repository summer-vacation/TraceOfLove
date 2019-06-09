# -*- coding: utf-8 -*-#
"""
 FileName:     run
 Author:       jynnezhang
 Date:         2019/6/5
 Description:  
"""

from flask import Flask, render_template
from flask_cors import CORS
#处理跨域请求

app = Flask(__name__, static_folder = "../dist/static", template_folder = "../dist")

CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
	return 'test ok!'


if __name__ == '__main__':
    # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
    app.run('127.0.0.1',port=5001,debug=True)
