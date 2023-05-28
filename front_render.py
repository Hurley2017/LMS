from flask import Flask, render_template

engine = Flask(__name__)


@engine.route('/', methods=['GET'])
def say_ello():
    return "Working"

@engine.route('/login', methods=['GET'])
def login():
    return render_template('log-in.html')

@engine.route('/logout', methods=['GET'])
def logout():
    return render_template('log-out.html')

@engine.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    engine.run(debug=True)