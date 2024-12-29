
import json


def set_voice(lang):
    return 2 if lang == 'es' else 1

def set_responses_languaje(lang):
    return "es_set.json" if lang == 'es' else "en_set.json"

idiom = "es" if True else "en" # False para inglés. True para español. False to english. True to spanish.
languaje_voice = set_voice(idiom)
responses_json = json.load((open(set_responses_languaje(idiom), 'r', encoding='utf-8')))

