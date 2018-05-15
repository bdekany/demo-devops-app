import os
import redis

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    db_version = r.get('db_version')
    visit = r.incr('visit')
    return render_template("homepage.html", db_version=db_version, visit=visit)

if __name__ == '__main__':
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    r.set('db_version', '1.0')
    port = int(os.environ.get('PORT', 9000))
    app.run(host='0.0.0.0', port=port)
