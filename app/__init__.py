#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#P00 -- Move Slowly and Fix Things
#2022-11-15
#time spent:
from flask import *
import os
import sqlite3
import db_builder

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/')
def index():
    if 'username' in session:
        return redirect("/home")
    return render_template('login.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_builder.verify(username,password):
        session['username'] = username
        session['password'] = password
        return redirect("/home")
    if request.form.get('submit_button') != None:
        return render_template("create_account.html")
    response = make_response(render_template('error.html',message = "credentials are not correct"))
    return response

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        user_info = request.form.get('username')
        pass_info = request.form.get('password') 
        if db_builder.account_used(user_info):
            return "account with this username already exists"
        else:
            return render_template("signed_in.html")
    return redirect(url_for('index'))
    

"""
@app.route('/landing', methods=['GET', 'POST'])
def landing_page():
    db = sqlite3.connect("database.db")
    cur = db.cursor()
    print("DIAG Tables")
    print(cur.execute("SELECT name FROM sqlite_master").fetchall())
    edited = cur.execute("SELECT * from edited_stories").fetchall()
    print(edited)
    db.close()
    return render_template('landing.html', edited = edited)
"""

if __name__ == '__main__':
    app.debug = True
    app.run()
