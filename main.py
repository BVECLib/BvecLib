from flask import Flask, flash, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from access import up, folder
import os
from functools import wraps
from datetime import timedelta

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
   return render_template('index.html')


def login_required(f):
   @wraps(f)
   def wrap(*args, **kwargs):
      if "logged_in" in session:
         return f(*args, **kwargs)
      else:
         flash("You need to log in to access this page.")
         return redirect(url_for('login'))
   return wrap


@app.route('/admin', methods = ['GET', 'POST'])
@login_required
def admin():
   fid = 'root'
   if request.method == 'POST':
      fid = request.form.get('folder')
      print(fid)
   return render_template('admin.html', folder=folder(fid))


@app.route('/login', methods=['GET', 'POST'])
def login():
   error = None
   if "logged_in" in session:
         return redirect(url_for('admin'))
   if request.method == 'POST':
         if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = "Invalid  Credentials. Please try again !"
         else:
            session.permanent = True
            session['logged_in'] = 'aditya'
            app.permanent_session_lifetime = timedelta(minutes=1440)
            return redirect(url_for('admin'))
   return render_template('login.html', error=error)


@app.route('/drop', methods = ['GET',  'POST'])
def drop():
	if request.method == 'POST':
		fid = request.form.get('folder')
	return render_template('drop.html', folder=folder(fid))


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      fid = request.form.get('folder')
      filename = secure_filename(f.filename)
      f.save(filename)
      print(fid)
      up(filename, fid)
      flash('File successfully uploaded')
      return redirect(url_for('admin'))
   if request.method == 'GET':
   	return "Method not supported"


@app.route('/sem/<sub>', methods = ['GET', 'POST'])
def subjects(sub):
   return render_template('subject.html', subject=sub)

   
if __name__ == "__main__":
   app.run(debug=True)