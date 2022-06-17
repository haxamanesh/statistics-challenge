#project1
import csv
from os import name, system

def main():
    allowedInputTitles = range(1397, 1401)
    yearSubjectCount = {
            1400: 4,
            1399: 5,
            1398: 5,
            1397: 4,
    }
    csvHeader = [["Enterance","Class Variance" ,"Class Average", "First Student", "Second Student", "Third Student", "Failed"]]
    inputCount = 4
    studentData = {}
    enteranceinfo=[]
    variance=0
    
    for i in range(1, inputCount + 1):

        # inputTitle = None
                                                                #moshakhas kardan sal vorodi daneshjoo
        # while True:
        inputTitle = int(input("Enter Years Of Enterance: ")) 
            # if inputTitle in allowedInputTitles: break
        
        studentData[inputTitle] = []
        studentCount = int(input("Enter student count for the #{}: ".format(inputTitle)))
        # sumOfEnterance=0
        # averageOfEnterance=0
        enteranceaverage=[]                                                       #moshakhasat daneshjooye har vorodi
        for p in range(1, studentCount + 1):
            
            scores = []
            studentIDNumber = int(input("\tEnter student ID number #{}: ".format(p)))
            sex = input("\tEnter {}'s gender: ".format(studentIDNumber)) 
                                                                        
                                                                        
                                                                 #mohasebe nomre har daneshjoo            
            
            for z in range(1, yearSubjectCount[inputTitle] + 1):

                factor = int(input("\tEnter subject #{}'s factor: ".format(z)))
                score = float(input("\tEnter subject #{}'s score: ".format(z)))
                scores.append(str(score) + ":" + str(factor)) 
            average = calculateAverageOfStudent(scores)
            # sumOfEnterance += average
            qualify=QualifyStatus(average)
            studentData[inputTitle].append(["|studentIDnumber:",studentIDNumber,sex,
            scores,average,qualify])
            enteranceaverage.append(average)
            
        # clearScreen()
        
        # averageOfEnterance=(sumOfEnterance/studentCount)
        enteranceaverage.sort()
        enteranceinfo.append(enteranceaverage)
        

        print('averageOfEnterance:',enteranceinfo)

        print("miangin:",miangin(enteranceinfo))
        print("miane",miane(enteranceinfo))
        print(studentData)
    

    print(enteranceinfo)    
            

    




def saveArray(data):
    with open('database.csv', 'w+') as fh:
        csv.writer(fh, delimiter=",").writerows(data)

# def clearScreen():
#     if name == 'nt':
#         system('cls')
#     else:
#         system('clear')

def calculateAverageOfStudent(scoresAndFactors):
    scoreSum = 0
    factorSum = 0
    for scoreString in scoresAndFactors:
        scoreString = scoreString.split(":")
        score = float(scoreString[0])
        factor = int(scoreString[1])
        scoreSum += score * factor
        factorSum += factor
    return scoreSum / factorSum 
def QualifyStatus(average):
    if average >= 12 :
        return("passed")
    else :
         return("failed")      
# def varianse(scoresAndFactors):
#     scoresums=0
#     for i in  scoresAndFactors:
#         i=i.split(",")
#         x=i[0]
#         return ave
def miane(listnahayimoadelha):
    for i in listnahayimoadelha:
        if (range(i)/2)%2==1:
            print("miane:",i[(range(i)-1)/2])
        else:
            print("miane:",(i[(range(i)/2)]+i[(range(i)/2)-1])/2)

def miangin(listnahayimoadelha):
    for j in listnahayimoadelha:
        x=0
        for i in j:
            x += i
            return("miangin:",int(x)/(range(i)))
                        


if __name__ == '__main__': main()
