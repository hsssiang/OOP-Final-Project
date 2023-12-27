import tkinter as tk
from tk import ttk
from People import People
from Manager import Manager
from User import User
from Clerk import Clerk
from tk import messagebox
from PIL import Image, ImageTk,ImageOps
import matplotlib.pyplot as plt



widget_set=[]
manager = Manager()
clerk = Clerk()
db = open('DB.txt', 'r')
obj_num = int(db.readline())
for i in range(obj_num):
    accuunt = db.readline().strip()
    pwd = db.readline().strip()
    name = db.readline().strip()
    gender = db.readline().strip()
    birth = db.readline().strip()
    phone = db.readline().strip()
    balance = db.readline().strip()
    permis = int(db.readline().strip())
    user_db = User ( accuunt, pwd, name, gender, birth, phone, balance )
    manager.set_permission(user_db.get_account(),permis)
    manager.add_member(user_db)
db.close()

def init():
    global widget_set
    for element in widget_set:
        element.destroy()
    title_label = tk.Label(win, text = "Online Bank System")
    title_label.grid(column = 0, row = 1)
    user_button = tk.Button(win, text = "User" , command = user_choice)
    user_button.grid(column=0, row=2, padx=210, pady = 5)
    manager_button = tk.Button(win, text = "Manager", command = manager_login)
    manager_button.grid(column=0, row=3, padx=210, pady = 5)
    clerk_button = tk.Button(win, text = "Clerk" , command = clerk_login)
    clerk_button.grid(column=0, row=4, padx=210, pady = 5)
    exit_button = tk.Button(win, text = "Exit" , command = safe_exit)
    exit_button.grid(column=0, row=5, padx=210, pady = 5)
    widget_set=[user_button,manager_button,clerk_button,exit_button,title_label]

def safe_exit():
    db = open('DB.txt', 'w')
    length = len(manager.get_member_list())
    db.writelines(str(length))
    db.writelines("\n")
    for i in manager.get_member_list():
        accuunt = i.get_account()
        db.writelines(accuunt)
        db.writelines("\n")
        pwd = i.get_pwd()
        db.writelines(pwd)
        db.writelines("\n")
        name = i.get_name()
        db.writelines(name)
        db.writelines("\n")
        gender = i.get_sex()
        db.writelines(gender)
        db.writelines("\n")
        birth = i.get_birth()
        db.writelines(birth)
        db.writelines("\n")
        phone = i.get_phone_number()
        db.writelines(phone)
        db.writelines("\n")
        balance = i.get_balance()
        db.writelines(str(balance))
        db.writelines("\n")
        permis = manager.get_permission()[accuunt]
        db.writelines(str(permis))
        db.writelines("\n")
    db.close()
    win.destroy()

def user_choice():
    global widget_set
    for element in widget_set:
        element.destroy()

    login_button = tk.Button(win, text = "Login", font=("Helvetica", 14), command = user_login, )
    login_button.grid(column=0, row=0, padx = 210, pady=30)
    register_button = tk.Button(win, text = "Registration", command = user_registration)
    register_button.grid(column=0, row=1, padx = 210)
    back_button = tk.Button(win, text = "Exit", command = init)
    back_button.grid(column=0, row=3, padx = 210, pady=10)
    widget_set=[register_button,login_button,back_button]

def user_registration():
    global widget_set
    for element in widget_set:
        element.destroy()
    
    space1 = tk.Label(win, text = " ")
    space1.grid(column=0, row=0, padx = 50)
    name_label = tk.Label(win, text = "Your name: ")
    name_label.grid(column = 1, row = 0, sticky = tk.E)
    name_entry = tk.Entry(win)
    name_entry.grid(column = 2, row = 0, sticky = tk.W)

    space1.grid(column=0, row=1, padx = 50)
    gender_label = tk.Label(win, text = "Your gender: ")
    gender_label.grid(column = 1, row = 1, sticky = tk.E)
    gender_entry = tk.Entry(win)
    gender_entry.grid(column = 2, row = 1, sticky = tk.W)

    space1.grid(column=0, row=2, padx = 50)
    birthday_label = tk.Label(win, text = "Your birthday: ")
    birthday_label.grid(column = 1, row = 2, sticky = tk.E)
    birthday_entry = tk.Entry(win)
    birthday_entry.grid(column = 2, row = 2, sticky = tk.W)

    space1.grid(column=0, row=3, padx = 50)
    phone_number_label = tk.Label(win, text = "Your phone number: ")
    phone_number_label.grid(column = 1, row = 3, sticky = tk.E)
    phone_number_entry = tk.Entry(win)
    phone_number_entry.grid(column = 2, row = 3, sticky = tk.W)
    
    space1.grid(column=0, row=4, padx = 50)
    id_label = tk.Label(win, text = "Your ID: ")
    id_label.grid(column = 1, row = 4, sticky = tk.E)
    id_entry = tk.Entry(win)
    id_entry.grid(column = 2, row = 4, sticky = tk.W)

    space1.grid(column=0, row=5, padx = 50)
    pws_label = tk.Label(win, text = "Your Password: ")
    pws_label.grid(column = 1, row = 5, sticky = tk.E)
    pws_entry = tk.Entry(win)
    pws_entry.grid(column = 2, row = 5, sticky = tk.W)
    
    creat_button = tk.Button(win, text="OK!", command=lambda: success(manager, name_entry.get(), gender_entry.get(), birthday_entry.get(), phone_number_entry.get(), id_entry.get(), pws_entry.get()))
    creat_button.grid(column = 2, row = 6)

    widget_set=[space1, creat_button, id_label,id_entry,pws_label,pws_entry,name_label,name_entry,gender_label,gender_entry,birthday_label,birthday_entry,phone_number_label,phone_number_entry]

    def success(manager, name, gender, birth, phone, acc, pwd ):

        user = User()
        done = user.regist(manager, name, gender, birth, phone, acc, pwd)
        if done == 1:
            messagebox.showerror('showerror', "ERROR: Can't enter empty string.")
        if done == 2:
            messagebox.showerror('showerror', "ERROR: Account existed!.")
        if done == 3:
            manager.set_permission(user.get_account(),3)
            manager.add_member(user)
            messagebox.showinfo('showinfo', "Registraion Completed!")
        user_choice()


def user_login():
    global widget_set
    for element in widget_set:
        element.destroy()

    space1 = tk.Label(win, text = " ")
    space1.grid(column=0, row=2, padx = 70, pady = 30)

    id_label = tk.Label(win, text = "ID: ")
    id_label.grid(column = 1, row = 3, pady=10, sticky = tk.E)
    id_entry= tk.Entry(win)
    id_entry.grid(column = 2, row = 3, pady=10, sticky = tk.W)

    space1.grid(column=0, row=1, padx = 60, pady = 10)
    pwd_label = tk.Label(win, text = "Password: ")
    pwd_label.grid(column = 1, row = 4, sticky = tk.E)
    pwd_entry = tk.Entry(win)
    pwd_entry.grid(column = 2, row = 4, sticky = tk.W)

    ok = tk.Button(win, text='OK!', command=lambda: succ_or_fail(id_entry.get(), pwd_entry.get()))
    ok.grid(column = 2, row = 5, pady = 10)

    widget_set = [space1, id_label, id_entry, pwd_label, pwd_entry, ok]

def succ_or_fail(id, pwd):
    global widget_set
    for element in widget_set:
        element.destroy()

    user_list = manager.get_member_list()
    for user in user_list:
        if id == "" or pwd == "":
            messagebox.showerror('showerror', 'ERROR: Syntax Error，Click and back to menu')
            user_choice()
            return
        elif id == user.get_account():
            if pwd == user.get_pwd():
                user_function(user)
                return
            else:
                messagebox.showerror('showerror', 'ERROR: Wrong Password，Click and back to menu')
                user_login()
                return

    messagebox.showerror('showerror', 'ERROR: Account Not Exist，Click and back to menu')
    user_login()
    

def user_function(user):
    global widget_set
    for element in widget_set:
        element.destroy()

    label = tk.Label(win, text = f"Hello, {user.get_name()}")
    label.grid(column = 1, row = 0)

    transfer_button = tk.Button(win, text = "Transfer" , command = lambda: user_transfer(user))
    transfer_button.grid(column=0, row=1, padx=10, pady=10)
    check_button = tk.Button(win, text = "Check" , command = lambda: user_check(user))
    check_button.grid(column=1, row=1, padx=10, pady=10)
    deposit_button = tk.Button(win, text = "Deposit" , command = lambda: user_deposit(user))
    deposit_button.grid(column=0, row=2, padx=10, pady=10)
    modify_button = tk.Button(win, text = "Modify" , command = lambda: user_modify(user))
    modify_button.grid(column=1, row=2, padx=10, pady=10)
    withdraw_button = tk.Button(win, text = "Withdraw" , command = lambda: user_withdraw(user))
    withdraw_button.grid(column=0, row=3, padx=10, pady=10)
    exit_button = tk.Button(win, text = "Exit" , command = init)
    exit_button.grid(column=1, row=3, padx=10, pady=10)

    widget_set = [label, transfer_button, check_button, deposit_button, modify_button, withdraw_button, exit_button]

#------Transfer---------------------------------------------------------------------------------------
    
def user_transfer(user):
    global widget_set
    for element in widget_set:
        element.destroy()

    transfer_to_id_label = tk.Label(win, text = "The ID you want to transfer")
    transfer_to_id_label.grid(column = 0, row = 0, padx=10, pady=10)
    transfer_to_id_entry= tk.Entry(win)
    transfer_to_id_entry.grid(column = 1, row = 0)

    transfer_money_label = tk.Label(win, text = "Transfer money")
    transfer_money_label.grid(column = 0, row = 1, padx=10, pady=10)
    transfer_money_entry= tk.Entry(win)
    transfer_money_entry.grid(column = 1, row = 1)

    ok = tk.Button(win, text='OK!', command=lambda: Trans(user, transfer_to_id_entry.get(), transfer_money_entry.get()))
    ok.grid(column = 1, row = 2)

    widget_set = [transfer_to_id_label, transfer_to_id_entry, transfer_money_label, transfer_money_entry, ok]

def Trans(user, id, money):
    if id == "" or money == "":
        messagebox.showerror('showerror', 'Syntax Error')
        user_function(user)
        return

    done = user.transfer(manager, id ,money)
    if done == 1:
        messagebox.showinfo('showinfo', 'Transfer successed')
        user_function(user)
    elif done == 2:
        messagebox.showerror('showerror', 'ERROR: Balance is insufficient')
        user_function(user)
    elif done == 3:
        messagebox.showerror('showerror', 'ERROR: Account Not Found')
        user_function(user)


#----check-------------------------------------------------------------------------------------------

def user_check(user):
    global widget_set
    for element in widget_set:
        element.destroy()

    user_c = tk.Toplevel()
    user_c.title("information")
    user_c.geometry("400x200")

    name_label = tk.Label(user_c, text = f"Name: {user.get_name()}")
    name_label.grid(column = 0, row = 0, padx=10, pady=10, sticky = tk.E)
    balance_label = tk.Label(user_c, text = f"Balance: {user.get_balance()}")
    balance_label.grid(column = 0, row = 1, padx=10, pady=10, sticky = tk.E)

    ok = tk.Button(user_c, text='OK!', command=lambda: user_function(user))
    ok.grid(column = 1, row = 2)

    widget_set = [user_c]

#------Deposit-----------------------------------------------------------------------------------------

def user_deposit(user):
    global widget_set
    for element in widget_set:
        element.destroy()

    deposit_money_label = tk.Label(win, text = "How much you want to deopsit: ")
    deposit_money_label.grid(column = 0, row = 0, padx=10, pady=10)
    deposit_money_entry = tk.Entry(win)
    deposit_money_entry.grid(column = 1, row = 0)

    ok = tk.Button(win, text='OK!', command=lambda:user_depo(user, deposit_money_entry.get()))
    ok.grid(column = 1, row = 1, padx = 80)
    
    widget_set=[deposit_money_label, deposit_money_entry, ok]

def user_depo(user, money):

    done = user.deposit(manager, money)
    if done == False:
        messagebox.showerror('showerror', 'ERROR: Syntax Error，Click and back to menu')
        user_function(user)
    if done == 1:
        messagebox.showinfo('showinfo', 'Deposit Successed，Click and back to menu')
        user_function(user)
    if done == 2:
        messagebox.showerror('showerror', 'ERROR: Insufficient Permission，Click and back to menu')
        user_function(user)

#------Modify-----------------------------------------------------------------------------------------

def user_modify(user):
    global widget_set
    for element in widget_set:
        element.destroy()

    user_m = tk.Toplevel()
    user_m.title("Modify")
    user_m.geometry("600x300")

    label = tk.Label(user_m, text = "Here are your old imformation, choosing one imformation you")
    label.grid(column = 0, row = 0)
    label1 = tk.Label(user_m, text = "want to modify.")
    label1.grid(column = 1, row = 0, sticky = tk.W)
    
    name_label = tk.Label(user_m, text = f"Your name:  {user.get_name()}")
    name_label.grid(column = 0, row = 2, sticky = tk.W)
    name_label = tk.Label(user_m, text = "  /  New name:  ")
    name_label.grid(column = 0, row = 2, sticky = tk.E)
    name_entry = tk.Entry(user_m)
    name_entry.grid(column = 1, row = 2, sticky = tk.E)

    gender_label = tk.Label(user_m, text = f"Your gender:  {user.get_sex()}")
    gender_label.grid(column = 0, row = 3, sticky = tk.W)
    gender_label = tk.Label(user_m, text = "  /  New gender:  ")
    gender_label.grid(column = 0, row = 3, sticky = tk.E)
    gender_entry = tk.Entry(user_m)
    gender_entry.grid(column = 1, row = 3, sticky = tk.E)

    birthday_label = tk.Label(user_m, text = f"Your birthday:  {user.get_birth()}")
    birthday_label.grid(column = 0, row = 4, sticky = tk.W)
    birthday_label = tk.Label(user_m, text = "  /  New birthday:  ")
    birthday_label.grid(column = 0, row = 4, sticky = tk.E)
    birthday_entry = tk.Entry(user_m)
    birthday_entry.grid(column = 1, row = 4, sticky = tk.E)

    phone_number_label = tk.Label(user_m, text = f"Your phone number:  {user.get_phone_number()}")
    phone_number_label.grid(column = 0, row = 5, sticky = tk.W)
    empty_label = tk.Label(user_m, text = "")
    empty_label.grid(column = 0, row = 5, sticky = tk.W)
    phone_number_label = tk.Label(user_m, text = "  /  New phone number:  ")
    phone_number_label.grid(column = 0, row = 5, sticky = tk.E)
    phone_number_entry = tk.Entry(user_m)
    phone_number_entry.grid(column = 1, row = 5, sticky = tk.E)
    
    id_label = tk.Label(user_m, text = f"Your ID:  {user.get_account()}")
    id_label.grid(column = 0, row = 6, sticky = tk.W)
    id_label = tk.Label(user_m, text = "  /  New ID:  ")
    id_label.grid(column = 0, row = 6, sticky = tk.E)
    id_entry = tk.Entry(user_m)
    id_entry.grid(column = 1, row = 6, sticky = tk.E)

    pwd_label = tk.Label(user_m, text = f"Your Password:  {user.get_pwd()}")
    pwd_label.grid(column = 0, row = 7, sticky = tk.W)
    pwd_label = tk.Label(user_m, text = "  /  New password:  ")
    pwd_label.grid(column = 0, row = 7, sticky = tk.E)
    pwd_entry = tk.Entry(user_m)
    pwd_entry.grid(column = 1, row = 7, sticky = tk.E)

    
    ok = tk.Button(user_m, text='OK!', command = lambda: done(user,name_entry.get(), gender_entry.get(), birthday_entry.get(), phone_number_entry.get(), id_entry.get(), pwd_entry.get()))
    ok.grid(column = 0, row = 9)

    widget_set = [user_m, name_label, name_entry, gender_label, gender_entry, birthday_entry, birthday_label, phone_number_entry, phone_number_label, id_entry, id_label, pwd_entry, pwd_label, ok]

def done(user, name, gender, birth, phone_number, account, pwd):
    if name != "":
        user.set_name(name)
    elif gender != "":
        user.set_sex(gender)
    elif birth != "":
        user.set_birthday(birth)
    elif phone_number != "":
        user.set_phone_number(phone_number)
    elif account != "":
        done = user.set_account(manager, account)
        if done == 2:
            messagebox.showerror('showerror', 'ERROR: Account exist，Click and back to menu')
            return
    elif pwd != "":
        user.set_pwd(pwd)

    messagebox.showinfo('showinfo', 'Modify completed')
    user_function(user)
    # ok = tk.Button(user_mm, text='OK!', command = lambda: )
    # ok.grid(column = 0, row = 8)

#------withdraw-----------------------------------------------------------------------------------------

def user_withdraw(user):
    global widget_set
    for element in widget_set:
        element.destroy()

    withdraw_money_label = tk.Label(win, text = "How much you want to withdraw: ")
    withdraw_money_label.grid(column = 0, row = 0, padx=10, pady=10)
    withdraw_money_entry = tk.Entry(win)
    withdraw_money_entry.grid(column = 1, row = 0)

    ok = tk.Button(win, text='OK!', command=lambda:user_with(user, withdraw_money_entry.get()))
    ok.grid(column = 1, row = 1, padx = 80)
    
    widget_set=[withdraw_money_label, withdraw_money_entry, ok]

def user_with(user, money):

    done = user.withdraw(manager, money)
    if done == False:
        messagebox.showerror('showerror', 'Syntax Error')
    if done == 1:
        messagebox.showinfo('showinfo', 'Withdraw successed')
    if done == 2:
        messagebox.showerror('showerror', 'Error: Insufficient Balance')
    if done == 3:
        messagebox.showerror('showerror', 'Error: Insufficient permission')

    user_function(user)


#------------------------------------------------------------------------------------------
#-----------------------manager------------------------------------------------------------
#------------------------------------------------------------------------------------------

#------login-----------------------------------------------------------------------------------------


def manager_login():
    global widget_set
    for element in widget_set:
        element.destroy()
    
    space1 = tk.Label(win, text = " ")
    space1.grid(column=0, row=0, padx = 70, pady = 10)
    id_label = tk.Label(win, text = "ID")
    id_label.grid(column = 1, row = 0, sticky = tk.E)
    id_entry= tk.Entry(win)
    id_entry.grid(column = 2, row = 0, sticky = tk.W)

    space1.grid(column=0, row=1, padx = 70, pady = 10)
    pwd_label = tk.Label(win, text = "Password")
    pwd_label.grid(column = 1, row = 1, sticky = tk.E)
    pwd_entry = tk.Entry(win)
    pwd_entry.grid(column = 2, row = 1, sticky = tk.W)

    ok = tk.Button(win, text='OK!', command = lambda:try_to_login(id_entry.get(), pwd_entry.get()))
    ok.grid(column = 2, row = 2)
    widget_set = [space1, id_label, id_entry, pwd_label, pwd_entry, ok]

def try_to_login(acc, pwd):
    global widget_set
    for element in widget_set:
        element.destroy()

    if acc == "M0":
        if pwd == "0":
            manager_function()
        else:
            messagebox.showerror('showerror', 'ERROR: 密碼輸入錯誤，自動跳回選單')
    else:
        messagebox.showerror('showerror', 'ERROR: 帳號輸入錯誤，自動跳回manager選單')
        manager_login()


def manager_function():
    global widget_set
    for element in widget_set:
        element.destroy()

    frame = tk.Frame(win)
    frame.grid()
    list_member_button = tk.Button(frame, text = "List members", command = manager_list_member)
    list_member_button.grid(column = 0, row = 0, pady=10)
    # data_modify_button = tk.Button(frame, text = "List user's permission", command = manager_list_permission)
    # data_modify_button.grid(column = 0, row = 1, pady=10)
    permission_modify_button = tk.Button(frame, text = "Edit permission", command = manager_permission_modify)
    permission_modify_button.grid(column = 0, row = 2, pady=10)
    exit_button = tk.Button(frame, text = "Exit" , command = init)
    exit_button.grid(column=0, row=3, pady=10)
    widget_set=[frame]

def manager_list_member():
    global widget_set
    for element in widget_set:
        element.destroy()
    frame = tk.Frame(win)
    frame.grid()
    i = 0
    member_label =[]
    for member in manager.get_member_list():
        temp = tk.Label(frame,  text = f"【Account: {member.get_account()}】\nName: {member.get_name()}\nSex: {member.get_sex()}\nBirthday: {member.get_birth()} \nPhone number: {member.get_phone_number()}\nPassword: {member.get_pwd()}\n\nPermission level: {manager.get_permission()[member.get_account()]}\n" )
        member_label.append(temp)
        member_label[i].grid(column = i, row = 0)
        i += 1
    ok = tk.Button(frame, text='OK!', command=manager_function)
    ok.grid(column = 0, row = 1, padx = 80)
    member_label.append(ok)
    member_label.append(frame)
    widget_set = member_label

def manager_permission_modify():
    global widget_set
    for element in widget_set:
        element.destroy()

    i = 0
    member_label =[]
    frame1 = tk.Toplevel(win)
    w, h = frame1.winfo_screenwidth(), frame1.winfo_screenheight()
    frame1.geometry("%dx%d+0+0" % (w, h))
    
    # 放圖片失敗
    # fulilan = Image.open("fulilan.png")
    # fulilan_pic = ImageTk.PhotoImage(fulilan)
    # pic = tk.Label(frame1, width=24,height=24, bg = "light blue", bd=1,image = fulilan_pic)
    # pic.grid(column=0,row=0)

    for member in manager.get_member_list():
        temp = tk.Label(frame1, text = f"【Account: {member.get_account()}】\nName: {member.get_name()}\nSex: {member.get_sex()}\nBirthday: {member.get_birth()} \nPhone number: {member.get_phone_number()}\nPassword: {member.get_pwd()}\n\nPermission level: {manager.get_permission()[member.get_account()]}")
        member_label.append(temp)
        member_label[i].grid(column = i+1, row = 1)
        i += 1

    acc_label = tk.Label(frame1, text = " Enter user account you want to modify: ")
    acc_label.grid(column = 0, row = 2)
    acc_entry = tk.Entry(frame1)
    acc_entry.grid(column = 0, row = 3, sticky = tk.E)
    enter = tk.Button(frame1, text = 'Enter', command = lambda: manager_modify_select_user(acc_entry.get()))
    enter.grid(column = 0,row = 4)
    back = tk.Button(frame1, text = 'Back', command = manager_function)
    back.grid(column = 0,row = 5)
    
    member_label.append(back)
    member_label.append(frame1)

    widget_set = member_label
    
def manager_modify_select_user(acc):
    global widget_set
    for element in widget_set:
        element.destroy()
    user_m = tk.Toplevel()
    user_m.title("Modify")
    user_m.geometry("400x300")

    acc_label = tk.Label(user_m, text = f" User account: {acc}") #帳號
    acc_label.grid(column = 0, row = 0)
    og_permission_label = tk.Label(user_m, text = f" Origin permission: {manager.get_permission()[acc]}") #原本的權限
    og_permission_label.grid(column = 0, row = 1)
    permission_label = tk.Label(user_m, text = " New permission:  ")
    permission_label.grid(column = 0, row = 2)
    permission_entry = tk.Entry(user_m)
    permission_entry.grid(column = 1, row = 2, sticky = tk.E)
    # go back go back
    
    ok = tk.Button(user_m, text = 'Ok!', command = lambda:manager_set_permission(acc, permission_entry.get()))
    ok.grid(column = 0,row = 3)
    widget_set = [user_m]
    widget_set.append(ok)


def manager_set_permission(acc, level):
    try:
        level = int(level)
    except:
        messagebox.showerror('showerror', 'ERROR: 權限輸入錯誤，自動跳回manager選單')
        manager_permission_modify()

    manager.set_permission(acc, level)
    print(f"Modify [{acc}]: level")
    manager_permission_modify()


def clerk_login():
    global widget_set
    for element in widget_set:
        element.destroy()
    clerk_input_id = tk.StringVar()
    clerk_input_pws = tk.StringVar()
    space1 = tk.Label(win, text = " ")
    space1.grid(column=0, row=0, padx = 70, pady = 10)
    id_label = tk.Label(win, text = "ID")
    id_label.grid(column = 1, row = 0, sticky = tk.E)
    id_entry= tk.Entry(win ,textvariable = clerk_input_id)
    id_entry.grid(column = 2, row = 0, sticky = tk.W)
    space1.grid(column=0, row=1, padx = 70, pady = 10)
    pws_label = tk.Label(win, text = "Password")
    pws_label.grid(column = 1, row = 1, sticky = tk.E)
    pws_entry = tk.Entry(win ,textvariable = clerk_input_pws)
    pws_entry.grid(column = 2, row = 1, sticky = tk.W)
    ok = tk.Button(win, text='OK!', command=lambda: clerk_succ_or_fail(id_entry.get(), pws_entry.get()))
    ok.grid(column = 2, row = 2)
    widget_set = [space1, id_label, id_entry, pws_label, pws_entry, ok]

def clerk_succ_or_fail(id, pwd):
    global widget_set
    for element in widget_set:
        element.destroy()

    if id == "" or pwd == "":
        messagebox.showerror('showerror', 'Empty is not allowed')
        clerk_login()
    elif id == clerk.get_account():
        if pwd == clerk.get_pwd():
            clerk_choose()
        else:
            messagebox.showerror('showerror', 'Wrong Password')
            clerk_login()
    else:
        messagebox.showerror('showerror', 'ERROR!!')
        clerk_login()

def clerk_choose():
    global widget_set
    for element in widget_set:
        element.destroy()
    frame = tk.Frame(win)
    frame.pack()
    label = tk.Label(frame, text = "HI, Clerk!")
    label.grid(column = 0, row = 0 , pady=10)
    New_button = tk.Button(frame, text = "New", command = clerk_registration)
    New_button.grid(column = 0, row = 1, pady=10)
    Old_button = tk.Button(frame, text = "Old", command = clerk_user_login)
    Old_button.grid(column = 0, row = 2, pady=10)
    Leave_button = tk.Button(frame, text = "Leave", command = init)
    Leave_button.grid(column = 0, row = 3, pady=10)
    widget_set=[frame]

def clerk_function(clerk_user):
    global widget_set
    for element in widget_set:
        element.destroy()
    frame = tk.Frame(win)
    frame.pack()
    Display_users_info_button = tk.Button(frame, text = "Display user's information", command = lambda: clerk_display( clerk_user ))
    Display_users_info_button.grid(column = 0, row = 0, pady=10)
    deposit_button = tk.Button(frame, text = "Deposit" , command = lambda: clerk_deposit( clerk_user ))
    deposit_button.grid(column=0, row=1, padx=10, pady=10)
    modify_button = tk.Button(frame, text = "Modify" , command = lambda: clerk_modify( clerk_user ))
    modify_button.grid(column=0, row=3, padx=10, pady=10)
    withdraw_button = tk.Button(frame, text = "Withdraw" , command = lambda: clerk_withdraw( clerk_user))
    withdraw_button.grid(column=0, row=2, padx=10, pady=10)
    transfer_button = tk.Button(frame, text = "Transfer" , command = lambda: clerk_transfer( clerk_user ))
    transfer_button.grid(column=0, row=4, padx=10, pady=10)
    exit_button = tk.Button(frame, text = "Exit" , command = init)
    exit_button.grid(column=1, row=0, padx=10, pady=10)
    widget_set=[frame]

def clerk_user_login():
    global widget_set
    for element in widget_set:
        element.destroy()

    space1 = tk.Label(win, text = " ")
    space1.grid(column=0, row=2, padx = 70, pady = 30)

    id_label = tk.Label(win, text = "ID: ")
    id_label.grid(column = 1, row = 3, pady=10, sticky = tk.E)
    id_entry= tk.Entry(win)
    id_entry.grid(column = 2, row = 3, pady=10, sticky = tk.W)

    space1.grid(column=0, row=1, padx = 60, pady = 10)
    pwd_label = tk.Label(win, text = "Password: ")
    pwd_label.grid(column = 1, row = 4, sticky = tk.E)
    pwd_entry = tk.Entry(win)
    pwd_entry.grid(column = 2, row = 4, sticky = tk.W)

    ok = tk.Button(win, text='OK!', command=lambda: clerk_user_succ_or_fail(id_entry.get(), pwd_entry.get()))
    ok.grid(column = 2, row = 5, pady = 10)

    widget_set = [space1, id_label, id_entry, pwd_label, pwd_entry, ok]

def clerk_user_succ_or_fail(id, pwd):
    global widget_set
    for element in widget_set:
        element.destroy()

    user_list = manager.get_member_list()
    for user in user_list:
        if id == "" or pwd == "":
            messagebox.showerror('showerror', 'Empty is not allowed')
            clerk_user_login()
            return
        elif id == user.get_account():
            if pwd == user.get_pwd():
                clerk_function(user)
                return
            else:
                messagebox.showerror('showerror', 'Wrong Password')
                clerk_user_login()
                return
    messagebox.showerror('showerror', 'ERROR!!')
    clerk_user_login()
    return
    

def clerk_display(clerk_user): #??
    global widget_set
    for element in widget_set:
        element.destroy()
    clerk_c = tk.Toplevel()
    clerk_c.title("information")
    clerk_c.geometry("600x600")

    name_label = tk.Label(clerk_c, text = f"Name: {clerk_user.get_name()}")
    name_label.grid(column = 0, row = 0, padx=10, pady=10, sticky = tk.E)
    balance_label = tk.Label(clerk_c, text = f"Account: {clerk_user.get_account()}")
    balance_label.grid(column = 0, row = 1, padx=10, pady=10, sticky = tk.E)
    balance_label = tk.Label(clerk_c, text = f"Gender: {clerk_user.get_sex()}")
    balance_label.grid(column = 0, row = 2, padx=10, pady=10, sticky = tk.E)
    balance_label = tk.Label(clerk_c, text = f"Birthday: {clerk_user.get_birth()}")
    balance_label.grid(column = 0, row = 3, padx=10, pady=10, sticky = tk.E)
    balance_label = tk.Label(clerk_c, text = f"Phone Number: {clerk_user.get_phone_number()}")
    balance_label.grid(column = 0, row = 4, padx=10, pady=10, sticky = tk.E)
    balance_label = tk.Label(clerk_c, text = f"Balance: {clerk_user.get_balance()}")
    balance_label.grid(column = 0, row = 5, padx=10, pady=10, sticky = tk.E)

    ok = tk.Button(clerk_c, text='OK!', command = lambda: clerk_function(clerk_user))
    ok.grid(column = 1, row = 2)

    widget_set = [clerk_c]

def clerk_registration():
    global widget_set
    for element in widget_set:
        element.destroy()
    #input variable
    input_name = tk.StringVar()
    input_gender = tk.StringVar()
    input_birthday = tk.StringVar()
    input_phone_number = tk.StringVar()
    input_account = tk.StringVar()
    input_pws = tk.StringVar()
    #
    frame = tk.Frame()
    frame.pack()

    name_label = tk.Label(frame, text = "New name")
    name_label.grid(column = 1, row = 0, sticky = tk.E)
    name_entry = tk.Entry(frame ,textvariable = input_name)
    name_entry.grid(column = 2, row = 0, sticky = tk.W)

    gender_label = tk.Label(frame, text = "New gender")
    gender_label.grid(column = 1, row = 1, sticky = tk.E)
    gender_entry = tk.Entry(frame ,textvariable = input_gender)
    gender_entry.grid(column = 2, row = 1, sticky = tk.W)

    birthday_label = tk.Label(frame, text = "New birthday")
    birthday_label.grid(column = 1, row = 2, sticky = tk.E)
    birthday_entry = tk.Entry(frame ,textvariable = input_birthday)
    birthday_entry.grid(column = 2, row = 2, sticky = tk.W)

    phone_number_label = tk.Label(frame, text = "New phone number")
    phone_number_label.grid(column = 1, row = 3, sticky = tk.E)
    phone_number_entry = tk.Entry(frame ,textvariable = input_phone_number)
    phone_number_entry.grid(column = 2, row = 3, sticky = tk.W)
    
    id_label = tk.Label(frame, text = "New ID")
    id_label.grid(column = 1, row = 4, sticky = tk.E)
    id_entry = tk.Entry(frame ,textvariable = input_account)
    id_entry.grid(column = 2, row = 4, sticky = tk.W)

    pws_label = tk.Label(frame, text = "New Password")
    pws_label.grid(column = 1, row = 5, sticky = tk.E)
    pws_entry = tk.Entry(frame ,textvariable = input_pws)
    pws_entry.grid(column = 2, row = 5, sticky = tk.W)
    
    ok = tk.Button(frame, text='OK!', command=lambda: clerk_create_success(manager, name_entry.get(), gender_entry.get(), birthday_entry.get(), phone_number_entry.get(), id_entry.get(), pws_entry.get()))
    ok.grid(column = 2, row = 6)
    widget_set = [frame]

def clerk_create_success ( manager, name, gender, birthday, phone_number, id, pws ):
    customer = User()
    state = clerk.Regist(customer, manager, name, gender, birthday, phone_number, id, pws )
    if state == 1:
        messagebox.showerror('showerror', "ERROR: Can't enter empty string.")
    if state == 2:
        messagebox.showerror('showerror', "ERROR: Account existed!.")
    if state == 3:
        manager.set_permission(customer.get_account(),3)  #manager更新資料
        manager.add_member(customer) #user list新增user
        messagebox.showinfo('showinfo', "Registraion Completed!")
    clerk_choose()

def clerk_deposit(clerk_user):
    global widget_set
    for element in widget_set:
        element.destroy()
    deposit_money = tk.IntVar()

    frame = tk.Frame(win)
    frame.pack()

    deposit_money_label = tk.Label(frame, text = "How much you want to deopsit")
    deposit_money_label.grid(column = 0, row = 0, padx=10, pady=10)
    deposit_money_entry= tk.Entry(frame ,textvariable = deposit_money)
    deposit_money_entry.grid(column = 1, row = 0)
    ok = tk.Button(frame, text='OK!', command=lambda:clerk_user_deposit(clerk_user, deposit_money_entry.get()))
    ok.grid(column = 1, row = 1, padx = 80)
    widget_set=[frame]

def clerk_user_deposit(clerk_user, money):
    done = clerk.Deposit( clerk_user, manager, money)
    if done == False:
        messagebox.showerror('showerror', 'ERROR: Syntax Error，Click and back to menu')
        clerk_deposit(clerk_user)
    if done == 1:
        messagebox.showinfo('showinfo', 'Deposit Successed，Click and back to menu')
        clerk_function(clerk_user)
    if done == 2:
        messagebox.showerror('showerror', 'ERROR: Insufficient Permission，Click and back to menu')
        clerk_deposit(clerk_user)
        

def clerk_withdraw(clerk_user):
    global widget_set
    for element in widget_set:
        element.destroy()
    withdraw_money = tk.IntVar()

    frame = tk.Frame(win)
    frame.pack()

    withdraw_money_label = tk.Label(frame, text = "How much you want to withdraw")
    withdraw_money_label.grid(column = 0, row = 0, padx=10, pady=10)
    withdraw_money_entry= tk.Entry(frame ,textvariable = withdraw_money)
    withdraw_money_entry.grid(column = 1, row = 0)
    ok = tk.Button(frame, text='OK!', command= lambda:clerk_user_withdraw(clerk_user, withdraw_money_entry.get()))
    ok.grid(column = 1, row = 1, padx = 80)
    widget_set=[frame,withdraw_money_label, withdraw_money_entry, ok]

def clerk_user_withdraw(clerk_user, money):

    state = clerk.Withdraw( clerk_user, manager, money)
    if state == False:
        messagebox.showerror('showerror', 'Syntax Error')
    if state == 1:
        messagebox.showinfo('showinfo', 'Withdraw successed')
    if state == 2:
        messagebox.showerror('showerror', 'Error: Insufficient Balance')
    if state == 3:
        messagebox.showerror('showerror', 'Error: Insufficient permission')

    clerk_function(clerk_user)
    

def clerk_modify(clerk_user):
    global widget_set
    for element in widget_set:
        element.destroy()

    clerk_m = tk.Toplevel()
    clerk_m.title("Modify")
    clerk_m.geometry("600x600")

    label = tk.Label(clerk_m, text = "Here are your old imformation, choosing one imformation you")
    label.grid(column = 0, row = 0)
    label1 = tk.Label(clerk_m, text = "want to modify.")
    label1.grid(column = 1, row = 0, sticky = tk.W)
    
    name_label = tk.Label(clerk_m, text = f"Your name:  {clerk_user.get_name()}")
    name_label.grid(column = 0, row = 2, sticky = tk.W)
    name_label = tk.Label(clerk_m, text = "  /  New name:  ")
    name_label.grid(column = 0, row = 2, sticky = tk.E)
    name_entry = tk.Entry(clerk_m)
    name_entry.grid(column = 1, row = 2, sticky = tk.E)

    gender_label = tk.Label(clerk_m, text = f"Your gender:  {clerk_user.get_sex()}")
    gender_label.grid(column = 0, row = 3, sticky = tk.W)
    gender_label = tk.Label(clerk_m, text = "  /  New gender:  ")
    gender_label.grid(column = 0, row = 3, sticky = tk.E)
    gender_entry = tk.Entry(clerk_m)
    gender_entry.grid(column = 1, row = 3, sticky = tk.E)

    birthday_label = tk.Label(clerk_m, text = f"Your birthday:  {clerk_user.get_birth()}")
    birthday_label.grid(column = 0, row = 4, sticky = tk.W)
    birthday_label = tk.Label(clerk_m, text = "  /  New birthday:  ")
    birthday_label.grid(column = 0, row = 4, sticky = tk.E)
    birthday_entry = tk.Entry(clerk_m)
    birthday_entry.grid(column = 1, row = 4, sticky = tk.E)

    phone_number_label = tk.Label(clerk_m, text = f"Your phone number:  {clerk_user.get_phone_number()}")
    phone_number_label.grid(column = 0, row = 5, sticky = tk.W)
    empty_label = tk.Label(clerk_m, text = "")
    empty_label.grid(column = 0, row = 5, sticky = tk.W)
    phone_number_label = tk.Label(clerk_m, text = "  /  New phone number:  ")
    phone_number_label.grid(column = 0, row = 5, sticky = tk.E)
    phone_number_entry = tk.Entry(clerk_m)
    phone_number_entry.grid(column = 1, row = 5, sticky = tk.E)
    
    id_label = tk.Label(clerk_m, text = f"Your ID:  {clerk_user.get_account()}")
    id_label.grid(column = 0, row = 6, sticky = tk.W)
    id_label = tk.Label(clerk_m, text = "  /  New ID:  ")
    id_label.grid(column = 0, row = 6, sticky = tk.E)
    id_entry = tk.Entry(clerk_m)
    id_entry.grid(column = 1, row = 6, sticky = tk.E)

    pwd_label = tk.Label(clerk_m, text = f"Your Password:  {clerk_user.get_pwd()}")
    pwd_label.grid(column = 0, row = 7, sticky = tk.W)
    pwd_label = tk.Label(clerk_m, text = "  /  New password:  ")
    pwd_label.grid(column = 0, row = 7, sticky = tk.E)
    pwd_entry = tk.Entry(clerk_m)
    pwd_entry.grid(column = 1, row = 7, sticky = tk.E)

    
    ok = tk.Button(clerk_m, text='OK!', command = lambda: clerk_user_modify(clerk_user,name_entry.get(), gender_entry.get(), birthday_entry.get(), phone_number_entry.get(), id_entry.get(), pwd_entry.get()))
    ok.grid(column = 0, row = 8)

    widget_set = [clerk_m, name_label, name_entry, gender_label, gender_entry, birthday_entry, birthday_label, phone_number_entry, phone_number_label, id_entry, id_label, pwd_entry, pwd_label, ok]

def clerk_user_modify(clerk_user, name, gender, birth, phone_number, account, pwd):

    if name != "":
        clerk_user.set_name(name)
    elif gender != "":
        clerk_user.set_sex(gender)
    elif birth != "":
        clerk_user.set_birthday(birth)
    elif phone_number != "":
        clerk_user.set_phone_number(phone_number)
    elif account != "":
        state = clerk_user.set_account(manager, account)
        if state == 2:
            messagebox.showerror('showerror', 'ERROR: Account exist，Click and back to menu')
    elif pwd != "":
        clerk_user.set_pwd(pwd)

    messagebox.showinfo('showinfo', 'Modify completed')
    clerk_function(clerk_user)

def clerk_transfer(clerk_user):
    global widget_set
    for element in widget_set:
        element.destroy()

    #variable
    transfer_to_id = tk.StringVar()
    transfer_money = tk.IntVar()
    #
    frame = tk.Frame(win)
    frame.pack()

    transfer_to_id_label = tk.Label(frame, text = "The ID you want to transfer")
    transfer_to_id_label.grid(column = 0, row = 0, padx=10, pady=10)
    transfer_to_id_entry= tk.Entry(frame ,textvariable = transfer_to_id)
    transfer_to_id_entry.grid(column = 1, row = 0)

    transfer_money_label = tk.Label(frame, text = "Transfer money")
    transfer_money_label.grid(column = 0, row = 1, padx=10, pady=10)
    transfer_money_entry= tk.Entry(frame ,textvariable = transfer_money)
    transfer_money_entry.grid(column = 1, row = 1)
    ok = tk.Button(frame, text='OK!', command=lambda:clerk_user_transfer(clerk_user, transfer_to_id_entry.get(), transfer_money_entry.get()))
    ok.grid(column = 1, row = 2)
    widget_set=[frame,transfer_to_id_label, transfer_to_id_entry, transfer_money_label, transfer_money_entry, ok]

def clerk_user_transfer(clerk_user, id, money):
    if id == "" or money == "":
        messagebox.showerror('showerror', 'Syntax Error')
        clerk_function(clerk_user)
        return

    state = clerk.Transfer( clerk_user, manager, id ,money)
    if state == 1:
        messagebox.showinfo('showinfo', 'Transfer successed')
        clerk_function(clerk_user)
    elif state == 2:
        messagebox.showerror('showerror', 'ERROR: Balance is insufficient')
        clerk_function(clerk_user)
    elif state == 3:
        messagebox.showerror('showerror', 'ERROR: Account Not Found')
        clerk_function(clerk_user)

win = tk.Tk()
win.title("Online bank system")
win.geometry('500x300')
init()
win.mainloop()
