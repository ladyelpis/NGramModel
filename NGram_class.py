import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re

class NGram_class(object):
    """Строит N-Gram языковую модель"""

    def BuildNGramModel(text, words_tokens, ngrams, words): #строит языковую модель
        #text → наш текст
        #words_tokens → слова
        #ngrams → N-граммы
        #words → количество слов

        ngrams = {}
        words_tokens = nltk.word_tokenize(text)
        for i in range(len(words_tokens)-words):
            seq = ' '.join(words_tokens[i:i+words])
            #print(seq) #вывод слов
            if  seq not in ngrams.keys():
                ngrams[seq] = []
            ngrams[seq].append(words_tokens[i+words])
            # fdist = nltk.FreqDist(ngrams)
            # for key in fdist:
            #     print(key, fdist[key])
        return words_tokens, ngrams;

    def GenerateText(curr_sequence, how_many, words_tokens, ngrams, words): #генерирует текст, используя триграммы слов
        #curr_sequence → любое входное слово
        #how_many → сколько слов надобно
        #words_tokens → наша база слов
        #ngrams → наши N-граммы
        #words → количество слов

        output = curr_sequence
        print("*************")
        for i in range(how_many):
            if curr_sequence not in ngrams.keys():
                if curr_sequence not in words_tokens:
                    i = len(words_tokens)
                    j = random.randrange(i-4)
                    curr_sequence = ' '.join(words_tokens[j:(j+3)])
                else:
                    rs = {x: y for x, y in ngrams.items() if re.match('.*%s.*' % curr_sequence, x, re.IGNORECASE)}
                    ls = list(rs.keys())
                    if len(ls) != 0:
                        curr_sequence = ls[0]    
            possible_words = ngrams[curr_sequence]
            next_word = possible_words[random.randrange(len(possible_words))]
            output += ' ' + next_word
            seq_words = nltk.word_tokenize(output)
            curr_sequence = ' '.join(seq_words[len(seq_words)-words:len(seq_words)])
        print(output) #вывод текста 
        print("*************")