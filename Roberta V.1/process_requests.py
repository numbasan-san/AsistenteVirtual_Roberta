
# process_requests.py
import re, responses
from unidecode import unidecode

def get_response(input):
    user_input = unidecode(input)
    split_message = re.split(r'\s|[,:;¿?¡!-_]\s*', user_input.lower())
    
    response = responses.check_all_messages(split_message)
    return response

def message_probability(user_message, reconized_words, single_response = False, requierd_words = []):
    message_certainty = 0
    has_required_words = True
    for word in user_message:
        if word in reconized_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len (reconized_words))
    for word in reconized_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int (percentage * 100)
    else:
        return 0
