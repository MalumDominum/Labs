# coding=utf-8
import re


def longer_than_num(number, words, result=0):
    split = re.split(r'\W', words)
    print (words)
    for i in split:
        letters = 0
        for g in i:
            match = re.match(r'[a-z]|[A-Z]', g)
            if match:
                letters += 1
        if letters >= number:
            result += 1
    print ("Result: " + str(result))


num = int(input("Minimum characters in a word: "))
sentence_1 = "I am happy to take your donation; any amount will be greatly appreciated."
longer_than_num(num, sentence_1)
sentence_2 = "Should we start class now, or should we wait for everyone to get here?"
longer_than_num(num, sentence_2)
sentence_3 = "She works two jobs to make ends meet; at least, that was her reason for not having time to join us."
longer_than_num(num, sentence_3)
sentence_4 = ("What was the person thinking when they discovered cow’s milk was fine for human consumption… "
              "and why did they do it in the first place!?.")
longer_than_num(num, sentence_4)