from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import helpers
import os

load_dotenv()

engine = Flask(__name__)

#connect Mongo

Cluster_Pointer = MongoClient(os.environ.get('CONNECTION_URL'))
SESSION = Cluster_Pointer["SESSION"]
KEYS = SESSION["KEYS"]
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
    response = {"status" : False, "message" : None}
    incoming_data = request.json
    email = incoming_data["email"]
    password = helpers.MD5_HexDigest(incoming_data["password"])
    flagged_user = USER.find_one({"email":email, "password":password})
    if flagged_user == None:
        flagged_staff = STAFF.find_one({"email":email, "password":password})
        if flagged_staff == None:
            response["message"] = "Wrong Email or Password"
        else:
            del flagged_staff["password"]
            session = helpers.sessionGenerator(10)
            session_package = {"avatar" : flagged_staff["email"], "key" : session}
            flagged_staff["_id"] = "ADMIN"
            response["status"] = True
            response["message"] = session_package
            KEYS.insert_one(session_package)
    else:
        del flagged_user["password"]
        session = helpers.sessionGenerator(10)
        session_package = {"avatar" : flagged_user["email"], "key" : session}
        flagged_user["_id"] = "USER"
        response["status"] = True
        response["message"] = session_package
        KEYS.insert_one(session_package)
    return response


@engine.route('/send_reginfo', methods=['POST'])
def reg_info():
    response = {"status" : False, "message" : None}
    incoming_data = request.json
    search_user = USER.find_one({"email" : incoming_data["email"]})
    if search_user == None:
        if incoming_data["password"] != incoming_data["password2"]:
            response["status"] = False
            response["message"] = "Passwords do not match!"
        else:
            del incoming_data["password2"]
            incoming_data["password"] = helpers.MD5_HexDigest(incoming_data["password"])
            USER.insert_one(incoming_data)
            response["status"] = True
            response["message"] = "Successfully Registered!"
    else:
        response["status"] = False
        response["message"] = "Email id is already associated with an account."
    return response

