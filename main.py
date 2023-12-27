from Manager import Manager
from User import User
from Clerk import Clerk

def log_in(manager):
    try:
        op = int(float(input("[1:Modify, 2:Deposit, 3:Withdraw, 4:Check, 5:Transfer, 6:Exit]: ")))
    except ValueError:
        print("Input value error")
    if op == 1:
        user.modify(manager)
    elif op == 2:
        user.deposit(manager)
        print("Deposit Completed.\n")
    elif op == 3:
        user.withdraw(manager)
    elif op == 4:
        user.check()
    elif op == 5:
        user.transfer(manager)
    else:
        print("Exit sucessfully.\n")
        return False
    return True

# main
counter = 1
manager = Manager()#初始帳秘：M0 , 0
clerk = Clerk()#初始帳秘：C0 , 0

while True:
    print ( ">>Please enter your identity: " )
    choice = int(input( "[1:User, 2:Manager ,3:Exit] :" ))
    if choice == 1:
        # user
        while True:
            print ( ">>Which function do you want to choose?" )
            try:
                op = int(input("Choose function [1:Creat, 2:Log in , 3:Return]: "))
            except ValueError:
                print("ERROR: Input value error, please do again.\n")
                continue
            if op == 1:
                user = User()
                if user.regist(manager):       # 回傳 True 的話，才add
                    manager.set_permission(user.get_account(),3)  #manager更新資料
                    manager.add_member(user) #user list新增user 
                    print("Registraion Completed!\n")
                else :
                    print("You can't enter empty string.\n")
            elif op == 2:
                user_list = manager.get_member_list()
                account = input("Input your account: ")
                pwd = input("Inpur your password: ")
                flag = True
                for user in user_list:
                    if account == user.get_account():
                        if pwd == user.get_pwd():
                            print(f"Hello, {user.get_name()}")
                            while True:
                                if log_in(manager) == False: 
                                    flag = False
                                    break
                        else:
                            print("Wrong password. \n")
                            flag = False
                            break
                if flag == False: continue
                print("Account not found!\n")
            else:
                break
    elif choice == 2:
        # manager / clerk
        acc = input("Accouct: ")
        pwd = input("Password: ")
        if ( acc == manager.get_account() and pwd == manager.get_pwd() ):
            while True:
                try:
                    op = int(input(">>Choose function [1:Display, 2:Edit_permission, 3:Display_member, 4:Exit]: "))
                except ValueError:
                    print("ERROR: Input value error, please do again.\n")
                    continue
                if op == 1:
                    manager.Display_permission()
                elif op == 2:
                    manager.Edit_permission()
                elif op == 3:
                    manager.Display_member()
                else:
                    print("Exit sucessfully. ")
                    break
        elif ( acc == clerk.get_account() and pwd == clerk.get_pwd() ):
            while True:
                retry = 0
                new_acc_op = input ("If you want to create a new account, please enter 'New'\nIf you want to use an existing account, please enter 'Old'\nIf you want to exit, please enter 'Exit'\n:")
                if new_acc_op == "New":
                    customer = User()
                    if clerk.Regist(customer , manager) == False:
                        print("No empty.")
                        print("Re choose.\n")
                        continue
                    manager.set_permission(customer.get_account(),3)  #manager更新資料
                    manager.add_member(customer) #user list新增user 
                    print("Registraion Completed!\n")
                elif new_acc_op == "Old":
                    user_acc = input("Please input Your account: ")
                    user_list = manager.get_member_list()
                    customer = User()
                    for user in user_list:
                        if user.get_account() == user_acc:
                            customer = user
                            retry = 1
                            break
                    if not retry:
                        break
                    while 1:
                        op = int(input(">> Function(1:Display, 2:Modify, 3:Deposit, 4:Withdraw, 5.Check, 6.Transfer other:Exit): "))
                        if op == 1:    
                            clerk.Display(customer)
                        elif op == 2:
                            clerk.Modify(customer,manager)
                        elif op == 3:
                            clerk.Deposit(customer,manager)
                        elif op == 4:
                            clerk.Withdraw(customer,manager)
                        elif op == 5:
                            clerk.Check(customer)
                        elif op == 6:
                            clerk.Transfer(customer,manager)
                        else:
                            break
                elif new_acc_op == "Exit":
                    print("Exit sucessfully. \n")
                    break
    else:
        break
