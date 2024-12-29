
# handlers.py
import config

def clean_user_google_search(user_input): # normalize input for cleaner Google search queries
    user_input = ' '.join(user_input)

    filter_words = ((config.responses_json["clean_user_google_search"])["filter_words"])
    normalization_map = ((config.responses_json["clean_user_google_search"])["normalization_map"])

    # convert to lowercase for consistency in filtering
    cleaned_input = user_input.lower()

    # remove filter words
    for word in filter_words:
        cleaned_input = cleaned_input.replace(word, "").strip()

    # apply normalization mappings
    for old, new in normalization_map.items():
        cleaned_input = cleaned_input.replace(old, new).strip()

    # remove any extra whitespace
    cleaned_input = ' '.join(cleaned_input.split())

    return cleaned_input

def clean_user_yt_search(user_input): # normalize input for cleaner YouTube search queries
    user_input = ' '.join(user_input)
    
    filter_words = ((config.responses_json["clean_user_yt_search"])["filter_words"])
    normalization_map = ((config.responses_json["clean_user_yt_search"])["normalization_map"])

    # convert to lowercase for consistency in filtering
    cleaned_input = user_input.lower()

    # remove filter words
    for word in filter_words:
        cleaned_input = cleaned_input.replace(word, "").strip()

    # apply normalization mappings
    for old, new in normalization_map.items():
        cleaned_input = cleaned_input.replace(old, new).strip()

    # remove any extra whitespace
    cleaned_input = ' '.join(cleaned_input.split())

    return cleaned_input

def get_im_fine_response(): # returns a random "I'm fine" type response
    return config.responses_json["im_fine_responses"]

def get_introductions():
    return config.responses_json["introductions"]

def get_greetings(): # returns a list of greeting responses
    return config.responses_json["greetings"]

def get_courteous_reply(): # returns a courteous reply
    return config.responses_json["courteous_reply"]

def get_thankful_reply(): # returns a thankful reply
    return config.responses_json["thankful_reply"]
