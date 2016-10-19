import json
from flask import *
from mongoengine import *
from mlab import *

app = Flask(__name__)


class Post(Document):
   title = StringField()
   content = StringField()
   def get_json(self):
       return {"title": self.title, 'content': self.content}


post1 = {
    "title" : "Good day",
    "content" : "I met a girl"
}

post2 = {
    "title" : "Bad day",
    "content" : "Today , she did show up and I felt more lonely than ever"
}



posts = [post1,post2]

print(post1["title"])

@app.route('/')
def main():
   posts = Post.objects
   return jsonify([post.get_json() for post in posts])

@app.route('/addpost', methods=["POST"])
def add_post():
    args = request.form
    title = args["title"]
    content = args["content"]
    p = Post(title = title, content = content)
    p.save()
    return jsonify({"code": 1, "message": "OK"})

    new_post = {
        "title" : title,
        "content" : content
    }
    posts.append(new_post)
    print(title, content)
    return "OK"


if __name__ == '__main__':
    mlab_connect()
    app.run()
