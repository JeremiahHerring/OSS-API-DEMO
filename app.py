from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data storage
posts = []

# Helper function to find a post by ID
def find_post(post_id):
    return next((post for post in posts if post["id"] == post_id), None)

# GET all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

# GET a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = find_post(post_id)
    if post:
        return jsonify(post), 200
    abort(404, description="Post not found")

# POST a new post
@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or 'title' not in request.json or 'content' not in request.json:
        abort(400, description="Title and Content are required")
    new_id = posts[-1]['id'] + 1 if posts else 1
    post = {
        "id": new_id,
        "title": request.json['title'],
        "content": request.json['content']
    }
    posts.append(post)
    return jsonify(post), 201

# PUT to update a post by ID
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = find_post(post_id)
    if not post:
        abort(404, description="Post not found")
    if not request.json:
        abort(400, description="Request must be JSON")
    post['title'] = request.json.get('title', post['title'])
    post['content'] = request.json.get('content', post['content'])
    return jsonify(post), 200

# DELETE a post by ID
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = find_post(post_id)
    if not post:
        abort(404, description="Post not found")
    posts.remove(post)
    return jsonify({"message": "Post deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
