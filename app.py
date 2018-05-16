import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis('redis')
hostname = os.environ.get('HOSTNAME')

@app.route("/")
def index():
    return '%s %d' % (hostname, redis.incr('counter'))

app.run(host='0.0.0.0', port='80')

