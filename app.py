from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello World!",
        "status": "running",
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "uptime": "ok"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)