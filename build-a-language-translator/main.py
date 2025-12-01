translations = {
  "bathroom":"baño",
  "beer":"cerveza",
  "bread":"pan",
  "breakfast":"desayuno",
  "cat":"gato",
  "dad":"papá",
  "dog":"perro",
  "family":"familia",
  "food":"comida",
  "friend":"amigo",
  "goodbye":"adiós",
  "hello":"hola",
  "house":"casa",
  "love":"amor",
  "mom":"mamá",
  "money":"dinero",
  "moon":"luna",
  "night":"noche",
  "no":"no",
  "please":"por favor",
  "school":"escuela",
  "sorry":"lo siento",
  "sun":"sol",
  "thank you":"gracias",
  "yes":"sí",
  "water":"agua",
  "welcome":"bienvenido",
  "what":"qué",
  "when":"cuándo",
  "where":"dónde",
  "who":"quién",
  "why":"por qué",
  "work":"trabajo"
}

done = False

print('Type "done" at any time to exit')

while not done:
    word = input("Greetings! Type in an English word to translate: ")
    word = word.lower()

    if word == "done":
        done = True
    elif word in translations:
        print(translations[word])
    else:
        print("Translation unavailable")