import re

def normalize_phone(phone_number):
    pattern = r"[^+]"
    phone_number = re.sub(pattern, "", phone_number) 
    return(phone_number)
corrected_phone_number = normalize_phone(    +38(093)451-4441  )
