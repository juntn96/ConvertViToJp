import json

single_special_end = {
    "m": {
        "vi": "m",
        "jp": "mmu"
    },
    "k": {
        "vi": "k",
        "jp": "kku"
    },
    "p": {
        "vi": "p",
        "jp": "ppu"
    },
    "t": {
        "vi": "t",
        "jp": "tto"
    },
    "c": {
        "vi": "c",
        "jp": "kku"
    }
}

double_special_end = {
    "nh": {
        "vi": "nh",
        "jp": "n"
    },
    "ng": {
        "vi": "ng",
        "jp": "n"
    },
    "ch": {
        "vi": "ch",
        "jp": "kku"
    },
}


single_end_json = json.dumps(single_special_end)
single_end_list = json.loads(single_end_json)
double_end_json = json.dumps(double_special_end)
double_end_list = json.loads(double_end_json)


def get_special_end(word):
    return get_double_end(word)


def get_double_end(word):
    special = word[len(word) - 2: len(word)]
    try:
        return double_end_list[special]
    except:
        return get_single_end(word)


def get_single_end(word):
    special = word[len(word) - 1: len(word)]
    try:
        return single_end_list[special]
    except:
        return False
