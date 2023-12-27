class People:
    def __init__(
        self,
        account=None,
        pwd=None,
        name=None,
        sex=None,
        birth=None,
        phone_number=None,
    ):
        self.__account = account
        self.__pwd = pwd
        self.__name = name
        self.__sex = sex
        self.__birth = birth
        self.__phone_number = phone_number
    
    def get_account(self): return self.__account
    def get_pwd(self): return self.__pwd
    def get_name(self): return self.__name
    def get_sex(self): return self.__sex
    def get_birth(self): return self.__birth
    def get_phone_number(self): return self.__phone_number

    def set_pwd(self, pwd): self.__pwd = pwd
    def set_name(self, name): self.__name = name   
    def set_sex(self, gender): self.__sex = gender
    def set_birth(self, birth): self.__birth = birth
    def set_phone_number(self,phone_number): self.__phone_number = phone_number

    def set_account(self ,manager, Acc):
        flag = False
        while flag == False:
            if Acc == "":
                return False
            account_list = [x.get_account() for x in manager.get_member_list()]
            if Acc in account_list:
                flag = 2
                return 2 #已存在，失敗
            else:
                self.__account = Acc
                flag = 3 #成功
                return 3
    
    def set_account_init(self , account):
        self.__account = account
        