import json
import Consonants

trip_consonant_json = json.dumps(Consonants.triple_consonants)
trip_consonant_list = json.loads(trip_consonant_json)
double_consonant_json = json.dumps(Consonants.double_consonants)
double_consonant_list = json.loads(double_consonant_json)
single_consonant_json = json.dumps(Consonants.single_consonants)
single_consonant_list = json.loads(single_consonant_json)


def get_consonant(word):
    return get_triple_consonant(word)


def get_triple_consonant(word):
    consonant = word[0:3]
    try:
        return trip_consonant_list[consonant]
    except:
        return get_double_consonant(word)


def get_double_consonant(word):
    consonant = word[0:2]
    try:
        return double_consonant_list[consonant]
    except:
        return get_single_consonant(word)


def get_single_consonant(word):
    consonant = word[0:1]
    try:
        return single_consonant_list[consonant]
    except:
        return False
