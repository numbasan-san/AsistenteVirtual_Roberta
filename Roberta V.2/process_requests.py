
# process_requests.py
import responses, re, es_dep_news_trf
from nltk.corpus import stopwords

nlp = es_dep_news_trf.load()

def get_response(user_input):
    # Step 1: Remove special characters and numbers
    # Step 2: Convert to lowercase
    split_text = re.split(r'\s|[,:;¿?¡!-_]\s*', user_input.lower())
    print(split_text)
    texto = " ".join(split_text)

    # Step 3: Tokenization and lemmatization using spaCy
    doc = nlp(texto)
    tokens = [token.lemma_ for token in doc]

    # Step 4: Remove stopwords
    stop_words = stopwords.words("spanish")
    tokens_filtered = [word for word in tokens if word not in stop_words]
    return responses.check_all_messages(tokens_filtered)

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    # Calculate probability that user's message matches certain keywords
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words)) if recognized_words else 0

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
            
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0