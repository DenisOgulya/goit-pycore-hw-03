import re

def normalize_phone(phone_number):
    
    pattern = r"[\D\s\;,\-:!\.\()]"
    phone_number = re.sub(pattern, "", phone_number) 
    
    index_of_0_in_phone_number =  phone_number.find("0")
    
    if index_of_0_in_phone_number == 0:
        phone_number = "+38" + phone_number
    elif index_of_0_in_phone_number == 1:
        phone_number = "+3"+ phone_number
    elif index_of_0_in_phone_number == 2:
        phone_number = "+" + phone_number
    else:
        return(phone_number )
    
    
    return(phone_number)

corrected_phone_number = normalize_phone("   8093)--451-4441  "  )
print(corrected_phone_number)

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)