from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

engine = Flask(__name__)

#connect Mongo

Cluster_Pointer = MongoClient(os.environ.get('CONNECTION_URL'))

Database = Cluster_Pointer['LMS']
AUTHOR = Database["AUTHOR"]
BOOK = Database["BOOK"]
BOOK_COVER = Database["BOOK_COVER"]
CATEGORY = Database["CATEGORY"]
PUBLISHER = Database["PUBLISHER"]
STAFF = Database["STAFF"]
USER = Database["USER"]



#renders
@engine.route('/', methods=['GET'])
def say_ello():
    return "Working"

@engine.route('/login', methods=['GET'])
def login():
    return render_template('log-in.html')

@engine.route('/register', methods=['GET'])
def logout():
    return render_template('register.html')

@engine.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@engine.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@engine.route('/add', methods=['GET'])
def add():
    return render_template('add_book.html')

@engine.route('/edit', methods=['GET'])
def edit():
    return render_template('edit_book.html')



#services

@engine.route('/send_loginfo', methods=['POST'])
def log_info():
    return "Help"
