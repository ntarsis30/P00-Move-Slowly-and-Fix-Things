#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#P00 -- Move Slowly and Fix Things
#2022-11-15
#time spent: 
from flask import Flask,session,request, redirect, url_for,render_template
import os

# Set the secret key to some random bytes. Keep this really secret!
app = Flask(__name__)
app.secret_key = os.urandom(32)


if __name__ == '__main__':
    app.debug = True
    app.run()
