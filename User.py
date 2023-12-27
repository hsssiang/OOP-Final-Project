from People import People

class User(People):
    def __init__(self=None,account=None,pwd=None,name=None,sex=None,birth=None,phone_number=None,balance=0):
        super().__init__(account,pwd,name,sex,birth,phone_number)
        self.__balance = int(balance)
        
    def set_balance(self, balance):
        self.__balance += balance
    
    def get_balance(self):
        return self.__balance
    
    def regist(self, manager, Name, Gender, Birth, Phone, Acc, Pwd):
        if Name == "": return 1 
        else: self.set_name(Name)

        if Gender == "": return 1
        else: self.set_sex(Gender)

        if Birth == "": return 1
        else: self.set_birth(Birth)

        if Phone == "": return 1
        else: self.set_phone_number ( Phone )

        done = self.set_account ( manager, Acc )
        if done == False: #空字串
            return 1
        if done == 2: #帳號已存在
            return 2

        pwd = Pwd
        if pwd == "": return 1
        else: self.set_pwd ( pwd )
        return 3

    def modify(self, manager, Name, Gender, Birth, Phone, Acc, Pwd):
        print("1 for name / 2 for gender / 3 for birthday / 4 for phone number / 5 for password / 6 for account / 7 for exit")
        choice = int(input(">> Enter the data you want to modify: "))
        if choice == 1:
            self.set_name ( Name )
        elif choice == 2:
            self.set_sex ( input("Input your new gender: ") )
        elif choice == 3:
            self.set_birth ( input("Input your new birthday: ") )
        elif choice == 4:
            self.set_phone_number ( input("Input your new phone number: ") )
        elif choice == 5:
            pwd = input("Input your new password: ")
            check_pwd = input("Please confirm your new password: ")
            if( pwd == check_pwd ):
                self.set_pwd ( pwd )
            else:
                print("The two passwords you entered do not match. Failed\n")
                return
        elif choice == 6:
            self.set_account ( manager )
        print("Modify Completed!\n")

        
    def deposit(self, manager, money):
        if money == "": return False
        auth_dict = manager.get_permission()
        self_auth = auth_dict[self.get_account()]
        if self_auth >= 2:
            self.set_balance ( int(money) )
            return 1
        else:
            return 2
            print("Insufficient Permissions.\n")

    def withdraw(self, manager, money):
        if money == "": return False
        auth_dict = manager.get_permission()
        self_auth = auth_dict[self.get_account()]
        if self_auth == 3:
            take = int(money)
            if self.get_balance() < take:
                return 2
            else:
                self.set_balance ( -take )
                return 1
        else:
            return 3

    def check(self):
        self
        print("Name: ", self.get_name(), "\tYour balance: ", self.get_balance())

    def transfer(self, manager, acc, money):
        other_acc = acc
        user_list = manager.get_member_list()
        flag = True # 跳出下面的for迴圈
        for user in user_list:
            if user.get_account() == other_acc:
                amount = int(money)
                auth_dict = manager.get_permission()
                self_auth = auth_dict[self.get_account()]
                other_auth = auth_dict[other_acc]
                if self_auth == 3 and other_auth != 0 :
                    if self.get_balance() < amount:
                        flag = False
                        return 2 #轉帳失敗
                        break
                    else:
                        self.set_balance ( -amount )
                        user.set_balance ( amount )
                        return 1
                        flag = False #轉帳成功
                        break
        return 3 #找不到account
