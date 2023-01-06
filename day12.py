class Elf:
    def __init__(self):
        self.itemsList = []
        # Maximalwert von itemsList
        self.maximumFood = 0

    def calcMaxFood(self):
        for item in self.itemsList:
            self.maximumFood += int(item)


def getElfWithMaxFood(elfList):
    # Entfernen des letztens Elements, weil es leer sein wird
    elfWithMostFood = elfList[0]
    for i in range(len(elfList)):
        # Algorithmus zum finden des größten Wertes
        if elfList[i].maximumFood > elfWithMostFood.maximumFood:
            elfWithMostFood = elfList[i]
    return elfWithMostFood

def getTopNElvesFood(elfList, n):
    # Liste mit den n gesuchten Elementen
    nthElfList = []
    # Zum löschen aus der Liste
    elfPointer = None
    # Solange Suchen, bis die geforderten n-Elemente gefunden wurden
    for i in range(0, n):
        # Zurücksetzten des ersten Messelfes, damit der vergleich im Loop weitergeht
        nthElfWithMaxFood = elfList[0]
        for j in range(0, len(elfList)):
            print(j)
            if elfList[j].maximumFood > nthElfWithMaxFood.maximumFood:
                nthElfWithMaxFood = elfList[j]
                elfPointer = j
        del elfList[elfPointer]
        nthElfList.append(nthElfWithMaxFood)
    return nthElfList

def mainCycle():
    # Liste aller elfen
    elfList = []
    # Userinput
    userInput = None
    # Laufvariable
    running = True
    # counter
    counter = 0
    while running:
        userInput = input()
        while userInput:
            if userInput == "n":
                break
            # Beim erstern durchlaufen von einem Elfen
            if counter == 0:
                print("Erstelle elfen")
                elf = Elf()
                elfList.append(elf)
                counter = 1
            elf.itemsList.append(int(userInput))
            userInput = input()
        counter = 0    
        if userInput == "n":
            print(f"Beende Aufnahme. Es gibt {len(elfList)} Elfen.")
            running = False
            break
    # Berechnen des maximalen Essens für jeden Elfen
    for elf in elfList:
        elf.calcMaxFood()
    # Ausgabe des Elfen mit dem meisten essen
    print(f"Der Elf mit dem meisten Proviant hat {getElfWithMaxFood(elfList).maximumFood} Kalorien mitsich.")
    nthElvesWithFood = input("Wieviele Elfen mit ihrem maximalen Essen sollen gesucht werden?")
    elvesWithFoodList = getTopNElvesFood(elfList, int(nthElvesWithFood))
    totalCalories = 0
    for elf in elvesWithFoodList:
        print(f"Auf {totalCalories} kommen {elf.maximumFood}")
        totalCalories += elf.maximumFood
    print(f"Insgesamt haben die top {nthElvesWithFood}-Elfen {totalCalories} Kalorien mitsich!")

    

if __name__ == '__main__':
    mainCycle()