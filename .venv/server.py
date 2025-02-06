from flask import Flask, request, jsonify
import requests
import os
# from openai import OpenAI
from common.Welcome_Menu  import welcome_Menu


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
                    welcome_Menu(sender)  # Call the function to send a text message
            else:
                print("No 'messages' key found in the incoming data.")
        else:
            print("No 'changes' found in the entry.")
    else:
        print("No 'entry' key found in the incoming data.")

    return jsonify({"status": "success"}), 200  # Acknowledge receipt of the message

        
if __name__ == "__main__":
    app.run(debug=True)