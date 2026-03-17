from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    # Intentional vulnerability: No input sanitization (demonstration only)
    name = request.args.get("name", "World")
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Security note: Use of debug=True is not recommended for production
    app.run(host="0.0.0.0", port=5000, debug=True)
