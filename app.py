from flask import Flask, send_from_directory
import os

app = Flask(__name__)
BUILD_PATH = 'C:\\Projects\\creativ3lab_hosting'

@app.route('/')
def serve_index():
    """
    Serves the index.html file from the specified build directory.

    Returns:
        Response: The response object containing the index.html file.
    """
    return send_from_directory(BUILD_PATH, 'index.html')


@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(BUILD_PATH, path)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
