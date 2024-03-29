import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("testgenai-3783-firebase-adminsdk-kabq0-9841d2578b.json")
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Define a reference to a collection
users_ref = db.collection("users")

# Add data to the collection
doc_ref = users_ref.document("user1")
doc_ref.set({
    "name": "GenAI",
    "player": "Winner",
    "userID": 38833
})

# Read data from the collection
docs = users_ref.get()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
