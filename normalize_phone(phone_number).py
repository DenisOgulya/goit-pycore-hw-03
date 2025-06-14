import re

def normalize_phone(phone_number):
    pattern = r"[;,\-:!\.\()\s]"
    phone_number = re.sub(pattern, "", phone_number) 
    
    index_of_0_in_number =  phone_number.find("0")
    
    if index_of_0_in_number == 0:
        phone_number = "+38" + phone_number
    elif index_of_0_in_number == 1:
        phone_number = "+3"+ phone_number
    elif index_of_0_in_number == 2:
        phone_number = "+" + phone_number
    else:
        return(phone_number )
    
        
        
    
    
    return(phone_number)

corrected_phone_number = normalize_phone("   8093)--451-4441  "  )
print(corrected_phone_number)