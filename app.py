from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    print("🚀 CS 2 Market sayti ishga tushdi: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)