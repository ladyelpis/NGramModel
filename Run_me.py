import tkinter as tk
from tkinter import filedialog
import re #регулярные выражения библиотека
import nltk #обработка текста library
import pickle #сохранить и открыть модель
import Text_class as tc
import NGram_class as ngc

#nltk.download() #загрузка nltk

#открыть текстовый файл
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("TXT files", "*.txt")])
file = open(file_path, encoding="UTF-8", mode="r") #кодировочка <3, r - открывает файл только для чтения

# загрузка информации
text = file.read()
file.close()

#обработка текста
text = tc.Text_class.RemoveSymbols(text)

#N-Граммовая Модель
words_tokens = []
ngrams = []
words = 3 #количество слов
words_tokens, ngrams = ngc.NGram_class.BuildNGramModel(text, words_tokens, ngrams, words)

#автоматический текстовый наполнитель, используя только что созданные триграммы слов.
curr_sequence = "В середине комнаты"
how_many = 500 #длина текста = 500 слов
ngc.NGram_class.GenerateText(curr_sequence, how_many, words_tokens, ngrams, words)

#сохранить модель
with open('words_tokens.pickle', 'wb') as handle:
    pickle.dump(words_tokens, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('ngrams.pickle', 'wb') as handle:
    pickle.dump(ngrams, handle, protocol=pickle.HIGHEST_PROTOCOL)

#открыть модель
with open('words_tokens.pickle', 'rb') as handle:
    words_tokens2 = pickle.load(handle)
with open('ngrams.pickle', 'rb') as handle:
    ngrams2 = pickle.load(handle)

#автоматический текстовый наполнитель, используя только что созданные триграммы слов.
while True:
    print("")
    print("Введите любое слово")
    curr_sequence = input()
    ngc.NGram_class.GenerateText(curr_sequence, how_many, words_tokens2, ngrams2, words)