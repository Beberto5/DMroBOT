from flask import Flask, request, Response, jsonify
from decouple import config
import base64
import hashlib
import hmac 
import json

app=Flask(__name__)

CONSUMER_KEY=config('consumer_key')
CONSUMER_SECRET=config('consumer_secret')
ACCESS_TOKEN=config('access_token')
ACCESS_TOKEN_SECRET=config('access_token_secret')

@app.route('/webhook/twitter', methods=['GET'])
def webhook_challenge():
    consumer_secret_bytes = bytes(CONSUMER_SECRET,'utf-8') 
    message = bytes(request.args.get('crc_token'),'utf-8')

    sha256_hash_digest = hmac.new(consumer_secret_bytes, message, 
        digestmod=hashlib.sha256).digest()
    response={
        'response_token':'sha256='+base64.b64encode(sha256_hash_digest).decode('utf-8')
    }

    return json.dumps(response)

@app.route('/')
def index():
    return f"<h3>Welcome to Cat Facts!</h3>"

if __name__=='__main__':
    print('parto')
    app.run(port=5000)
    print('finisco')