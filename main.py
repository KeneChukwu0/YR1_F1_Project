import getseasonschedule
import getsessionfastestlap
import getsessionresults

print("--------------------------------------------------------------------------------")

while True:
    print("1. Season Schedule")
    print("2. Session Results")
    print("3. Session Fastest Lap")
    print("4. Exit\n")
    num = input("Please enter a number\n")
    if num == "1":
        getseasonschedule.seasonschedule()
        print("-------------------")
        print("\n")
    elif num == "2":
        getsessionresults.sessionresults()
        print("-------------------")
        print("\n")
    elif num == "3":
        getsessionfastestlap.sessionfastestlap()
        print("-------------------")
        print("\n")
    elif num == "4":
        break
    else:
        print("Not an option, please reenter\n")

print("--------------------------------------------------------------------------------")
