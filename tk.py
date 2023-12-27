import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Manager import Manager
from User import User
from Clerk import Clerk

widget_set=[]

class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Online Bank System")
        self.geometry("400x300")

        self.manager = Manager()
        self.clerk = Clerk()

        self.create_widgets(self.manager, self.clerk)

    def create_widgets(self, manager, clerk):
        self.label = tk.Label(self, text="User Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.identity_label = tk.Label(self, text="Select your identity:")
        self.identity_label.pack()

        self.identity_var = tk.StringVar()
        self.identity_var.set("User")

        self.identity_menu = tk.OptionMenu(self, self.identity_var, "User", "Manager", "Clerk")
        self.identity_menu.pack()

        self.login_button = tk.Button(self, text="OK", command=lambda: self.OK(manager, clerk))
        self.login_button.pack(pady=10)

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack()

    def OK(self, manager, clerk):
        self.iconify()
        identity = self.identity_var.get()
        if identity == "User":
            self.Function(manager)
        # elif identity == "Manager":
        #     self.show_manager_menu()
        # elif identity == "Clerk":
        #     self.show_clerk_menu()

    def Function(self, manager):
        user_screen = tk.Toplevel(self)
        user_screen.title("Function")
        user_screen.geometry("350x250")

        user_label = tk.Label(user_screen, text="Please Enter Your account/pwd: ", font=("Helvetica", 10))
        user_label.pack(pady=5)

        user_label = tk.Label(user_screen, text="Account:")
        user_label.pack()
        Account = tk.Entry(user_screen)
        Account.pack()
        user_label = tk.Label(user_screen, text="Password: ")
        user_label.pack()
        Pwd = tk.Entry(user_screen)
        Pwd.pack()

        self.Login_button = tk.Button(user_screen, text="Login", command=lambda: self.Check(manager, Account.get(), Pwd.get()))
        self.Login_button.pack(pady=10)

        self.creat_button = tk.Button(user_screen, text="Creat", command=lambda: self.Creat(manager))
        self.creat_button.pack(pady=10)


    def Check(self, manager, account, pwd):
        user_list = manager.get_member_list()
        flag = True
        for user in user_list:
            if account == user.get_account():
                if pwd == user.get_pwd():
                    user_menu = tk.Toplevel(self)
                    user_menu.title("User Menu")
                    user_menu.geometry("300x200")

                    user_label = tk.Label(user_menu, text="Hello,", command = self.Login)
                    user_label.pack(pady=10)
                    while True:
                        if user.log_in(manager) == False: 
                            flag = False
                            break
                else:
                    wrong = tk.Toplevel(self)
                    wrong.title("!")
                    wrong.geometry("200x100")

                    user_label = tk.Label(wrong, text="Wrong password")
                    user_label.pack(pady=10)
                    flag = False
                    break
        
        print("Account not found!\n")

    def Creat(self, manager):
        user_creat = tk.Toplevel(self)
        user_creat.title("New User information")
        user_creat.geometry("300x400")

        frame1 = ttk.Frame(user_creat)
        frame1.pack(pady=10)
        user_label = tk.Label(frame1, text="Name: ")
        user_label.pack(side = "left")
        name = tk.Entry(frame1)
        name.pack(side = "left")

        frame2 = ttk.Frame(user_creat)
        frame2.pack(pady=10)
        user_label = tk.Label(frame2, text="Gender: ")
        user_label.pack(side = "left")
        gender = tk.Entry(frame2)
        gender.pack(side = "left")

        frame3 = ttk.Frame(user_creat)
        frame3.pack(pady=10)
        user_label = tk.Label(frame3, text="BirthDay: ")
        user_label.pack(side = "left")
        birth = tk.Entry(frame3)
        birth.pack(side = "left")

        frame4 = ttk.Frame(user_creat)
        frame4.pack(pady=10)
        user_label = tk.Label(frame4, text="Phone Number: ")
        user_label.pack(side = "left")
        phone = tk.Entry(frame4)
        phone.pack(side = "left")

        frame5 = ttk.Frame(user_creat)
        frame5.pack(pady=10)
        user_label = tk.Label(frame5, text="Account: ")
        user_label.pack(side = "left")
        acc = tk.Entry(frame5)
        acc.pack(side = "left")

        frame6 = ttk.Frame(user_creat)
        frame6.pack(pady=10)
        user_label = tk.Label(frame6, text="Password: ")
        user_label.pack(side = "left")
        pwd = tk.Entry(frame6)
        pwd.pack(side = "left")

        self.creat_button = tk.Button(user_creat, text="Done!", command=lambda: self.Done(manager, name.get(), gender.get(), birth.get(), phone.get(), acc.get(), pwd.get()))
        self.creat_button.pack(pady=10)

    def Done(self, manager, name, gender, birth, phone, acc, pwd ):
        user_done = tk.Toplevel(self)
        user_done.title("complete")
        user_done.geometry("200x100")

        user = User()
        if user.regist(manager, name, gender, birth, phone, acc, pwd):
            manager.set_permission(user.get_account(),3)
            manager.add_member(user)
            user_label1 = tk.Label(user_done, text="Registraion Completed!")
            user_label1.pack()
        else :
            user_label1 = tk.Label(user_done, text="You can't enter empty string.")
            user_label1.pack()

    def Login(self):
        print("done")

        # deposit_button = tk.Button(user_menu, text="Deposit", command=self.deposit)
        # deposit_button.pack(pady=5)

        # withdraw_button = tk.Button(user_menu, text="Withdraw", command=self.withdraw)
        # withdraw_button.pack(pady=5)

        # check_balance_button = tk.Button(user_menu, text="Check Balance", command=self.check_balance)
        # check_balance_button.pack(pady=5)

        # transfer_button = tk.Button(user_menu, text="Transfer", command=self.transfer)
        # transfer_button.pack(pady=5)

    def show_manager_menu(self):
        manager_menu = tk.Toplevel(self)
        manager_menu.title("Manager Menu")
        manager_menu.geometry("300x200")

        manager_label = tk.Label(manager_menu, text="Welcome, Manager!", font=("Helvetica", 14))
        manager_label.pack(pady=10)

        display_permission_button = tk.Button(manager_menu, text="Display Permission", command=self.display_permission)
        display_permission_button.pack(pady=5)

        edit_permission_button = tk.Button(manager_menu, text="Edit Permission", command=self.edit_permission)
        edit_permission_button.pack(pady=5)

        display_member_button = tk.Button(manager_menu, text="Display Member", command=self.display_member)
        display_member_button.pack(pady=5)

    def show_clerk_menu(self):
        clerk_menu = tk.Toplevel(self)
        clerk_menu.title("Clerk Menu")
        clerk_menu.geometry("300x200")

        clerk_label = tk.Label(clerk_menu, text="Welcome, Clerk!", font=("Helvetica", 14))
        clerk_label.pack(pady=10)

        create_account_button = tk.Button(clerk_menu, text="Create Account", command=self.create_account)
        create_account_button.pack(pady=5)

        use_existing_account_button = tk.Button(clerk_menu, text="Use Existing Account", command=self.use_existing_account)
        use_existing_account_button.pack(pady=5)

    def deposit(self):
        messagebox.showinfo("Deposit", "Deposit functionality will be implemented here.")

    def withdraw(self):
        messagebox.showinfo("Withdraw", "Withdraw functionality will be implemented here.")

    def check_balance(self):
        messagebox.showinfo("Check Balance", "Check Balance functionality will be implemented here.")

    def transfer(self):
        messagebox.showinfo("Transfer", "Transfer functionality will be implemented here.")

    def display_permission(self):
        messagebox.showinfo("Display Permission", "Display Permission functionality will be implemented here.")

    def edit_permission(self):
        messagebox.showinfo("Edit Permission", "Edit Permission functionality will be implemented here.")

    def display_member(self):
        messagebox.showinfo("Display Member", "Display Member functionality will be implemented here.")

    def create_account(self):
        messagebox.showinfo("Create Account", "Create Account functionality will be implemented here.")

    def use_existing_account(self):
        messagebox.showinfo("Use Existing Account", "Use Existing Account functionality will be implemented here.")

if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()