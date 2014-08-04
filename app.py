from flask import Flask, render_template
from flask import make_response, redirect, abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
boostrap = Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)

@app.route('/debug')
def debug():
  nums = range(10)
  return render_template('debug.html', nums=nums)

@app.route('/extends')
def extends():
  return render_template('extends.html')

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


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500

if __name__ == '__main__':
  app.run(debug=True)
  # manager.run()



