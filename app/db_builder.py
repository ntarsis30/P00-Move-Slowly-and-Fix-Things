#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#P00 -- Move Slowly and Fix Things
#2022-11-15
#time spent:
from flask import Flask,session,request, redirect, url_for,render_template
import sqlite3
import os

db = sqlite3.connect("database.db")
c = db.cursor()

if not """('logins',)""" in str((c.execute("SELECT name FROM sqlite_master")).fetchall()):
    print("g")
    c.execute("CREATE TABLE logins(username TEXT, password TEXT)")
if not """('edited_stories',)""" in str((c.execute("SELECT name FROM sqlite_master")).fetchall()):
    print("ge")
    c.execute("CREATE TABLE edited_stories(title TEXT, story TEXT)")
if not """('all_stories',)""" in str((c.execute("SELECT name FROM sqlite_master")).fetchall()):
    print("ga")
    c.execute("CREATE TABLE all_stories(username TEXT, story TEXT, newest TEXT)")
#c.execute("""INSERT INTO edited_stories VALUES("test title", "Test storyTest storyTest storyTest storyTest storyTest storyTest storyTest storyTest storyTest story") """)
#c.execute("DELETE FROM edited_stories")
print((c.execute("SELECT name FROM sqlite_master")).fetchall())
db.commit()
db.close()
