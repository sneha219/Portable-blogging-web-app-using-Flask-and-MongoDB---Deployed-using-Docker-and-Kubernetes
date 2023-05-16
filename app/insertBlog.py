from pymongo import MongoClient

# Set up a connection to the local MongoDB instance
client = MongoClient('mongodb://localhost:27017/')

# Select the blog database and the posts collection
db = client.blog
collection = db.posts

# Create a new post document to insert into the collection
post = {
    "title": "My first blog post",
    "author": "John Doe"
}

# Insert the post document into the collection
result = collection.insert_one(post)

# Print the ID of the inserted document
print(f"Inserted post with ID {result.inserted_id}")
