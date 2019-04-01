#-*- coding=utf-8 -*-

from flask import Flask,flash,render_template,url_for,request,redirect, flash,get_flashed_messages
from flask_bootstrap import Bootstrap
import os
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '123223a'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username =='king7' and password =='*******':
            return redirect('*******')
        else:
            return 'username or password error!'
    else:
        return render_template('login.html')
    return render_template('login.html')

@app.route('/*********',methods=['GET','POST'])
def myshell():
    if request.method == 'POST':
        cmd = request.form['cmd']
        if len(cmd)>12:
            flash(u"长度限制为12")
        else:
            cmdcontent = os.popen(cmd).read()
            return render_template('admin.html',cmdcontent=cmdcontent)


    else:
        return render_template('admin.html')
    return render_template('admin.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
