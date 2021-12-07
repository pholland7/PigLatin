import requests
userInput = input("Welcome to Pig Latin Translator! Enter a sentence to translate to Pig Latin: ")
userInput = userInput.split(" ")
construction = ""
for text in userInput:
    if text not in userInput[-1]:
        construction += text + "%20"
    else:
        construction += text
response = requests.get("https://api.funtranslations.com/translate/pig-latin.json?text=" + construction)
data = response.json()
print(data['contents']['translated'])
