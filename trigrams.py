import random
import sys

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

    charaters_to_remove = ['.', ',', '-', '(', ')', '"', ' \'', '\' ', '\n', '*', '?']
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


def read_in_data(ebook_filename):
    ebook = open(ebook_filename)
    start_of_book_flag = 1 
    end_of_book_flag = 0
    start_of_book_string = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    end_of_book_string = '*** END OF THIS PROJECT GUTENBERG EBOOK'

    for line in ebook:
        if start_of_book_flag:
            if start_of_book_string in line:
                start_of_book_flag = 0
                in_data = ''
        elif end_of_book_flag:
            pass
        else:
            in_data += line

    ebook.close()
    return (in_data)

def build_text(tri_dict, sentence_length = 7, number_of_sentences  = 7):
    out_string = ''
    for index in range(number_of_sentences):
        out_string += make_sentence(tri_dict, sentence_length) + ' \n'
    return out_string


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)








