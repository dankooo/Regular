# https://regexr.com/ - тут можно чекать регулярки

import pyperclip
import re

phoneRegex = re.compile(
    r'((\d{3}|\(\d{3}\))(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{2,4})(\s|-|\.)?(\d{2})?(\s*(ext|x|ext.)\s*(\d{2,5}))?)')

emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4})')

linkRegex = re.compile(
    r'((https|http|ftp):\/\/)([a-zA-Z0-9]+)([.a-zA-Z]+)*([\/a-zA-Z0-9]+)*(\.(html|php))?')
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
for groups in linkRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена: ')
    print('\n'.join(matches))
else:
    print('Телефонные номера и E-Mail не найдены.')
