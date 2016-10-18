from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
	#return redirect('https://www.ft.com')
	#response = make_response('<h1> This document carries a cookie! </h1>')
	#response.set_cookie('answer','42')
	#return response
	#user_agent = request.headers.get('User-Agent')
	#return '<p> Your Browser is %s </p>' % user_agent

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name = name)

if __name__ == "__main__":
	app.run()