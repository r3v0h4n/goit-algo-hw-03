import re

def normalize_phone(phone_number):
    # Remove all non-digit characters except '+'
    cleaned_number = re.sub(r'\D', '', phone_number)

    if cleaned_number.startswith('+'):
        return cleaned_number
    
    if cleaned_number.startswith('380'):
        return "+" + cleaned_number

    return "+38" + cleaned_number

# Example usage
phone_numbers = [
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

sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
print(sanitized_numbers)