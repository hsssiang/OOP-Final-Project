from People import People

class Manager(People):
    def __init__(self):
        self.set_account_init ("M0")
        self.set_pwd ("0")
        self.__permission_dict = {} #存放使用者權限 {string : int}
        self.__member_list = [] #裡面放User Object
    # set   
    def set_permission(self, acc, level):
        self.__permission_dict[acc] = level

    def add_member(self, user):
        self.__member_list.append(user) 
    # get  
    def get_permission(self):
        return self.__permission_dict
    def get_member_list(self):
        return self.__member_list
    
    # functions
    def Display_permission(self):
        print("account\t\tpermission level")
        for keys, values in self.__permission_dict.items():
            print(f"{keys}\t\t{values}")

    def Display_member(self):
        for user in self.__member_list:
            print()
            print ( f"[Account]: \t\t{user.get_account()}")
            print ( f"[Name]: \t\t{user.get_name()}")
            print ( f"[Gender]: \t\t{user.get_sex()}")
            print ( f"[Birthday]: \t\t{user.get_sex()}")
            print ( f"[Phone number]: \t{user.get_phone_number()}")
            print ( f"[Balance]: \t\t{user.get_balance()}")
            print ( "-"*30)

    def Edit_permission(self):
        self.Display_permission()
        acc = input("Please enter the person you want to modify (account): ")
        for user in self.__member_list:
            if acc == user.get_account():
                level =  int(input("Please enter new permission level(1~3): "))
                if level>=1 and level<=3:
                    self.__permission_dict[acc] = level
                    break
                print("Wrong permission level.n")
            else:
                print("Account not found.\n")
                break