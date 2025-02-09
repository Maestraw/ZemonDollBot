from flask import Flask, request, jsonify
import requests

def welcome_Menu(recipient_id):
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
                "text": "Welcome.Click Menu Options to proceed."
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
                                # "description": "Provide Shop name and a few necessary details."
                            },
                            {
                                "id": "get_into_myshop",
                                "title": "My Shop",
                                # "description": "login to start managing you shop"
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
