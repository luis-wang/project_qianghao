#coding=utf-8
#!/usr/bin/python
'''
Created on May 27, 2013

@author: root
'''
from flask import Flask,make_response,request
from flask import render_template
from flask import abort, redirect, url_for

app = Flask(__name__)




#@app.route("/hello")
#def hello():
#    return "Hello World!878755"



@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello1(name=None):
    username = request.cookies.get('username')
    # 使用 cookies.get(key) 来代替 cookies[key] ，
    # 以避免当 cookie 不存在时引发 KeyError 。
    print 'hello cookie username = ',username
    
    resp = make_response(render_template('hello.html', name=name))
    resp.set_cookie('username', 'the username is wangxudong')
    return resp
    
    
    #return render_template('hello.html', name=name)

@app.route('/test')
def test():
    username = request.cookies.get('username')
    resp = 'test cookie username = ' + username
    return redirect(url_for('hello1'))
    #return resp

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.route('/user/<username>')
def show_user_profile(username='default name'):
    # show the user profile for that user
    return 'username is :'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    abort(401)
    error = None
    if request.method == 'POST':
        #要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性:
        #searchword = request.args.get('q', '')
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 如果请求访求是 GET 或验证未通过就会执行这里的代码

from werkzeug import secure_filename
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/root/Desktop/test/' + secure_filename(f.filename))
        
    return 'save success'






@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8081)
    #app.run()
    
    
    
    
    
    
    
    
    
    
    
    