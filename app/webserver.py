from flask import Flask
import os
import socket
import uuid

app = Flask(__name__)

@app.route('/hostname')
def get_hostname():
    return socket.gethostname()

@app.route('/author')
def get_author():
    author = os.getenv('AUTHOR', 'Author not set')
    return author

@app.route('/id')
def get_id():
    id = os.getenv('UUID', 'UUID not set')
    return id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)