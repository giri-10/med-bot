
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

# Twilio credentials
account_sid = 'ACa7f4088feb42730d6b80296918fef3b1'
auth_token = '2d72fb403ef8f13d42334c6ee4e542a2'
twilio_number = '+18012069828'

# Create a Twilio client
client = Client(account_sid, auth_token)


msg = client.messages.create(
              # body=response_meissage,
              from_=twilio_number,
              # to=request.form['From'],
              # messaging_service_sid='MG4998ae0067015d28c28024d171410104',
              body='Hello there!',      
              to='+918073152546'
)

# @app.route('/sms', methods=['GET','POST'])
# def sms_reply():
#         resp = MessagingResponse()
#         resp.message("wait till i diagnose your symptoms")
#         return str(resp)

@app.route('/sms', methods=['POST'])
def sms_reply():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Wait ".format(body))

    return str(resp)


# def process_message(message):
#     # Add your logic to process the incoming message and generate a response
#     # For example, you can use if-else statements or machine learning models
    
#     # Return a sample response for now

#               if message == "Hello":
#                                           return "Hi, this is med bot. How can I help you?"
#               elif message == "I have a headache":
#                                           return "Do you have any other symptoms?"
              

#               return "Thank you for your message!"

if __name__ == '__main__':
    app.run(debug= True)
