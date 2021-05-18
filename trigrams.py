import random

def build_trigram(WordList):
    trigram_dict = dict()
    for index in range(len(WordList)-2):
        key = tuple(WordList[index:index+2])
        if key in trigram_dict.keys():
            trigram_dict[key].append(WordList[index+2])
        else:
            trigram_dict[key] = [WordList[index+2]]
    return trigram_dict


def get_last_pair(WordList):
    return tuple(WordList[-2:])

def pick_random_pair(tri_dict):
    return random.choice(list(tri_dict.keys()))


def get_random_follower(tri_dict, key):
    try:
        return random.choice(tri_dict[key])
    except KeyError:
        return random.choice(tri_dict[random.choice(list(tri_dict.keys()))])

def make_sentence(tri_dict, sentence_length):
    sentence = list(pick_random_pair(tri_dict))
    sentence[0] = sentence[0].title()
    while len(sentence) < sentence_length:
        sentence.append(get_random_follower(tri_dict, get_last_pair(sentence)))
    return ' '.join(sentence) + '.'


def make_words(input_string):

    charaters_to_remove = ['.', ',', '-', '(', ')', '"', ' \'', '\' ', '\n']
    for character in charaters_to_remove:
        input_string = input_string.replace(character, ' ')
    
    words = input_string.split(' ')

    while '' in words:
        words.remove('')

    for ii in range(len(words)):
        if words[ii] == 'i' or words[ii] == 'I':
            words[ii] = words[ii].upper()
        else:
            words[ii] = words[ii].lower()

    
    return words



