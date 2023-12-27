import tkinter as tk
from tkinter import messagebox
from Manager import Manager
from User import User
from Clerk import Clerk

class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Management System")
        self.geometry("400x300")

        self.manager = Manager()
        self.clerk = Clerk()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="User Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.identity_label = tk.Label(self, text="Select your identity:")
        self.identity_label.pack()

        self.identity_var = tk.StringVar()
        self.identity_var.set("User")

        self.identity_menu = tk.OptionMenu(self, self.identity_var, "User", "Manager", "Clerk")
        self.identity_menu.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack()

    def login(self):
        identity = self.identity_var.get()

        if identity == "User":
            self.show_user_menu()
        elif identity == "Manager":
            self.show_manager_menu()
        elif identity == "Clerk":
            self.show_clerk_menu()

    def show_user_menu(self):
        user_menu = tk.Toplevel(self)
        user_menu.title("User Menu")
        user_menu.geometry("300x200")

        user_label = tk.Label(user_menu, text="Welcome, User!", font=("Helvetica", 14))
        user_label.pack(pady=10)

        deposit_button = tk.Button(user_menu, text="Deposit", command=self.deposit)
        deposit_button.pack(pady=5)

        withdraw_button = tk.Button(user_menu, text="Withdraw", command=self.withdraw)
        withdraw_button.pack(pady=5)

        check_balance_button = tk.Button(user_menu, text="Check Balance", command=self.check_balance)
        check_balance_button.pack(pady=5)

        transfer_button = tk.Button(user_menu, text="Transfer", command=self.transfer)
        transfer_button.pack(pady=5)

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