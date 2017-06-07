#enconfig:utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import models

app = Flask(__name__)
app.secret_key='\x00$\xe496\n8\x82\x93)` \x9ep\x82j\xd9`\x16,\x1cL\xe7\xd5J:H\xb1\x12\x85\xd9\xc9'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods = ['post','get'])
def login():
    rt = request.form if request.method == 'POST' else request.args
    username = rt.get('username', '')
    password = rt.get('password', '')
    rt_cnt=models.login_check((username, password))
    if rt_cnt:
        session['user'] = username
        return redirect('/user/')
    else:
        return render_template('index.html', username=username, password=password)

@app.route('/user/')
def user():
    if session.get('user') is None:
        return redirect('/')
    rt_list = models.get_users()
    return render_template('user.html', users=rt_list)

@app.route('/user/add/')
def user_add():
    if session.get('user') is None:
        return redirect('/')
    return render_template("user_add.html")

@app.route('/user/add/save/',methods=['post'])
def user_add_save():
    if session.get('user') is None:
        return redirect('/')
    username=request.form.get('username', '')
    password=request.form.get('password', '')
    age=request.form.get('age', '')
    models.add_user_save((username,password,age))
    return redirect('/user/')

@app.route('/user/delete/')
def user_delete():
    if session.get('user') is None:
        return redirect('/')
    id=request.args.get('id', '')
    models.del_user((id,))
    return redirect('/user')


@app.route('/user/views/')
def user_views():
    if session.get('user') is None:
        return redirect('/')
    id = request.args.get('id', '')
    rt_list=models.modify_user_info((id,))
    username = rt_list[0][0]
    age = rt_list[0][1]
    return render_template('user_modify.html', id=id, username=username, age=age)


@app.route('/user/modify/', methods=['post'])
def user_modify():
    if session.get('user') is None:
        return redirect('/')
    id=request.form.get('id', '')
    username=request.form.get('username', '')
    age=request.form.get('age', '')
    models.modify_user_save((username, age, id))
    return redirect('/user/')


@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)


