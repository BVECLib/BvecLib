from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from access import up, folder
import os

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/admin', methods = ['GET', 'POST'])
def upload():
	fid = 'root'
	if request.method == 'POST':
		fid = request.form.get('folder')
		print(fid)
	return render_template('upload.html', folder=folder(fid))

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
      os.remove(filename)
      flash('File successfully uploaded')
      return redirect(url_for('upload'))
   if request.method == 'GET':
   	return "Method not supported"