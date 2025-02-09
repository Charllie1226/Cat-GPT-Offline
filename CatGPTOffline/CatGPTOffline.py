from configparser import ConfigParser
from random import randint
lang = ConfigParser()
lang.read("lang.ini")
print("Select a language")
user_langs=[]
numl = 1
for languages in lang.sections():
   print (f"{numl} : {lang[languages]['name']}")
   user_langs.append(lang.sections()[numl-1])
   numl += 1
user_select = input(">")
user_lang = user_langs[0]
try:
   user_lang = user_langs[int(user_select)-1]
except ValueError as e:
   print("Error:", e)

print(f"\n{lang[user_lang]['text1']}")
while 1:
    user_inp = input("User >")
    if user_inp == "":
        print(f"Cat GPT > {lang[user_lang]['anwser']}{lang[user_lang]['ques']}")
    else:
        if randint(0,1)==1 :
            print(f"Cat GPT > {lang[user_lang]['anwser']}{lang[user_lang]['peri']}")
        else:
            print(f"Cat GPT > {lang[user_lang]['anwser']}{lang[user_lang]['excm']}")