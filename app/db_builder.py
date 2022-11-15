import sqlite3

stories = "(name TEXT, full TEXT, last TEXT, editors TEXT)"
users = ("(username TEXT, password TEXT)")

def data_query(table, info = None):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    if info is None:
        output = c.execute(table)
    else:
        output = c.execute(table, info)
    db.commit()
    db.close()
    return output
def create_table(name, outline):
    data_query(f"CREATE TABLE IF NOT EXISTS {name} {outline}")

create_table("Story", stories)
create_table("User", users)

def get_table_list(name):
    db = sqlite3.connect("database.db")
    c = db.cursor()
    curr = c.execute(f"SELECT * from {name}")
    output = curr.fetchall()
    db.commit()
    db.close()
    return output

def add_account(username, password):
    if not(used(username,"User")):
        data_query("INSERT INTO User VALUES (?, ?)", (username, password))
    return -1


def verify(username, password):
    accounts = get_table_list("User")
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

def used(name,table):
    arr = get_table_list(table)
    for i in arr:
        if i[0] == name:
            return True
    return False

def add_story(name, text, editor):
    if not(used(name,"Story")):
        data_query("INSERT INTO Story VALUES (?, ?, ?, ?)", (name, text, text, editor))
    return -1

def get_story_info(name):
    story_info = get_table_list("Story")
    for row in story_info:
        if row[0] == name:
            return row[1:]
    return -1
    
def get_story_contents(storyName):
    storyInfo = get_table_list("Story")
    for row in story_info:
        if row[0] == storyName:
            return row[1]
    return -1
            
def edit_story(name, text, editor):
    if used(name,"Story"):
        story_info = get_story_info(name)
        old_text = story_info[0] + text 
        editors = editor + "," + story_info[2] 
        data_query(f'''UPDATE Story SET full = ?, last = ?, editors = ? WHERE name = ? ''', (old_text, text, editors, name))
    else:
        return -1
def get_user_stories(username):
    view_stories,edit_stories = [],[]
    stories = get_table_list("Story")
    for story in stories:
        editors = story[3].split(",")
        if username in editors:
            view_stories.append(story[0])
        else:
            edit_stories.append(story[0])
    return view_stories, edit_stories
