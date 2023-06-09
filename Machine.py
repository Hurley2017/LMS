from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import helpers
import os

load_dotenv()

engine = Flask(__name__)

#connect MongoDB
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
BORROW_RETURN = Database["BORROW/RETURN"]



#renders

@engine.route('/', methods=['GET'])
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
    response = {"status" : False, "message" : {}}
    incoming_data = request.json
    email = incoming_data["email"]
    password = helpers.MD5_HexDigest(incoming_data["password"])
    flagged_user = USER.find_one({"email":email, "password":password})
    if flagged_user == None:
        flagged_staff = STAFF.find_one({"email":email, "password":password})
        if flagged_staff == None:
            response["message"] = "Wrong Email or Password"
        else:
            if(KEYS.find_one({"avatar" : flagged_staff["email"]}) != None):
                response["message"] = {"avatar" : flagged_staff["email"], "key" : KEYS.find_one({"avatar" : flagged_staff["email"]})["key"], "role" : "ADMIN"}
            else:
                session = helpers.sessionGenerator(10)
                response["message"] = {"avatar" : flagged_staff["email"], "key" : session, "role" : "ADMIN"}
                session_package = {"avatar" : flagged_staff["email"], "key" : session, "role" : "ADMIN"}
                KEYS.insert_one(session_package)
            response["status"] = True
    else:
        if(KEYS.find_one({"avatar" : flagged_user["email"]}) != None):
            response["message"] = {"avatar" : flagged_user["email"], "key" : KEYS.find_one({"avatar" : flagged_user["email"]})["key"], "role" : "USER"}
        else:
            session = helpers.sessionGenerator(10)
            response["message"] = {"avatar" : flagged_user["email"], "key" : session, "role" : "USER"}
            session_package = {"avatar" : flagged_user["email"], "key" : session, "role" : "USER"}
            KEYS.insert_one(session_package)
        response["status"] = True
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

@engine.route('/checkSession', methods=['POST'])
def checkSession():
    response = {"status" : False, "message" : None}
    sessionData = request.json
    flag = KEYS.find_one({"avatar":sessionData["email"], "key":sessionData["key"]})
    if flag == None:
        response["message"] = "Session Invalid"
    else:
        response["status"] = True
        if flag["role"] == "ADMIN":
            response["message"] = {"role":"ADMIN", "fname": STAFF.find_one({"email" : sessionData["email"]})["fname"], "lname" : STAFF.find_one({"email" : sessionData["email"]})["lname"]}
        else:
            response["message"] = {"role":"USER", "fname": USER.find_one({"email" : sessionData["email"]})["fname"], "lname" : USER.find_one({"email" : sessionData["email"]})["lname"]}
    return response

# @engine.route('/search_res', methods=['POST'])
# def search():
#     incoming_data = request.json
#     sample_list = []
#     BOOK_res = BOOK.find({"title" : "/"+incoming_data["content"]+"/i"}, {})
#     AUTHOR_IDs = AUTHOR.find({"author_name" : "/"+incoming_data["content"]+"/i"}, {})
#     for ID in AUTHOR_IDs:
#         temp_Store = BOOK.find({"author_id" : ID["author_id"]})
#         BOOK_res = BOOK_res + temp_Store
#     for data in BOOK_res:
#         sample_list.append(data)
#     print(sample_list)
#     return " off"    

#just testing
@engine.route('/add_book', methods=['POST'])
def add_book():
    response = {"status" : False, "message" : None}
    incoming_data = request.json
    BOOK.insert_one(incoming_data)
    response["status"] = True
    response["message"] = "successfully added!"
    print("Above code is reached!")
    return response



#sending book information
@engine.route('/getBook', methods=['GET'])
def getBook():
    response = {"status" : False, "message" : None}
    book = BOOK.find({})
    if book == None:
        response["status"] = False
        response["message"] = "Book not found!"
    else:
        response["status"] = True
        # response["message"] = book
        response["message"] = {
            
        }
    return response