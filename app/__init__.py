#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#P00 -- Move Slowly and Fix Things
#2022-11-15
#time spent:
from flask import Flask,session,request, redirect, url_for,render_template
import os
import sqlite3

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = os.urandom(32)

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

if __name__ == '__main__':
    app.debug = True
    app.run()
