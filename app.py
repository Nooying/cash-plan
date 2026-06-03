from flask import Flask, send_file
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 8080))

@app.route('/')
def index():
    return send_file('budget-system.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)
