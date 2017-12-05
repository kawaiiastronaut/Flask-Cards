from flask import Flask
app = Flask(__name__)
    python helpers.py 
@app.route("/")
def login_or_redirect():
    test();
    pass

@app.route("/sets-home")
def sets_home():
    user = input('Enter userId: ');
    return getSets(user);
    

@app.route("/settings")
def show_settings():
    
    pass

@app.route("/set/<int:setid>")
def show_set(setid):
    return getCards(setid);

@app.route("/set/<int:setid>/edit")
def edit_set(setid):
    name = input('Enter new set name: ');
    modifySet(setid,name);
    pass


