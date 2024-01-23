#Dallas and Natalia
#1/12/24
#To-Do List

#Initialize
choresList=[]
#Function
#Chores Intro: prints instructions on how to use chores List
def choresIntro():
    print("Welcome to Chore List Maker. Answer the questions to add and complete tasks.")

#Main
while True:
    action=str(input("What do you want to do? \n1=Add a Task \n2=View Chore List \n3=Mark a Task as Completed \n4=Remove a Task \n5=Remove Whole List \n6=Sort List \n7=Quit"))
    if action=="1":
        choresList.append(input("What chore do you want to add?"))
    elif action=="2":
        print(choresList)
    elif action=="3":
        chore=input("What chore did you complete?")
        i=choresList.index(chore)
        choresList[i]=chore+" X"
    elif action=="4":
        choreremoved=input("What chore do you want to remove?")
        choresList.remove(choreremoved)
    elif action=="5":
        choresList.clear()
    elif action =="6":
        choresList.sort()
    elif action=="7":
        break
    else:
        print("Error occured, try again.")