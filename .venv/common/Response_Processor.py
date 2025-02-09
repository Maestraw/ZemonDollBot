import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class Response_Processor:
    def __init__(self, text):
        self.text = text

    def checkForRegistration(self):
        trigger_words = ("register",)
        rawText = self.text.lower()
        pre_processed_text = word_tokenize(rawText)
        if any(word in pre_processed_text for word in trigger_words):
            print('Matched trigger word')
            return True
        else:
            print('Did not match trigger word')
            return False

    def extract_shop_name(self):
        parts = self.text.lower().split("register", 1)
        if len(parts) > 1:
            shop_name = parts[1].strip().split(",")[0].strip()
            return shop_name
        return None

    def cash_In_intention(self):
        trigger_words = ("cash", "in")
        preprocessed_text = word_tokenize(self.text.lower())
        if all(word in preprocessed_text for word in trigger_words):
            return True
        else:
            return False

    def cash_Out_intention(self):
        trigger_words = ("cash", "out")
        preprocessed_text = word_tokenize(self.text.lower())
        if all(word in preprocessed_text for word in trigger_words):
            return True
        else:
            return False

    def extract_description_and_amount(self):
        parts = re.split(r'\bin\b|\bout\b', self.text.lower(), 1)
        if len(parts) > 1:
            # Extract the raw description and strip whitespace
            raw_description = parts[1].strip()
            pre_processed_description = word_tokenize(raw_description)

            # Check if there are enough tokens for description and amount
            if len(pre_processed_description) >= 2:
                # Join all tokens except the last one as the description
                actual_description = ' '.join(pre_processed_description[:-1])  # All but the last token
                actual_amount = pre_processed_description[-1]  # Last token as the amount
                print(f'Description: {actual_description}') 
                print(f'Amount: {actual_amount}') 
                return (actual_description, actual_amount)
            else:
                print("Not enough tokens to extract description and amount.")
                return None
        else:
            print("No description found after 'in' or 'out'.")
            return None

# Example usage
responseProcessor = Response_Processor("cash out bond paper and ink 2.50")
cashOut_Intention = responseProcessor.cash_Out_intention()   
if cashOut_Intention:
    responseProcessor.extract_description_and_amount()
    print("Cash Out detected!")
else:
    print("No cash Out intention was detected!")

# Uncomment and use the following lines for registration checking
# responseProcessor = Response_Processor("register uncle cookies print shop")
# registrationIntention = responseProcessor.checkForRegistration()
# if registrationIntention:
#     shopName = responseProcessor.extract_shop_name()
#     print(f'Shop name is {shopName}')