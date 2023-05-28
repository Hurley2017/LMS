from flask import Flask, render_template

engine = Flask(__name__)

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


