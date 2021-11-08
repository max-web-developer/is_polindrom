# word= str(input('enter word:'))
# w = len(word)
# i = 0
# w = w - 1
# k = 0
# while w - i >= i:
#     if word[w - i] == word[i]: # Проверяем слово на полиндром
#         i += 1 
#     else:
#         k = 1
#         break
# if k == 1:
#   print("Not Polindrom")
# else:
#   print("Polindrom")

word = str(input('Enter word: '))
a = word[::-1] # Проверяем на полидром через последний индекс
list=[]
list.append(word.upper())
if word == a:
  print("Polindrom")
else:
  print("Not Polindrom")
  