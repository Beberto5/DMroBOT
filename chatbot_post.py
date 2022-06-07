@app.route('/webhook/twitter',methods=['POST'])
def respond_with_facts():
    if validateRequest(request):
        #Do whatever you like here!
        req=request.get_json()
        cat_regex=re.compile(r'[Ss][Ee][Nn][Dd] [Mm][Ee] [Cc][Aa][Tt] [Ff][Aa][Cc][Tt][Ss]')
        send_cats=False
        user_id = ''

        if 'direct_message_events' in req.keys():
            msg_txt = str(req['direct_message_events'][0]['message_create']['message_data']['text'])
            user_id = str(req['direct_message_events'][0]['message_create']['sender_id'])
            send_cats = cat_regex.search(msg_txt)

        if user_id != 'YOUR-PERSONAL-USER-ID' and send_cats:
            api.send_direct_message(user_id,catfacts.retrieveCatfact()+" Nya~")




    else:
        res = {'message':"Unauthorized Access"}
        return Response(res,status=401)
        
    return {'status_code':200}

def validateRequest(request):
    req_headers = request.headers
    if req_headers.has_key('x-twitter-webhooks-signature'):

        twitter_signature = req_headers['x-twitter-webhooks-signature'] 
        
        consumer_secret_bytes = bytes(CONSUMER_SECRET,'utf-8') 
        payload_body = bytes(request.get_data(as_text=True),'utf-8')

        sha_256_digest = hmac.new(consumer_secret_bytes, payload_body , digestmod=hashlib.sha256).digest()

        consumer_payload_hash = "sha256="+base64.b64encode(sha_256_digest).decode('utf-8')

        if hmac.compare_digest(consumer_payload_hash,twitter_signature):
            return True
        else:
            return False