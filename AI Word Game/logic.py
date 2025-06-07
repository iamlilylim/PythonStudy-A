#randomly popping words
#checking the answers
#saving the frequent mistakes

import random
from word_data import word_dict

#saving mistakes
mistakes_list = []
#giving a question: #Todo - to give more questions (later update)
def get_question(level):
    #randomly pick a word
    return random.choice(word_dict[level])#

#checking the answers

def check_answer( correct ,user_input ):
    #compare correct and user_input(change into lower cases)
    is_correct = correct.lower() == user_input.lower()

    #when incorrect-> append to the mistakes_list
    if not is_correct:
        mistakes_list.append((correct,user_input))

    #return the result
    return is_correct


