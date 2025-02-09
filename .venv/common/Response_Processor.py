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

    def extract_description_and_amount(self):
    
        parts = self.text.lower().split("in", 1)
        
        if len(parts) > 1:
            
            # Extract the raw description and strip whitespace
            
            raw_description = parts[1].strip()
            
            pre_processed_description=word_tokenize(raw_description)
            
            if pre_processed_description :
                
                actual_description=pre_processed_description[0]
                actual_amount=pre_processed_description[1]
                
                print(f'Description:{actual_description}') 
                print(f'Amount:{actual_amount}') 
                
                return (actual_description,actual_amount)
        else:
            
            print("No description found after 'in'.")
            
            return None

# Example usage

responseProcessor = Response_Processor("cash in photocopying 2.50")

cashIn_Intention = responseProcessor.cash_In_intention()   

if cashIn_Intention:
    
    responseProcessor.extract_description_and_amount()
    
    print("Cash in detected!")
    
else:
    
    print("No cash in intention was detected!")

# Uncomment and use the following lines for registration checking
# responseProcessor = Response_Processor("register uncle cookies print shop")
# registrationIntention = responseProcessor.checkForRegistration()
# if registrationIntention:
#     shopName = responseProcessor.extract_shop_name()
#     print(f'Shop name is {shopName}')