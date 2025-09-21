# context
# 1) Bank Account
# 2) Deposit monney
# 3) Withdraw money
# 4) Details
# 5) Update Detail
# 6) Delete The Account 

# importing some useful libraries(usefull for interact with 
# json(used as database) file)
import json
import random
import string
from pathlib import Path

# creating an object
class Bank:
    # create a database path
    database = 'data.json'
    # create a dummy data (copy of json file's data)
    data = []

    # exception handaling
    try:
        # this check data.json is existed or not.
        if Path(database).exists():
            # open json file 
            with open(database) as fs:
                # copy data from json file to dummy data
                data = json.loads(fs.read())
        else:
            print("no such file is existed.")

    except Exception as err:
        print(f"an exception occured as {err}")

    # create an static method named update
    @classmethod
    def __update(cls):
        with open(cls.database , "w") as fs:
            fs.write(json.dumps(Bank.data))

    # it is private class method which generate rendom account number
    @classmethod
    def __account_generate(cls):
        #  3 random Alphabets
        alpha = random.choices(string.ascii_letters , k = 3)
        #  3 random numbers
        num = random.choices(string.digits , k = 3)
        # 1 special character
        spchar = random.choices("!@#$%^&*()" , k = 1)
        # appending this all stuff
        id = alpha + num + spchar
        # this is use for suffling alpha num and spchar
        random.shuffle(id)
        # this convert id list into string
        return "".join(id)

    def create_account(self):
        info = {
            "name" : input("Tell Your Name :-") , 
            "age" : int(input("Tell Your Age :-")) , 
            "email" : input("Tell Your Email :-") , 
            "pin" : int(input("Tell Your 4 Number Pin :-")) ,
            "account_no." : Bank.__account_generate() , 
            "balance" : 0 
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("sorry you can't create your account.")
        else:
            print("account has been successfully created.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number.")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your account pin : "))
        # it cut only 1 user part which is needed
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == pin]
        #check for user is existed or not
        if userdata == False:
            print("sorry user dosn't existed")
        else:
            amount = int(input("Enter the Deposit Amount : "))
            if amount > 10000 or amount < 0:
                print("sorry , you can't deposit 10000+ amount.")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount is deposited successfully")

    def withdrawmoney(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your account pin : "))
        # it cut only 1 user part which is needed
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == pin]
        #check for user is existed or not
        if userdata == False:
            print("sorry user dosn't existed")
        else:
            amount = int(input("Enter the Withdraw Amount : "))
            if userdata[0]['balance'] < amount:
                print("sorry , you can't Withdraw because your balance is too low.")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount is Withdrew successfully")


    def showdetails(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your account pin : "))
        # it cut only 1 user part which is needed
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("sorry user dosn't existed")
        else:
            print("your information are \n\n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetail(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your account pin : "))
        
        # it cut only 1 user part which is needed
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("sorry user dosn't existed")
        else:
            print("you cann't change age , account number , balance")
            print("fill details for change or leave it empty if no change")
            print("Press enter for skip the field ")
            new_data = {
                'name' : input("tell your updated name : ") ,
                'email' : input("tell your uodated email: ") , 
                'pin' : input("Tell your new pin : ")
            }
            if new_data['name'] == "":
                new_data['name'] = userdata[0]['name']
            if new_data['email'] == "":
                new_data['email'] = userdata[0]['email']
            if new_data['pin'] == "":
                new_data['pin'] = userdata[0]['pin']


            new_data['age'] = userdata[0]['age']
            new_data['account_no.'] = userdata[0]['account_no.']
            new_data['balance'] = userdata[0]['balance']


            if type(new_data['pin']) == str:
                new_data['pin'] = int(new_data['pin'])


            for i in new_data:
                if new_data[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = new_data[i]
            Bank.__update()
            print("Update detail successfully....") 


    def deleteuser(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your account pin : "))
        
        # it cut only 1 user part which is needed
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("sorry no such data existed")
        else:
            check = input("press Y for actually delete the account or press N : ")
            if check == 'N' or check == 'n':
                print("bypassed")
            if check == 'Y' or check == 'y':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleting successfully")
                Bank.__update()

print("Press 1 For Creating An Account.") 
print("Press 2 For Deposititing The Monney In The Bank.") 
print("Press 3 For Withdrawing The Monney.") 
print("Press 4 For Details.") 
print("Press 5 For Updating The Details.") 
print("Press 6 For Deleting Your Account.") 
user = Bank()

check = int(input("Tell Your Response :- "))

if check == 1:
    user.create_account()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetail()

if check == 6:
    user.deleteuser()