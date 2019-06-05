# -*- coding: utf-8 -*-#
"""
 FileName:     run
 Author:       jynnezhang
 Date:         2019/6/5
 Description:  
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'


if __name__ == '__main__':
    # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
    app.run(debug=True)
