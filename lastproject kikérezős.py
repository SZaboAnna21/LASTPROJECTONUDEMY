import random
import time
import ast

print("Hello itt tudod megtanulni a szavakat a program addig fut ameg az osszes faljba levo szo jelenteset jol be nem irtad vagy addig ameddig be nem irod az 'END' szót")
kezdes=time.time()
with open("pytonUDEMY2023\\flie.txt", "r")as f:
    cardlist=f.read()

if not cardlist:
    cardlist=[]
    print("nincs szopar a fajlba hasznald a masik programot hogy tele legyen a fajl\nENd of program")
    exit()
else:
    [s.strip() for s in cardlist[1:-1].split(',')]
    cardlist=ast.literal_eval(cardlist)
    cardlistszama=len(cardlist)

#print(cardlist)
#print(type(cardlist))


def randomvalsztas():
    global cardlist
    szopar= random.choice(cardlist)
    return szopar


folytat=True
while folytat:
    if cardlist:
        szopar=randomvalsztas()
        guess=input(f"ADD meg magyarul a kovetkezo angol szo jelenteset\n{szopar[1]}:  ")
        if guess ==szopar[0]:
            list.remove(cardlist,szopar)
        elif guess=="END":
            print("megszakitas...\nend of program")
            vege=time.time()
            megtanultszo=(cardlistszama)-len(cardlist)
            ido=vege-kezdes
            print(f"megtanultal:{megtanultszo} szót {ido} masodperc alatt ")
            #faljon lévo dolgok törlése
            f = open("pytonUDEMY2023\\flie.txt", "r+") 
            f.seek(0) 
            f.truncate()
            with open("C:\\Users\\szabo\\OneDrive\\Dokumentumok\\pyton\\complete_coding_Udemy\\pytonUDEMY2023\\flie.txt", "a") as f:
                f.write(str(cardlist))
            folytat=False
        else:
            print("Ezt sajnos nem talaltad el probalkozz még!")
            time.sleep(1)
    else:
        print("End of program")
        vege=time.time()
        cardlistszama
        ido=vege-kezdes
        print(f"megtanultal:{cardlistszama} szót {ido} masodperc alatt ")
        #faljon lévo dolgok törlése
        f = open("pytonUDEMY2023\\flie.txt", "r+") 
        f.seek(0) 
        f.truncate()
        folytat=False
