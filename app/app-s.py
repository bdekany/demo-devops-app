import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    db_version = 1
    visit = 1
    return render_template("homepage.html", db_version=db_version, visit=visit)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9000))
    app.run(host='0.0.0.0', port=port)
