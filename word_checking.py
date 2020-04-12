from openpyxl import load_workbook
import random

class Words():

    def __init__(self,en_ws,gr_ws,gr_ws1):
        self.en_ws = en_ws
        self.gr_ws = gr_ws
        self.gr_ws1 = gr_ws1
      
    def create_list_of_words(self,english_words,greek_words):
        for el in self.en_ws:
            english_words.append(el.value)

        for i in range(len(self.gr_ws)):
            greek_words.append([self.gr_ws[i].value,self.gr_ws1[i].value])

        return english_words,greek_words


class Steps():


    def __init__(self, eng_words, gr_words, recheck_eng_words, recheck_gr_words):
        self.eng_words = eng_words
        self.gr_words = gr_words
        self.recheck_eng_words = recheck_eng_words
        self.recheck_gr_words = recheck_gr_words

    
    def get_random_word(self):
        
        random_english_word = random.choice(self.eng_words)
        index = self.eng_words.index(random_english_word)
        random_greek_words = self.gr_words[index]

        return random_english_word , random_greek_words

    def write_a_word(self,ran_en_w,ran_gr_ws):
        for i in range(3):
            write_your_guess = input('{}:\t'.format(ran_en_w))
    
            if (steps.check_solution(write_your_guess,ran_gr_ws)):
                print('CORRECT')
                break

        if i==2:
            print("{}:\t{}".format(ran_en_w,ran_gr_ws))
            self.recheck_eng_words.append(ran_en_w)
            self.recheck_gr_words.append(ran_gr_ws)

       # print (self.recheck_words)
        
    def remove_checked_word(self,ran_en_w,ran_gr_ws):
        self.eng_words.remove(ran_en_w)
        self.gr_words.remove(ran_gr_ws)

    def check_solution(self,write_your_guess,random_greek_words):

        if (write_your_guess in random_greek_words):
            return True

    def convert_lists(self):
        self.gr_words = self.recheck_gr_words
        self.eng_words = self.recheck_eng_words
        self.recheck_eng_words = []
        self.recheck_gr_words = []
        



workbook = load_workbook(filename = "words.xlsx")
sheet = workbook.active

english_words = []
greek_words = []

en_ws = list(sheet["A"])
gr_ws = list(sheet["B"])
gr_ws1 = list(sheet["C"])




words = Words(en_ws, gr_ws, gr_ws1)

english_words , greek_words = words.create_list_of_words([],[])

initial_index = int(input('Starting word:\t'))
last_index = int(input("Last word:\t"))
english_words_indexed = english_words[initial_index:last_index+1]
greek_words_indexed = greek_words[initial_index:last_index+1]

steps = Steps(english_words_indexed, greek_words_indexed, [], [])

while True:
    while len(steps.eng_words)>0:
        
        ran_en_w , ran_gr_ws = steps.get_random_word()
        steps.write_a_word(ran_en_w, ran_gr_ws)
        steps.remove_checked_word(ran_en_w,ran_gr_ws)
        #print(steps.eng_words,'\n', steps.recheck_eng_words)

    if len(steps.recheck_eng_words)>0:
        steps.convert_lists()
    else:
        break


print('END')
