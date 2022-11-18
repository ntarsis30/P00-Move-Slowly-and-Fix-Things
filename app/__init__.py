from flask import *
import os 
import db_builder

app = Flask(__name__)  
app.secret_key = os.urandom(32)
@app.route('/')
def index():
    if 'username' in session:
        return redirect("/landing")
    return render_template('login.html') 

@app.route('/login', methods = ['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_builder.verify(username,password):
        session['username'] = username
        session['password'] = password
        return redirect("/landing")
    if request.form.get('submit_button') is not None:
        return render_template("create_account.html")
    response = make_response(render_template('error.html',msg = "username or password is not correct"))
    return response

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    accounts = db_builder.get_table_list("User")
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        for account in accounts:
            if account[0]==userIn:
                return f"account with username {userIn} already exists"
        db_builder.add_account(userIn,passIn)
        return render_template("signed_in.html")
    return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/landing')
def landing():
    if 'username' not in session:
        return redirect("/login")
    username = session['username']
    password = session['password']
    if db_builder.verify(username, password):
        view_pages, edit_pages = db_builder.get_user_stories(username)[0], db_builder.get_user_stories(username)[1]
        return render_template("landing.html", username = username,
        viewable_stories = view_pages, editable_stories = edit_pages)

@app.route('/view')
def view():
    if verify_session():
        storyname = request.args.get("storyName")
        storyInfo = db_builder.get_story_info(storyname)
        if storyInfo == -1:
            return render_template("error.html", msg="Story is Not in Database")
        fullText = storyInfo[0]
        contributors = storyInfo[2]
        if session['username'] in contributors.split(','):
            return render_template("story_template.html",fullText = fullText,storyname = storyname)
    return render_template("error.html", msg="session could not be verified")
@app.route('/edit')
def edit():
    if verify_session():
        storyName = request.args.get("storyName")
        storyInfo = db_builder.get_story_info(storyName)
        lastAdded = storyInfo[1]
        contributors = storyInfo[2].split(",")
        if session['username'] not in contributors:
            return render_template('edit.html', storyName = storyName, storyText = lastAdded)
        return render_template("error.html", msg= "user has already edited story")
    return render_template("error.html", msg="session could not be verified")
    
@app.route("/make_edit", methods = ['POST'])
def make_edit():
    if verify_session():
        storyName = request.form.get("storyName")
        newAddition = request.form.get("newText")
        db_builder.edit_story(storyName, newAddition, session['username'])
        return redirect("/")
    return render_template("error.html", msg = "session could not be verified")

def verify_session():
    return 'username' in session and 'password' in session and db_builder.verify(session['username'], session['password'])

@app.route('/create_story', methods=['GET', 'POST'])
def create_story():
    if verify_session():
        username = session['username']
        storyName = request.form.get('storyName')
        newText = request.form.get('newText')
        if not db_builder.used(storyName,"Story"):
            db_builder.add_story(storyName, newText, username)
            return render_template("create.html",storyName = storyName)
        return "Story Not Added"
    return render_template("error.html", message="session could not be verified")

if __name__ == "__main__":
    app.debug = True 
    print(db_builder.get_table_list("Story"))
    app.run()
