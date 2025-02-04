from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')  # Set this in your environment
PAGE_ACCESS_TOKEN = "EAAZAyg37sE4ABOxqp2R1BK7KRqJLeNRgpQMJKEbG3vvdJ9vZBDjngYALUZAGhD9Op3ZCFYQyrFr0J7NoP1OaPmS1BhJ56YpWQ1z4A3h4z4STLiX1cUJwZBUJK8JN4vkq4838Ej2aMgHwEoBZAnvxTWOyEPBFGcqh9OUZASu1YLjJ4yoAkPyWoVCP3o9Sx6iTXiKB5oXz18zkfeZAgi9nQ8q1ZBUDMESZA8c4KpwALhZCuMWC4MMZAZAaUrHAZD"  # Set this in your environment

# print(f'VERIFY_TOKEN:{VERIFY_TOKEN}')
# print(f'PAGE_ACCESS_TOKEN:{PAGE_ACCESS_TOKEN}')

@app.route("/", methods=['GET'])
def webhook_verification():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode and token == VERIFY_TOKEN:
        print('Webhook verified!')
        return jsonify({"status": "success", "challenge": challenge}), 200
    else:
        print('Attempt to verify webhook failed!')
        return jsonify({"status": "error", "message": "Verification failed"}), 403  # Forbidden

@app.route('/', methods=['POST'])
def webhook():
    print('Post Request was made')
    data = request.json
    print("Received data: %s", data)  # Log the incoming data

    # Navigate through the nested structure to access 'messages'
    if 'entry' in data and len(data['entry']) > 0:
        changes = data['entry'][0]['changes']
        if len(changes) > 0:
            messages = changes[0]['value'].get('messages', [])
            if messages:
                sender = messages[0]['from']  # Extract the sender's number
                message_text = messages[0]['text']['body']  # Extract the message text
                # Check if the message is "hi"
                if message_text.lower() == "hi":
                    response_message = f"Hello {sender}, Welcome to 2boxMediahouse shop manager. Would you like to setup shop or login?"
                    send_whatsapp_interactive_message(sender)  # Call the function to send a text message
            else:
                print("No 'messages' key found in the incoming data.")
        else:
            print("No 'changes' found in the entry.")
    else:
        print("No 'entry' key found in the incoming data.")

    return jsonify({"status": "success"}), 200  # Acknowledge receipt of the message

def send_whatsapp_interactive_message(recipient_id):
    """Send an interactive message to the user."""
    url = f"https://graph.facebook.com/v22.0/574126562443300/messages"  # Use the correct endpoint
    headers = {'Content-Type': 'application/json',
               'Authorization':'Bearer EAAZAyg37sE4ABO2BDzeF1F18yibpv7ZCFSCvmjp3ksiZCLweiZBQv9vOSNTkgGCij1009DrLXf3Slx9fq1uyYd0lZBn91bTIwG4Dl3UK4ovnZCLm50yE8k9puGpFw6twZANgc1x3jEEDjyjiSxlnsdGkBXHEPH5VZCZCwqfZB21jYAA7q07MnBgP2BUtypHr15XVexvwZDZD'}
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient_id,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": "Welcome to Shop manager ."
            },
            "body": {
                "text": "What would you like to do?"
            },
            "footer": {
                "text": "Powered by 2boxmediahouse"
            },
            "action": {
                "button": "Menu Options",
                "sections": [
                    {
                        "title": "Create Shop",
                        "rows": [
                            {
                                "id": "create_shop",
                                "title": "Get Started",
                                "description": "Provide Shop name and a few necessary details."
                            },
                            {
                                "id": "get_into_myshop",
                                "title": "My Shop",
                                "description": "login to start managing you shop"
                            }
                        ]
                    },
                   
                ]
            }
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        print("Failed to send message:", response.json())
        
if __name__ == "__main__":
    app.run(debug=True)