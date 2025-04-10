from flask import flask, request, redirect, url_for, render_template
from storage_json import Storage

app = flask(__name__)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
