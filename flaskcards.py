from flask import Flask
app = Flask(__name__)
    python helpers.py 
@app.route("/")
def login_or_redirect():
    
    pass

@app.route("/sets-home")
def sets_home():
    pass

@app.route("/settings")
def show_settings():
    pass

@app.route("/set/<int:setid>")
def show_set(setid):
    return getCards(setid);

@app.route("/set/<int:setid>/edit")
def edit_set(setid):
    modifySet(setid,%s);
    pass


