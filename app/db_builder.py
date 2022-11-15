#Flying Turtles | Anson Wong, Nicholas Tarsis
#SoftDev
#P00 -- Move Slowly and Fix Things
#2022-11-15
#time spent:
from flask import *
import sqlite3
import os

db = sqlite3.connect("database.db")
c = db.cursor()
stories = "(title TEXT, story TEXT, last TEXT, editors TEXT)"
users = ("(username TEXT, password TEXT)")

def data_query(table, info = None):
    db = sqlite3.connect("database.db", check_same_thread=False)
    c = db.cursor()
    if info == None:
        output = c.execute(table)
    else:
        output = c.execute(table, extra)
    db.commit()
    db.close()
    return output
def make_table(name, outline):
    data_query(f"CREATE TABLE IF NOT EXISTS {name} {outline}")

make_table("Story", stories)
make_table("User", users)

def get_table_list(name):
    db = sqlite3.connect("database.db", check_same_thread=False)
    c = db.cursor()
    curr = c.execute(f"SELECT * from {name}")
    out = curr.fetchall()
    db.commit()
    db.close()
    return out

def verify(username, password):
    accounts = get_table_list("User")
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

def account_used(username):
    accounts = get_table_list("User")
    for account in accounts:
        if account[0] == username:
            return True
    return False

def add_account(username, password):
    if not(account_exists(username)):
        query("INSERT INTO User VALUES (?, ?)", (username, password))
    else:
        return -1



#if not """('logins',)""" in str((c.execute("SELECT name FROM sqlite_master")).fetchall()):
#    print("g")
#    c.execute("CREATE TABLE logins(username TEXT, password TEXT)")
#if not """('edited_stories',)""" in str((c.execute("SELECT name FROM sqlite_master")).fetchall()):
#    print("ge")
#    c.execute("CREATE TABLE edited_stories(title TEXT, story TEXT)")
#if not """('all_stories',)""" in str((c.execute("SELECT name FROM sqlite_master")).fetchall()):
#    print("ga")
#    c.execute("CREATE TABLE all_stories(username TEXT, story TEXT, newest TEXT)")
#c.execute("""INSERT INTO edited_stories VALUES("test title", "Test story") """)
#c.execute("DELETE FROM edited_stories")
#print((c.execute("SELECT name FROM sqlite_master")).fetchall())

db.commit()
db.close()
