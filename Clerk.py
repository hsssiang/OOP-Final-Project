from People import People

class Clerk(People):
    def __init__(self):
        self.set_account_init ("C0")
        self.set_pwd ("0")
    def Regist(self,new_user, manager, name, gender, birthday, phone_number, id, pws):
        if name == "": return 1
        else: new_user.set_name(name)

        if gender == "": return 1 
        else: new_user.set_sex(gender)

        if birthday == "": return 1 
        else: new_user.set_birth(birthday)

        if phone_number == "": return 1
        else: new_user.set_phone_number ( phone_number )

        output =  new_user.set_account ( manager, id ) 
        if output == 1: #空字串
            return 1
        if output == 2: #帳號已存在
            return 2

        if pws == "": return 1
        else: new_user.set_pwd ( pws )
        return 3
    
    def Display(self,user):
        print ( "[Account]: " + user.get_account())
        print ( "[Name]: " + user.get_name())
        print ( "[Gender]: " + user.get_sex())
        print ( "[Birthday]: " + user.get_birth())
        print ( "[Phone number]: " + user.get_phone_number())
        print ( "[Balance]: " + str(user.get_balance()))
        print ( "-" *20)

    def Modify(self,user,manager,Name, Gender, Birth, Phone, Acc, Pwd):
        self.Display(user)
        while True:    
            print(">> Enter the data you want to modify")
            choice = int(input("[1:name, 2:gender, 3:birthday, 4:phone number, 5:address, 6:e-mail, 7:pwd, 8:acc, 9:exit]: "))
            if choice == 1:
                user.set_name( Name )
            elif choice == 2:
                user.set_gender(Gender)
            elif choice == 3:
                user.set_birth(Birth)
            elif choice == 4:
                user.set_phone_number(Phone)
            elif choice == 7:
                pwd = input("Input your new password: ")
                check_pwd = input("Please confirm your new password: ")
                if( pwd == check_pwd ):
                    user.set_pwd(pwd)
                else:
                    print("The two passwords you entered do not match.\n")
            elif choice == 8:
                user.set_account(manager)
            elif choice == 9:
                print ( "Thank you.\n" )
                break
        return user
    
    def Deposit( self, user, manager, money ):
        if money == "": return False
        auth_dict = manager.get_permission()
        self_auth = auth_dict[user.get_account()]
        if self_auth >= 2:
            user.set_balance ( int(money) )
            return 1
        else:
            return 2
            print("Insufficient Permissions.\n")
    
    def Withdraw(self,user,manager,money):
        if money == "": return False
        auth_dict = manager.get_permission()
        user_auth = auth_dict[user.get_account()]
        if user_auth >= 3:
            takeout = int(money)
            if user.get_balance() < takeout:
                return 2
            else:
                user.set_balance ( -takeout )
                return 1
        else:
            return 3
    
    def Check(self,user,manager):
        user_auth = manager.get_permission_dict([user.get_name()]) 
        if user_auth >= 1:
            print ( "Hello! + "  + user.get_name() ) 
            print("Your current balance is:",user.get_balance())
        print ( "Thank you.\n" )
        return user
    
    def Transfer(self,user,manager, acc, money):
        other_acc = acc
        user_list = manager.get_member_list()
        for other_user in user_list:
            if other_user.get_account() == other_acc:
                amount = int(money)
                auth_dict = manager.get_permission()
                user_auth = auth_dict[user.get_account()]
                other_auth = auth_dict[other_acc]
                if user_auth == 3 and other_auth != 0 :
                    if user.get_balance() < amount:
                        return 2 #轉帳失敗
                    else:
                        user.set_balance ( -amount )
                        other_user.set_balance ( amount )
                        return 1
        return 3 #找不到account
        
