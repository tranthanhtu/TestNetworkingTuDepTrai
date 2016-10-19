import json
from flask import Flask, request

app = Flask(__name__)

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
    return json.dumps(posts)

@app.route('/addpost', methods=["POST"])
def add_post():
    args = request.form
    title = args["title"]
    content = args["content"]
    new_post = {
        "title" : title,
        "content" : content
    }
    posts.append(new_post)
    print(title, content)
    return "OK"


if __name__ == '__main__':
    app.run()
