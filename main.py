import getseasonschedule
import getsessionfastestlap
import getsessionresults
import getsessionresultsadvanced

gui = False

print("--------------------------------------------------------------------------------")

while True:
    print("1. Season Schedule")
    print("2. Simple Session Results")
    print("3. Advanced Session Results")
    print("4. Session Fastest Lap (WIP)")
    print("5. Exit\n")
    num = input("Please enter a number\n")
    if num == "1":
        getseasonschedule.seasonschedule(gui)
        print("-------------------")
        print("\n")
    elif num == "2":
        getsessionresults.sessionresults(gui)
        print("-------------------")
        print("\n")
    elif num == "3":
        getsessionresultsadvanced.advancedsessionresults(gui)
        print("-------------------")
        print("\n")
    elif num == "4":
        getsessionfastestlap.sessionfastestlap()
        print("-------------------")
        print("\n")
    elif num == "5":
        break
    else:
        print("Not an option, please reenter\n")

print("--------------------------------------------------------------------------------")
