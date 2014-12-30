from flask import Flask, request, jsonify
from flask import render_template
from twilio.rest import TwilioRestClient


app = Flask(__name__)

@app.route('/') 
def index():
    return 'Index!'

def sendsms():
    account_sid = "AC2503925359b3b37abbeaaff6d87621f9"
    auth_token = "44363a15bca971ddba81edd23cd56ee9"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+19736504192", from_="+18622775096", body="twofass")


#this initializes the 2 factor process once company validates 1st auth 
@app.route('/init', methods=['POST', 'GET'])
def template():
    #need to get phone number and Company token and userID
    #phone number, company token will be received as json
    #parses the json and sends to database and user's phone
    json = request.json
    print(json)

    
    #sendsms()
    #sendToDB()
    #display 2nd fact input page

    return jsonify(json)


@app.route('/admin')
def admin():
    return 'Admin'

@app.route('/firstlogInDone')
def auth():
    #gets phone number, and the auth token set my sys admin and sends code to user. 
    #write the user code, phone number, and user id to db 
    return 'Authorize'

@app.route('/validate')
def val():
    #gets the user id, phone number, and code and compares that to db
    return 'Validate'

@app.route('/login')
def log_in():
    return app.send_static_file('login.html')

@app.route('/two_factor')
def two_factor():
    return app.send_static_file('twofac.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
