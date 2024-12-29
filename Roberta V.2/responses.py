
# responses.py
import json, random, process_requests, actions, config

print((config.responses_json["clean_user_google_search"])["filter_words"])
# print(config.responses_json["im_fine_list_of_words"])
# input()

def check_all_messages(message):
    highest_prob = {}

    # Store probability of each possible response based on keywords
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        # print(f"Comparando mensaje: '{message}' con: {list_of_words}")
        highest_prob[bot_response] = process_requests.message_probability(message, list_of_words, single_response, required_words)
    
    # Define response patterns with keywords, and check probability of each
    response(
        lambda: actions.respond_to_greeting(), 
        config.responses_json["greeting_list_of_words"], 
        single_response=True
    )
    response(
        lambda: actions.im_fine(), 
        config.responses_json["im_fine_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["im_fine_required_words"]
    )
    response(
        lambda: actions.say_my_name(), 
        config.responses_json["say_my_name_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["say_my_name_required_words"]
    )
    response(
        lambda: actions.courteous_reply(), 
        config.responses_json["courteous_reply_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["courteous_reply_required_words"]
    )
    response(
        lambda: actions.thankful_reply(),
        config.responses_json["thankful_reply_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["thankful_reply_required_words"]
    )
    response(
        lambda: actions.open_whatsapp(),
        config.responses_json["open_whatsapp_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["open_whatsapp_required_words"]
    )
    response(
        lambda: actions.search_google(message),
        config.responses_json["search_google_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["search_google_required_words"]
    )
    response(
        lambda: actions.search_youtube(message),
        config.responses_json["search_youtube_list_of_words"], 
        single_response=True, 
        required_words=config.responses_json["search_youtube_required_words"]
    )

    best_match = max(highest_prob, key=highest_prob.get)
    # print(f"Mejor coincidencia: {best_match} con probabilidad: {highest_prob[best_match]}")
    return unknown() if highest_prob[best_match] < 1 else best_match()

def unknown(): # return a random response when input is unrecognized
    return config.responses_json["unknown_response"][random.randrange(5)]
