from googletrans import Translator
import time
import ast
translator = Translator()
cardsLIST=[]


with open("pytonUDEMY2023\\flie.txt") as f:
    cardsLIST=f.read()

if not cardsLIST:
    print ("lsit is empty")
    cardsLIST=[]
    cardList2=[]
else:
    [s.strip() for s in cardsLIST[1:-1].split(',')]
    cardsLIST=ast.literal_eval(cardsLIST)
    cardList2 =cardsLIST

print(f"Egyenlore {len(cardsLIST)} db szópár van a fáljba ")
if len(cardsLIST) != 0:
    megnéziaszavakat=input("meg akarod nézni ezeket a szavakat? (igen/nem)  ")
    if megnéziaszavakat=="igen":
        print(cardsLIST)
        törlés=input("maradjanak vagy töröljük ezeket a szavakt? (marad/töröl)  ")
        if törlés =="töröl":
            cardsLIST=[]
            cardList2=[]
        else:
            cardsLIST=[]
    else:
        cardsLIST=[]


print(type(cardsLIST))
print(type(cardList2))


#faljon lévo dolgok törlése
f = open("pytonUDEMY2023\\flie.txt", "r+") 
f.seek(0) 
f.truncate() 


def translate(wordhu):
    english = translator.translate( wordhu, src="hu", dest="en").text
    return english



def addANewCard():
    global cardsLIST
    wordhu=input("kerlek add meg azt a magyar szot amit angolul akarsz megtanulni:  ")
    worden = translate(wordhu)
    time.sleep(1)
    print(worden)
    newCard = (wordhu, worden)
    time.sleep(1)
    answer = input(f"Akarod ezt a part({newCard}) hozzadni a listahoz? (igen\nem)  ")
    if answer == "igen":
        print("Hozzáadás...")
        time.sleep(1)
        list.append(cardsLIST,newCard)



again = True 
while again:
    addANewCard()
    time.sleep(1)
    another = input("Akarsz e meg egy part hozzadni az eddigiekhez? (igen\nem)  ")
    if another =="nem":
        again = False


time.sleep(1)
print(cardsLIST)
if (not cardsLIST):
    if cardList2:
        with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
            f.write(str(cardList2))
            print("End of program")
    else:
        print("End of program")
else:
    answer = input("Hozzáakarod adni ezeket a fáljhoz? (igen/ nem)  ")
    if answer =="igen":
        if not cardList2:
            with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
                f.write(str(cardsLIST))
            print("Hozzáadás...")
            print("End of program")
        else:
            cardsLIST.extend(cardList2)
            with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
                f.write(str(cardsLIST))
            print("Hozzáadás...")
            print("End of program")

