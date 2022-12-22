eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

direction = input('Вы хотите зашифровать или дешифровать ваше сообщение - (зашифровать-1/2-дешифровать): ')
language = input('Выберите язык - (русский-1/2-английский): ')
step = input('Зашифруйте или дешифруйте текст, нажав любую цифру от 1 до 25: ')
text = input('Введите текст, который нужно зашифровать или дешифровать: ')
result = ''

if direction == '1':
    if language == '1':
        for i in text:
            if not i.isalnum() or i.isdigit():
                result += i
            if i.isupper():
                result += rus_upper_alphabet[rus_upper_alphabet.find(i) - 32 + int(step)]
            elif i.islower():
                result += rus_lower_alphabet[rus_lower_alphabet.find(i) - 32 + int(step)]
    elif language == '2':
        for i in text:
            if not i.isalnum() or i.isdigit():
                result += i
            if i.isupper():
                result += eng_upper_alphabet[eng_upper_alphabet.find(i) - 26 + int(step)]
            elif i.islower():
                result += eng_lower_alphabet[eng_lower_alphabet.find(i) - 26 + int(step)]
elif direction == '2':
    if language == '1':
        for i in text:
            if not i.isalnum() or i.isdigit():
                result += i
            if i.isupper():
                result += rus_upper_alphabet[rus_upper_alphabet.find(i) - int(step)]
            elif i.islower():
                result += rus_lower_alphabet[rus_lower_alphabet.find(i) - int(step)]
    elif language == '2':
        for i in text:
            if not i.isalnum() or i.isdigit():
                result += i
            if i.isupper():
                result += eng_upper_alphabet[eng_upper_alphabet.find(i) - int(step)]
            elif i.islower():
                result += eng_lower_alphabet[eng_lower_alphabet.find(i) - int(step)]
print(result)