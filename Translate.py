from translate import Translator

lang_li = ['ja', 'en', 'hi', 'zh']
while True:
    print('''Please enter language code to translate in that language
            Language   Code
            Janpanes : ja
            Chinese  : zh
            Hindi    : hi
            English  : en
            ''')
    trans_to = input("Choose language: ")
    try:
        lang_index = lang_li.index(trans_to)
        break
    except ValueError:
        print('You have entered invalid lang code')
        print('Please try again')

while True:
    file_path = input("Please enter the file path: ")
    file_path = file_path.replace("\\", "/")

    try:
        file1 = open(file_path, mode='r+')
        break
    except FileNotFoundError:
        print('Invalid File path...')
        print('Try again...')

translator = Translator(to_lang=trans_to)

trans_file_name = input("Please enter the translated file name: ")
trans_file_path = input("Enter file path where you want to save the translated file: ")
trans_file_path = trans_file_path.replace("\\", "/")
file2 = open(f"{trans_file_path}/{trans_file_name}.txt", mode='w', encoding="utf-8")
file2.mode = 'a'
print("Please wait, while we are translating your file...")
st = file1.readlines()
for item in range(0, len(st)):
    translation = translator.translate(st[item])
    file2.write(translation + "\n")

print('''Thank you for waiting, 
Your file has been translated''')
file2.close()
file1.close()

# 'C:/Users/prasad/Desktop/myTxt.txt'
# C:\Users\prasad\Desktop\myTxt.txt
