import os
import redis
import json

from flask import Flask, render_template

app = Flask(__name__)

if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
    redis_host = services['user-provided'][0]['credentials']['host']
    redis_port = services['user-provided'][0]['credentials']['port']
else:
    redis_host = 'redis'
    redis_port = 6379

@app.route('/')
def homepage():
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
    db_version = r.get('db_version')
    visit = r.incr('visit')
    return render_template("homepage.html", db_version=db_version, visit=visit)

if __name__ == '__main__':
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
    r.set('db_version', '1.0')
    port = int(os.environ.get('PORT', 9000))
    app.run(host='0.0.0.0', port=port)
