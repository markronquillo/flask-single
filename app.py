from flask import Flask
from flask import make_response, redirect, abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
  return '<h1> Hello World </h1>'

@app.route('/user/<name>')
def user(name):
  return '<h1>Hello, %s!</h1>' % name

@app.route('/mresponse')
def mresponse():
  response = make_response('<h1> This document carries a cookie!</h1>')
  response.set_cookie('answer', '42')
  return response

@app.route('/redirect')
def redir():
  return redirect('http://www.google.com')

@app.route('/user_id/<id>')
def get_id(id):
  user = 3
  if user != id:
    abort(404)
  return '<h1> Hello, %s</h1>' % id

if __name__ == '__main__':
  # app.run(debug=True)
  manager.run()



