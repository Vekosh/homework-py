<<<<<<< HEAD
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def random_words(quantity : int, word: str = "абв"):  
    words_list = []
    for i in range(quantity):
        el = sample(word, 3)
        words_list.append(''.join(el))
    return ' '.join(words_list)

def simple_sentence(word: str) -> str:
    return ' '.join(i for i in word.split() if i != "абв")

res=random_words(int(input('Enter the number of words: ')))
print(res)
=======
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def random_words(quantity : int, word: str = "абв"):  
    words_list = []
    for i in range(quantity):
        el = sample(word, 3)
        words_list.append(''.join(el))
    return ' '.join(words_list)

def simple_sentence(word: str) -> str:
    return ' '.join(i for i in word.split() if i != "абв")

res=random_words(int(input('Enter the number of words: ')))
print(res)
>>>>>>> 2a27de4c503eb01003b9ffb752fb210131e45de7
print(simple_sentence(res))