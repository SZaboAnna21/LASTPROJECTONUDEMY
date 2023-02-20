from googletrans import Translator
import time
import ast
import os


translator = Translator()
cardsLIST=[]
cardList2=[]
print("HELLO")
validanswer=["igen","nem"]
validanswertöröl=["töröl", "marad"]




with open("pytonUDEMY2023\\flie.txt") as f:
    cardsLIST=f.read()

if not cardsLIST:
    print ("list is empty")
    cardsLIST=[]
else:
    [s.strip() for s in cardsLIST[1:-1].split(',')]
    cardsLIST=ast.literal_eval(cardsLIST)

print(f"Egyenlore {len(cardsLIST)} db szópár van a fáljba ")
if len(cardsLIST) != 0:
    loop=True
    while loop:
        megnéziaszavakat=input("meg akarod nézni ezeket a szavakat? (igen/nem)  ")
        if megnéziaszavakat in validanswer:
                loop=False
                if megnéziaszavakat=="igen":
                    print(cardsLIST)
                    loop = True
                    while loop:
                        törlés=input("maradjanak vagy töröljük ezeket a szavakt? (marad/töröl)  ")
                        if törlés in validanswertöröl:
                            loop=False
                            if törlés =="töröl":
                                cardsLIST=[]
                        else:
                            print(f"bocsi ezt nem ertem valasz valaszt innem:{validanswertöröl}")
                            time.sleep(1)
        else:
                print("Kerlek igen vagy nem valaszokat hasznald")
                time.sleep(1)


#print(type(cardsLIST))
#print(type(cardList2))


#faljon lévo dolgok törlése
f = open("pytonUDEMY2023\\flie.txt", "r+") 
f.seek(0) 
f.truncate() 


def translate(wordhu):
    english = translator.translate( wordhu, src="hu", dest="en").text
    return english



def addANewCard():
    global cardList2
    wordhu=input("kerlek add meg azt a magyar szot amit angolul akarsz megtanulni:  ")
    worden = translate(wordhu)
    time.sleep(1)
    print(worden)
    newCard = (wordhu, worden)
    time.sleep(1)

    loop=True 
    while loop:
        answer = input(f"Akarod ezt a part({newCard}) hozzadni a listahoz? (igen\nem)  ")
        if answer in validanswer:
            loop=False
            if answer == "igen":
                print("Hozzáadás...")
                time.sleep(1)
                list.append(cardList2,newCard)
        else:
            print(f"Kerlek valassz valaszt ezek kozul:{validanswer}")
            time.sleep(1)



again = True 
while again:
    addANewCard()
    time.sleep(1)
    loop=True
    while loop:
        another = input("Akarsz e meg egy part hozzadni az eddigiekhez? (igen\nem)  ")
        if another in validanswer:
            loop=False
            if another =="nem":
                again = False


time.sleep(1)
print(cardList2)
if (not cardList2):
    if cardsLIST:
        with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
            f.write(str(cardsLIST))
            print("End of program")
    else:
        print("End of program")
else:
    loop=True
    while loop:
        answer = input("Hozzáakarod adni ezeket a fáljhoz? (igen/ nem)  ")
        if answer in validanswer:
            loop=False
            if answer =="igen":
                if not cardsLIST:
                    with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
                        f.write(str(cardList2))
                    print("Hozzáadás...")
                    print("End of program")
                else:
                    cardList2.extend(cardsLIST)
                    with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
                        f.write(str(cardList2))
                    print("Hozzáadás...")
                    print("End of program")
            else:
                print("End of program")
        else:
            print(f"Kerlek valassz valaszt ezek kozul:{validanswer}")
            time.sleep(1)