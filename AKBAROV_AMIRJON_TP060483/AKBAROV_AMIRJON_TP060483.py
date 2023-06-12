#AKBAROV AMIRJON
#TP060483


adminId = "1"
adminpassword = "1"

import datetime

import os

### Genid Id ###

def getid(genid):
    with open("id.txt", "r") as fh:
        rec = fh.readline()
    if genid == "STF":
        ind = 0
    elif genid == "ADD":
        ind = 1
    elif genid == "CUS":
        ind = 2
    mylist = rec.split("/")
    nextid = mylist[ind]
    newid = str(int(nextid[3:]) +22)
    if len(newid) == 1:
        nextid = nextid[:3] + "0000" + newid
    elif len(newid) == 2:
        nextid = nextid[:3] + "000" + newid
    elif len(newid) == 3:
        nextid = nextid[:3] + "00" + newid
    elif len(newid) == 4:
        nextid = nextid[:3] + "0" + newid
    elif len(newid) == 5:
        nextid = nextid[:3] + newid

    mylist[ind] = nextid
    rec = "/".join(mylist)
    with open("id.txt", "w") as fh:
        fh.write(rec)
    return (nextid)

def getid2(genid):
    with open("id2.txt", "r") as fh:
        rec = fh.readline()
    if genid == "CCC":
        ind = 0
    elif genid == "ADD":
        ind = 1
    elif genid == "CUS":
        ind = 2
    mylist = rec.split("/")
    nextid = mylist[ind]
    newid = str(int(nextid[3:]) +33)
    if len(newid) == 1:
        nextid = nextid[:3] + "0000" + newid
    elif len(newid) == 2:
        nextid = nextid[:3] + "000" + newid
    elif len(newid) == 3:
        nextid = nextid[:3] + "00" + newid
    elif len(newid) == 4:
        nextid = nextid[:3] + "0" + newid
    elif len(newid) == 5:
        nextid = nextid[:3] + newid

    mylist[ind] = nextid
    rec = "/".join(mylist)
    with open("id2.txt", "w") as fh:
        fh.write(rec)
    return (nextid)

### Password edit ###

def change_customer_password():
    f1 = open("customer_data.txt", "r")
    f2 = open("customer_data_new.txt", "w")
    userid = input("\nEnter customer id: ")
    pwd = input("Edit customer password: ")
    lines = f1.readlines()
    for line in lines:
        info = line.split("| ")
        id = info[0]
        balance = info[2]
        username = info[3]
        surname = info[4]
        email = info[5]
        city = info [6]
        birth = info[7]

        if userid == id:
            f2=open("customer_data_new.txt", "w")
            f2.write(id+"| "+pwd+"| "+balance+"| "+username+"| "+surname+"| "+email+"| "+city+"| "+birth+"\n")

    f1.close()
    f2.close()
    os.remove("customer_data.txt")
    os.rename("customer_data_new.txt", "customer_data.txt")
    staff_options()    

### Deposit and Withdraw ###

def deposit():
    accId = input("Enter your ID:")
    while True:
        templist = []
        with open("customer_data.txt", "r") as f:
            flg = 0
            for line in f:
                linelist = line.rstrip().split("| ")


                if accId.upper() in linelist[0].upper():
                    print("Your accoint ID ", linelist[0])
                    print("Your current balance: ", linelist[2])
                    Amt=input("Enter an amount: ")
                    bal=linelist[2]
                    newbal = int(bal) + int(Amt)
                    if newbal>100:
                        linelist[2]=str(newbal)
                        print(newbal)
                        flg = 1
                    else:
                        print("Error invalue")
                        flg = 2
                templist.append(linelist)

        if flg == 0: 
           print("Search value invalid!")
        else:
           with open("customer_data.txt", "w") as fileHandle:
               cnt = 0
               while (cnt < len(templist)):
                   linestr = "| ".join(templist[cnt])
                   fileHandle.write(linestr + "\n")
                   cnt += 1

        with open("customer_transactionhistory.txt", "a") as fileHandle:
            fileHandle.write(linelist[0] + "| " + "Current" + "| " + str(Amt) + "| "+(str(datetime.datetime.now())) + "\n")


        ans = input("Do you want to continue (Y/N): ").lower()
        if ans == "y":
           return deposit()
        else:
           if ans == "n":
               return customer_options()

def withdrawal():
    accId = input("Enter your ID:")
    while True:
        templist = []
        with open("customer_data.txt", "r") as f:
            flg = 0
            for line in f:
                linelist = line.rstrip().split("| ")


                if accId.upper() in linelist[0].upper():
                    print("Your account ID", linelist[0])
                    print("Your current balance: ", linelist[2])
                    Amt=input("Enter an amount: ")
                    bal=linelist[2]
                    newbal = int(bal) - int(Amt)
                    if newbal>100:
                        linelist[2]=str(newbal)
                        print(newbal)
                        flg = 1
                    else:
                        print("Error invalue")
                        flg = 2
                templist.append(linelist)

        if flg == 0: 
            print("Search value invalid!")
        else:
            with open("customer_data.txt", "w") as fileHandle:
                cnt = 0
                while (cnt < len(templist)):
                    linestr = "| ".join(templist[cnt])
                    fileHandle.write(linestr + "\n")
                    cnt += 1

        with open("customer_transactionhistory.txt", "a") as fileHandle:
            fileHandle.write(linelist[0] + "| " + "Current" + "| " + str(Amt) + "| " + (str(datetime.datetime.now()))+ "\n")


        ans = input("Do you want to continue (Y/N): ").lower()
        if ans == "y":
            return withdrawal()
        else:
            if ans == "n":
                return customer_options()

def cosBalance():
    pin = input("Please enter your id: ")
    with open("customer_data.txt", "r") as fh:
        lines2 = fh.readlines()
        for line2 in lines2:
            info= line2.split("| ")
            if pin == info[0]:
                id = info[0]
                name = info[3]
                surname = info[4]
                balance = info[2]
                if pin == id:
                    print(f"| User ID:{id}\n| User name:{name}\n| User surname:{surname}\n| User balance:{balance}\n ")
                    customer_options()
                else:
                    print("Wrong user, please try again...")
                    cosBalance()

### CHECK ACCOUNTS ###

def check_staff(): 
    f = open("staff_data.txt", "r")
    file_contents = f.read()
    print("\n| Staff accounts |\n")
    print("| User ID | User password | User name | User surname | User phone number | User adress |")
    print ("\n", file_contents, "\n")
    print("\n\n")
    f.close()
    admin_options()

def check_customer():
    f = open("customer_data.txt", "r")
    file_contents = f.read()
    print("\n| Customer accounts |\n")
    print("| User ID | User password | User name | User surname | User email | User adress |")
    print ("\n", file_contents, "\n")
    print("\n\n")
    f.close()
    staff_options()

## CREATE A NEW ACCOUNT ###

def create_staff():
    database = open("staff_data.txt", "a")
    username = input("Enter staff name: ")
    surname = input("Enter staff surname: ")
    number = input("Enter staff number: ")
    city = input("Enter costumer adress: ")
    password = input("Enter your password: ")
    password1 = input("Confirm password: ")
    userid = getid("STF")

    if password != password1: 
        print("Password does not match, Please try again...")
        create_staff()
    else:
        
        database = open("staff_data.txt","a")
        database.write(userid+"| "+password+"| "+username+"| "+surname+"| "+number+"| "+city+"| "+"\n")
    
     
    database.close()
    print("\n<<< Your account has been created >>>\n")
    print("Hello "+username)
    print("Your password is:"+password)
    print("Your default ID is:" +userid+"\n\n")
    admin_options()

def create_customer():
        db = open("customer_data.txt", "a")
        username = input("Enter customer name: ")
        surname = input("Enter customer surname: ")
        email = input("Enter customer's email: ")
        city = input("Enter customer adress: ")
        data_of_birth = input("Enter customer birthday: ")
        password = input("Enter your password: ")
        password1 = input("Confirm password: ")
        userid = getid2("CCC")
        if password != password1:
            print("Password does not match, Please try again...")

        accType = str(input("Saving or Current: "))

        if accType == "s":
            accType =100
            
        if accType == "c":
            accType =500
            
            
    
        db = open("customer_data.txt","a")
        db.write(userid+"| "+password+"| "+str(accType)+"| "+username+"| "+surname+"| "+email+"| "+city+"| "+data_of_birth+"\n")
        db.close()
        print("<<< Your account has been created >>>\n")
        print("Hello "+username)
        print("Your password is: "+password)
        print("Your default ID is: " +userid+"\n\n")
        staff_options()

### ACCESS ###

def adminaccess():
    print("  <<< Admin access >>>    \n\n")
    loginAdminId = input("Please enter your Id: ")
    loginAdminpassword = input("Please enter your password: ")
    if loginAdminId == adminId and loginAdminpassword == adminpassword:
        admin_options()
    else:
        print("Incorrect Id or password, please try again")
        adminaccess()

def staffaccess():
    userid = input("Enter your ID: ")
    password = input("Enter your password: ")
    fileRead = open("staff_data.txt", "r")
    flag = False
    while True:
        line = fileRead.readline()
        lineLength = len(line)
        if lineLength == 0:
            break
        lineItem = line.split("| ")
        if userid.strip() == lineItem[0] and password.strip() == lineItem[1] :
            print("Hello! ",userid," you have logged in successfully.")
            flag=True
            break
    if flag == False:
        print("The user is not found. Please re-enter your username and password.")
        main()
    
    staff_options()

def customeraccess():
    userid = input("Enter your ID: ")
    password = input("Enter your password: ")
    fileRead = open("customer_data.txt", "r")
    flag = False
    while True:
        line = fileRead.readline()
        lineLength = len(line)
        if lineLength == 0:
            break
        lineItem = line.split("| ")
        if userid.strip() == lineItem[0] and password.strip() == lineItem[1] :
            print("Hello! ",userid," you have logged in successfully.")
            flag = True
            customer_options()
            break
            
    if flag == False:
        print("The user is not found. Please re-enter your username and password.")
        main()

### OPTIONS ###

def main():
    print("   <<< Welcome to Bank >>>\n\n")
    print("1. <<<   Admin menu    >>>")
    print("2. <<<   Staff menu    >>>")
    print("3. <<<  Costumer menu  >>>")
    print("4. <<<      Exit       >>>\n\n")
    while True:
        mainOption = int(input("Please provide option: "))
        if mainOption ==1:
            adminaccess()
            break
        elif mainOption ==2:
            staffaccess()
            break
        elif mainOption ==3:
            customeraccess()
            break
        elif mainOption ==4:
            print("Thanks for visiting!")
            break
        else:
            print("ERROR")
            main()

def admin_options():
    print("   <<<       Welcome to admin menu         >>>\n\n")
    print("1. <<<           Create staff              >>>")
    print("2. <<<      Check all staff accounts       >>>")
    print("3. <<<              Exit                   >>>\n\n")
    
    adminans = input("Please provide option: ")
    if adminans == "1":
        create_staff()
    elif adminans == "2":
        check_staff()
    elif adminans == "3":
        print("Thanks for visiting!")
        main()
    else:
        print("ERROR")
        admin_options()

def staff_options():
    print("   <<<         Welcome to staff menu         >>>\n\n")
    print("1. <<<    Create new account for customer    >>>")
    print("2. <<<      Check all customer account       >>>")
    print("3. <<<       Change customer password        >>>")
    print("4. <<<                 Exit                  >>>\n\n")
    
    staffans = input("Please provide option: ")
    if staffans == "1":
        create_customer()

    elif staffans == "2":
        check_customer()
        
    elif staffans == "3":
        change_customer_password()

    elif staffans == "4":
        print("Thanks for visiting!")
        main()
    else:
        print("ERROR")
        staff_options()

def customer_options():
    print ("   <<<     Welcome to Bank      >>>\n\n")
    print ("1. <<<         Deposit          >>>")
    print ("2. <<<        Withdrawal        >>>")
    print ("3. <<<      Check balance       >>>")
    print ("4. <<<          Exit            >>>\n\n")
    
    
    optcos = input("Please provide option: ")
    if optcos == "1":
        deposit()
    elif optcos == "2":
        withdrawal()
    elif optcos =="3":
        cosBalance()
    elif optcos == "4":
        print("Thanks for visiting!")
        main()
    else:
        print("ERROR")
        customer_options()

main() 