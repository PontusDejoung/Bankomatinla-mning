import jsonpickle
from dataclasses import dataclass
@dataclass
class accountInfo:
    kontonummer: int
    saldo: int
def startMenu():
    print("    Meny    ")
    print("1. Skapa konto")
    print("2. Logga in på konto")
    print("3. Avsluta")
def accountSelection():
    while True:
        startMenu()
        selection = menuInput("Ange ett val:", minValue=1,maxValue=3)
        if selection == 1:
            accountCreation()
        elif selection == 2:
            loginMenu()
        elif selection == 3:
            break
def loginMenu():
    accountNumber = int(input("Ange ditt kontonummer"))
    if accountNumber not in allaccounts:
        print("Felaktigt kontonummer")
    else:
        while True:
            print("1.Ta ut pengar")
            print("2.Sätt in pengar")
            print("3.Visa saldo")
            print("4.Logga ut")
            selection = menuInput("Ange val:", minValue=1,maxValue=4)
            if selection == 1:
                accountNumber = accountWithdrawal(accountNumber)
              
            elif selection == 2:
                accountNumber = accountDeposit(accountNumber)
                
                #accountDeposit(accountNumber)
            elif selection == 3:
                if accountNumber in allaccounts:
                    print(f"Ditt saldo är {allaccounts[accountNumber]}")
            elif selection == 4:
                 break
def menuInput(prompt,minValue, maxValue):
    while True:
        try:
            selection = int(input(prompt))
            if selection < minValue or selection > maxValue:
                 print(f"Mata in ett tal mellan {minValue} och {maxValue} tack")
            else:
                 break
        except ValueError:
             print("Mata in ett tal tack")
             continue
    return selection
def accountCreation ():
    while True:
        try:
            accountNumber = int(input("Skriv in ett kontonummer: "))
            if accountNumber not in allaccounts: 
                allaccounts[accountNumber] = accountNumber
                saldo = allaccounts[accountNumber] = allaccounts[accountNumber] = 0
                print("Kontot skapas")
                break
            else:#elif accountNumber in allaccounts:
                print("Kontonummer är upptaget,försök igen")
                continue
        except ValueError:
            print("Kontonummret kan bara innehålla siffror")
            continue
    return accountNumber
def accountWithdrawal (accountNumber):
    while True:
        try:
            withdrawalAmount = float(input("Hur mycket vill du ta ut?: "))
            if allaccounts[accountNumber] >= withdrawalAmount:
                allaccounts[accountNumber] = allaccounts[accountNumber] - withdrawalAmount
                print(f"Du har nu tagit ut {withdrawalAmount} Ditt saldo är nu {allaccounts[accountNumber]}")
                break
            else:
                print(f"Ditt saldo är {allaccounts[accountNumber]}, försök ,med en mindre summa")
                continue
        except ValueError:
            print("Du kan bara mata in siffror")
            continue
    return accountNumber
def accountDeposit (accountNumber):
    while True:
        try:
            depositmoney = float(input("Hur mycket vill du sätta in?: "))
            allaccounts[accountNumber] = allaccounts[accountNumber] + depositmoney
            print(f"{depositmoney} insatt på ditt konto, ditt saldo är nu {allaccounts[accountNumber]}")
            break
        except ValueError:
            print("Du kan bara mata in siffror")
            continue
    return accountNumber
allaccounts = {}
# with open("accountinfo.txt", "r") as file:
#     allaccounts = jsonpickle.decode(file.read())
# with open("accountinfo.txt", "r") as file:
#     for raden in file:
#         accountNumber = raden.replace("\n", "")
#         if accountNumber not in allaccounts:
#             accountNumber = int(accountNumber)
#             allaccounts[accountNumber] = 0
# print(f"{allaccounts}")
accountSelection()
# with open("accountinfo.txt", "r") as file:
#     file.write(jsonpickle.encode(allaccounts))

# with open("accountinfo.txt","r") as filen:
#     for rad in filen:
#         allaccounts = (rad.replace("\n", ""))
# while True:
#     startMenu()
#     selection = menuInput("Ange ett val:", minValue=1,maxValue=3)
#     if selection == 1:
#         accountNumber = accountCreation()
#     elif selection == 2:
#         loginMenu(accountnumberlogin=1)
#     elif selection == 3:
#         break

    