import requests

class Text:
    def __init__(self,token,recipientid,message):
        
        self.token=token
        self.receipient=recipientid
        self.message=message
        
    def send_text_message(self):
        """Send a text message"""
        url = f"https://graph.facebook.com/v22.0/574126562443300/messages"  # Use the correct endpoint
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": self.receipient,
            "type": "text",
            "text": {
                "body": self.message,
            }
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            print("Failed to send message:", response.json())
            return False
        else:
            return True
