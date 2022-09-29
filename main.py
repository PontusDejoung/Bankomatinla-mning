def startMenu():
    print("    Meny    ")
    print("1. Skapa konto")
    print("2. Logga in på konto")
    print("3. Avsluta")
def accountSelection(allaccounts:dict):
    while True:
        startMenu()
        firstMenuSelection = menuIntInput("Ange ett val:", minValue=1,maxValue=3)
        if firstMenuSelection == 1:
            accountNumber = accountCreation()
            allaccounts[accountNumber] = accountNumber
            allaccounts[accountNumber] = allaccounts[accountNumber] = 0
        elif firstMenuSelection == 2:
            loginMenu(allaccounts)
        elif firstMenuSelection == 3:
            break
def loginMenu(allaccounts:dict):
    while True:
        try:
            logInAccountNumber = int(input("Ange ditt kontonummer"))
            if logInAccountNumber not in allaccounts:
                print("Felaktigt kontonummer, försök igen")
                continue
            else:
                while True:
                    print("1.Ta ut pengar")
                    print("2.Sätt in pengar")
                    print("3.Visa saldo")
                    print("4.Logga ut")
                    secondMenuSelection = menuIntInput("Ange val:", minValue=1,maxValue=4)
                    if secondMenuSelection == 1:
                        withdrawalAmount = accountWithdrawal(allaccounts,logInAccountNumber)
                        allaccounts[logInAccountNumber] = allaccounts[logInAccountNumber] - withdrawalAmount
                        print(f"Du har nu tagit ut {withdrawalAmount} Ditt saldo är nu {allaccounts[logInAccountNumber]}")
                    elif secondMenuSelection == 2:
                        depositmoney = accountDeposit()
                        allaccounts[logInAccountNumber] = allaccounts[logInAccountNumber] + depositmoney
                        print(f"{depositmoney} insatt på ditt konto, ditt saldo är nu {allaccounts[logInAccountNumber]}")
                    elif secondMenuSelection == 3:
                        if logInAccountNumber in allaccounts:
                            print(f"Ditt saldo är {allaccounts[logInAccountNumber]}")
                    elif secondMenuSelection == 4:
                        break
        except ValueError:
            print("Mata in ett tal tack")
            continue
        break
def menuIntInput(prompt,minValue:int, maxValue:int):
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
                print("Kontot har skapats")
                return accountNumber
            else:
                print("Kontonummer är upptaget,försök igen")
                continue
        except ValueError:
            print("Kontonummret kan bara innehålla siffror")
            continue
def accountWithdrawal (allaccounts,accountNumber:int):
    while True:
        try:
            withdrawalAmount = float(input("Hur mycket vill du ta ut?: "))
            if allaccounts[accountNumber] >= withdrawalAmount:
                return withdrawalAmount
            else:
                print(f"Ditt saldo är {allaccounts[accountNumber]}, försök med en mindre summa")
                continue
        except ValueError:
            print("Du kan bara mata in siffror")
            continue
def accountDeposit ():
    while True:
        try:
            depositmoney = float(input("Hur mycket vill du sätta in?: "))
            return depositmoney
        except ValueError:
            print("Du kan bara mata in siffror")
            continue
allaccounts = {}
accountSelection(allaccounts)