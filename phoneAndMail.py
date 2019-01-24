# https://regexr.com/ - тут можно чекать регулярки

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\+?[0-9]{1,4})
    (\s|-|\.)?
    (\d\d\d(\d)?|\(\d\d\d(\d)?\))
    (\s|-|\.)?
    (\d\d\d|\d\d)
    (\s|-|\.)?
    (\d\d)
    (\s|-|\.)?
    (\d\d)
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9-]+
    \.
    [a-zA-Z]{2,4}
    )''',re.VERBOSE)

linkRegex = re.compile(r'''(
    ((https|http|ftp):\/\/)?
    ([a-zA-Z0-9а-яА-Я.]+\.[а-яА-Яa-zA-Z]{2,4})
    ((\/[a-zA-Z0-9-%_?|=]+)*)?
    (\.(html|php))?
    )''',re.VERBOSE)
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = str(groups[0])
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
