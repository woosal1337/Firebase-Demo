import pyrebase
from credentials import credentials

firebase = pyrebase.initialize_app(credentials())
db = firebase.database()

all_agents = db.child("").get().val()
print(all_agents)
