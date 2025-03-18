from flask import Flask, jsonify, request
from flask_cors import CORS
import instaloader

app = Flask(__name__)
CORS(app)

loader = instaloader.Instaloader()

def get_instagram_image(post_url):
    try:
        shortcode = post_url.split('/')[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        return {"image_url": post.url}
    except Exception as e:
        return {"error": str(e)}

@app.route('/get_image', methods=['POST'])
def fetch_image():
    data = request.get_json()
    post_url = data.get("post_url")
    if not post_url:
        return jsonify({"error": "No post URL provided"}), 400
    return jsonify(get_instagram_image(post_url))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
