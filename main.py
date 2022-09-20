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
def accountCreation (accountNumber):
    while True:
            try:
                accountNumber = int(input("Skriv in ett kontonummer: "))
                if accountNumber not in allaccounts:
                    allaccounts[accountNumber] = accountNumber
                    allaccounts[accountNumber] = 0
                    print("Konto skapat")
                    #with open("spelare.txt","w") as file:
                    #for raden in filen:
                    #file.write(namn + "\n")
                    break
            except ValueError:
                print("Kontonummret kan bara innehålla siffror")
                continue
            else:
                print("Kontonummer är upptaget,försök igen")
                continue
def accountWithdrawal (withdrawalAmount):
    while True:
        try:
            withdrawalAmount = float(input("Hur mycket vill du ta ut?: "))
            if allaccounts[accountnumberlogin] >= withdrawalAmount:
                allaccounts[accountnumberlogin] = allaccounts[accountnumberlogin] - withdrawalAmount
                print(f"Du har nu tagit ut {withdrawalAmount} Ditt saldo är nu {allaccounts[accountnumberlogin]}")
                break
            else:
                print(f"Ditt saldo är {allaccounts[accountnumberlogin]}, försök ,med en mindre summa")
                continue
        except ValueError:
            print("Du kan bara mata in siffror")
            continue
def accountDeposit (depositAmount):
    while True:
        try:
            depositmoney = float(input("Hur mycket vill du sätta in?: "))
            if allaccounts[accountnumberlogin] < depositmoney:
                allaccounts[accountnumberlogin] = allaccounts[accountnumberlogin] = depositmoney
                print(f"{depositmoney} insatt på ditt konto, ditt saldo är nu {allaccounts[accountnumberlogin]}")
                break
            else: 
                allaccounts[accountnumberlogin] = allaccounts[accountnumberlogin] + depositmoney
                print(f"{depositmoney} insatt på ditt konto, ditt saldo är nu {allaccounts[accountnumber]}")
                break
        except ValueError:
            print("Du kan bara mata in siffror")
            continue
allaccounts = {}
while True:
    print("    Meny    ")
    print("1. Skapa konto")
    print("2. Logga in på konto")
    print("3. Avsluta")
    selection = menuInput("Ange ett val:", minValue=1,maxValue=3)
    if selection == 1:
        accountCreation(accountNumber=1)
    elif selection == 2:
        accountnumberlogin = int(input("Ange ditt kontonummer"))
        if accountnumberlogin not in allaccounts:
            print("Felaktigt kontonummer")
        else:
            while True:
                print("1.Ta ut pengar")
                print("2.Sätt in pengar")
                print("3.Visa saldo")
                print("4.Logga ut")
                selection = menuInput("Ange val:", minValue=1,maxValue=4)
                if selection == 1:
                    accountWithdrawal(withdrawalAmount=1)
                elif selection == 2:
                    accountDeposit(depositAmount=1)
                elif selection == 3:
                    if accountnumberlogin in allaccounts:
                        print(f"Ditt saldo är {allaccounts[accountnumberlogin]}")
                elif selection == 4:
                    break
    elif selection == 3:
        break
    