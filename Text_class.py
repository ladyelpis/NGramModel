import re #регулярные выражения библиотека
import nltk #обработка текста library
import string

class Text_class(object):
    """класс для работы с текстом"""     
    
    def RemoveSymbols(text): #обработка текста: text → необработанный текст
        #минус теги
        text = re.sub(r'\<[^>]*\>', '', text)
        #минус сноски
        text = re.sub(r'\[[^>]*]', '', text)
        #стоп-слова 
        text = re.sub(r'(нем)', '', text)
        text = re.sub(r'(нем.)', '', text)
        text = re.sub(r'(фр)', '', text)
        text = re.sub(r'(фр.)', '', text)
        text = re.sub(r'(итал)', '', text)
        text = re.sub(r'(итал.)', '', text)
        text = re.sub(r'\n', ' ', text)
        #убираем латиницу
        text = re.sub(r'[A-z&=;]+', '', text)
        # разделение на слова
        from nltk.tokenize import word_tokenize
        tokens = word_tokenize(text)
        # понизить регистр слов
        tokens = [w.lower() for w in tokens]
        # убрать везде пунктуацию из слов
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # удалить неалфавитные токены
        words = [word for word in stripped if word.isalpha()]
        # удалить инглиш слова
        text = re.sub(r'[^А-Яа-я ]', '', text)
        return text;




