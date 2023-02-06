import os
from colorama import *
init()
""" You need to install the colorama library
    Install the library
    Type in CMD ( pip install colorama )
"""
products = []
products1 = []
products_user = []
user = []
user_file = "user.txt"
data = "data.txt"
admin_name = ""
admin_pass = ""

# Text color 
def error(m = None):
    print (Style.BRIGHT+Fore.RED+m+Style.RESET_ALL + Fore.RESET)
def ta(m = None) :
    print (Style.BRIGHT+Fore.GREEN+m+Style.RESET_ALL + Fore.RESET)
def matn(m = None) :
    print (Style.BRIGHT+Fore.LIGHTBLACK_EX+m+Style.RESET_ALL+ Fore.RESET)
def title(m = None) :
    print (Style.BRIGHT+Fore.BLUE+m+Style.RESET_ALL+ Fore.RESET)

# chek file user
if os.path.exists(user_file):
    u_f = open(user_file)
    for i in u_f :
        a = i.split(",")
        ab = {"user":a[0] , "name":a[1] , "password":a[2].replace("\n" , "")}
        user.append(ab)
    u_f.close()
else :
    admin_name = ""
    user_name = ""

# chek file 
if os.path.exists(data):
    d_f = open(data)
    for i in d_f :
        a = i.split(",")
        ab = {"id":a[0] , "name":a[1] , "price":a[2] , "count":a[3].replace("\n" , "")}
        products.append(ab)
    d_f.close()
else :
    d_f = open(data, "a+")
    a = "1000,chips,4500,27\n"
    b = "1001,yogurt,21000,16\n"
    c = "1002,Pepsi,16000,23\n"
    d_f.writelines(a)
    d_f.writelines(b)
    d_f.writelines(c)
    d_f.close()
    d_f = open(data)
    for i in d_f :
        a = i.split(",")
        ab = {"id":a[0] , "name":a[1] , "price":a[2] , "count":a[3].replace("\n" , "")}
        products.append(ab)
    d_f.close()
    
# chek user products
if len(user) == 1 :
    if user[0]["user"] == "Admin" :
        admin_name = user[0]["name"]
        admin_pass = user[0]["password"]
        user_name = ""
    elif user[0]["user"] == "User" :
        user_name = user[0]["name"]
        user_pass = user[0]["password"]
        admin_name = ""
elif len(user) == 2 :
    if user[0]["user"] == "Admin" :
        kh_admin = 0
        admin_name = user[0]["name"]
        admin_pass = user[0]["password"]
    elif user[1]["user"] == "Admin" :
        kh_admin = 1
        admin_name = user[1]["name"]
        admin_pass = user[1]["password"]
    if user[0]["user"] == "User" :
        kh_user = 0
        user_name = user[0]["name"]
        user_pass = user[0]["password"]
    elif user[1]["user"] == "User" :
        kh_user = 1
        user_name = user[1]["name"]
        user_pass = user[1]["password"]

# chek user
def chek_user() :
    global kh_admin
    global admin_name
    global admin_pass
    global kh_user
    global user_name
    global user_pass

    if len(user) == 1 :
        if user[0]["user"] == "Admin" :
            admin_name = user[0]["name"]
            admin_pass = user[0]["password"]
            kh_admin = 0
            user_name = ""
        elif user[0]["user"] == "User" :
            user_name = user[0]["name"]
            user_pass = user[0]["password"]
            kh_user = 0
            admin_name = ""
    elif len(user) == 2 :
        if user[0]["user"] == "Admin" :
            kh_admin = 0
            admin_name = user[0]["name"]
            admin_pass = user[0]["password"]
        elif user[1]["user"] == "Admin" :
            kh_admin = 1
            admin_name = user[1]["name"]
            admin_pass = user[1]["password"]
        if user[0]["user"] == "User" :
            kh_user = 0
            user_name = user[0]["name"]
            user_pass = user[0]["password"]
        elif user[1]["user"] == "User" :
            kh_user = 1
            user_name = user[1]["name"]
            user_pass = user[0]["password"]
        admin_pass = admin_pass.replace("\n" , "")
        user_pass = user_pass.replace("\n" , "")

# menu admin & user & guest
def admin_user_guest() :
    global kh_admin
    global admin_name
    global admin_pass
    global kh_user
    global user_name
    global user_pass

    title("\nWhich account do you log in with?")
    if admin_name == "" : matn("1_ Admin")
    else : matn("1_ Admin : " + admin_name)

    if user_name == "" : matn("2_ User")
    else : matn("2_ User : " + user_name)

    matn("3_ Guest user")
    matn("0_ Exit")

    a = int(input("_ ").strip())
    if a == 0 :
        ex()
    elif a == 1 :
        return admin()
    elif a == 2 :
        return user1()
    elif a == 3 :
        return 3
    else :
        error("\nPlease choose a number between 0 and 3 .")
        return 4

# admin password
def admin():
    
    if admin_name != "" :
        while True :
            title("\n**** Hi "+ admin_name+" ****")
            matn("\n1_ Back")
            matn("0_ Exit")

            p = input("Enter password to go product menu : ").strip()

            if p == "1" :
                return 0
            elif p == "0" :
                ex()
            elif p == "" :
                error("\nempty password .")
                continue
            elif p == admin_pass :
                return 1
            else :
                error("\nThe password is incorrect .")
    else :
        while True :
            name = input("Enter user name : ").strip()
            if name == "":
                error("\nempty name .\n")
                continue
            while True :
                paas = input("Enter password : ").strip()
                if paas == "":
                        error("\nempty password .\n")
                        continue
                break
            break
        ab = {"user":"Admin" , "name":name , "password":paas}
        user.append(ab)
        chek_user()
        return 1

# menu admin    
def admin_menu() :
    global kh_admin
    global admin_name
    global admin_pass
    global kh_user
    global user_name
    global user_pass

    title ("\n***** Menu Admin "+admin_name + " *****")
    matn("\n1_ Add new")
    matn("2_ Delete")
    matn("3_ Edit")
    matn("4_ Search")
    matn("5_ Show list")
    matn("6_ Change username")
    matn("7_ Change password")
    matn("8_ Delete account")
    matn("9_ Meno user")
    matn("0_ Exit")

    op = int(input("- ").strip())

    if op == 0 :
        ex()
    elif op == 1 :
        add()
    elif op == 2 :
        Delete_admin()
    elif op == 3 :
        edit()
    elif op == 4 :
        search()
    elif op == 5 :
        show_list()
    elif op == 6 :
            pp = input("Enter password : ").strip()
            if pp == admin_pass :
                p1 = input("Enter username new : ").strip()
                user[kh_admin]["name"] = p1
                admin_name = p1
                ta("\nUsername has been changed .")
            else :
                error("\nThe password is incorrect .")
    elif op == 7 :
            pp = input("Enter password old : ").strip()
            if pp == admin_pass :
                p1 = input("Enter password new : ").strip()
                user[kh_admin]["password"] = p1
                admin_pass = p1
                ta("\npassword has been changed .")
            else :
                error("\nThe password is incorrect .")
    elif op == 8 :
            pp = input("Enter password : ").strip()
            if pp == admin_pass :
                del user[kh_admin]
                ta("\nAccount deleted .")
                admin_name = ""
                admin_pass = ""
                return 0
            else :
                error("\nThe password is incorrect .")
    elif op == 9 :
        return 0
    else :
        error("\nPlease choose a number between 0 and 9 .")

# user password
def user1():
    
    if user_name != "" :
        while True :
            title("\n**** Hi "+ user_name+" ****")
            matn("\n1_ Back")
            matn("0_ Exit")

            p = input("Enter password to go product menu : ").strip()

            if p == "1" :
                return 0
            elif p == "0" :
                ex()
            elif p == "" :
                error("\nempty password .")
                continue
            elif p == user_pass :
                return 2
            else :
                error("\nThe password is incorrect .")
    else :
        while True :
            name = input("Enter user name : ").strip()
            if name == "":
                error("\nempty name .\n")
                continue
            while True :
                paas = input("Enter password : ").strip()
                if paas == "":
                        error("\nempty password .\n")
                        continue
                break
            break
        ab = {"user":"User" , "name":name , "password":paas}
        user.append(ab)
        chek_user()
        return 2

# user menu
def user_menu() :
    global kh_admin
    global admin_name
    global admin_pass
    global kh_user
    global user_name
    global user_pass

    title ("\n***** Menu User "+user_name + " *****")
    matn("\n1_ Buy")
    matn("2_ Search")
    matn("3_ list Shoping")
    matn("4_ payment")
    matn("5_ Change username")
    matn("6_ Change password")
    matn("7_ Delete account")
    matn("8_ Meno user")
    matn("0_ Exit")

    op = int(input("Enter namber : ").strip())

    if op == 0 :
        ex()
    elif op == 1 :
        buy()
    elif op == 2 :
        search_user()
    elif op == 3 :
        while True :
            show_list(products_user)
            matn("\n1_ Delete")
            matn("2_ Edit")
            matn("3_ payment")
            matn("0_ Back")
            a = int(input("Enter namber : ").strip())
            if a == 0 :
                break
            elif a == 1 :
                Delete_user()
            elif a == 2 :
                edit_user()
            elif a == 3 :
                payment()
            else :
                error("\nPlease choose a number between 0 and 3 .\n")

    elif op == 4 :
        payment()
    elif op == 5 :
            pp = input("Enter password : ").strip()
            if pp == user_pass :
                p1 = input("Enter username new : ").strip()
                user[kh_user]["name"] = p1
                user_name = p1
                ta("\nUsername has been changed .")
            else :
                error("\nThe password is incorrect .")
    elif op == 6 :
            pp = input("Enter password old : ").strip()
            if pp == user_pass :
                p1 = input("Enter password new : ").strip()
                user[kh_user]["password"] = p1
                user_pass = p1
                ta("\npassword has been changed .")
            else :
                error("\nThe password is incorrect .")
    elif op == 7 :
            pp = input("Enter password : ").strip()
            if pp == user_pass :
                del user[kh_user]
                ta("\nAccount deleted .")
                user_name = ""
                user_pass = ""
                return 0
            else :
                error("\nThe password is incorrect .")
    elif op == 8 :
        return 0
    else :
        error("\nPlease choose a number between 0 and 8 .")

# buy user
def buy(dic = products):
    while True :
        m = 0
        show_list(dic)
        title("\nBUY")
        matn ("0_ Back")
        a = input("Enter name or id :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products :
            if a == i["name"] or a == i["id"] :
                m = 1
                al = i
                d = [{"id":i["id"],"name":i["name"],"price":i["price"],"count":i["count"]}]
                show_list(d)
                while True :
                    how = int(input("\nhow many count? ").strip())
                    if how > int(al["count"]) :
                        error("\nThis number is not available in the store .")
                    else :
                        break
                d = [{"id":i["id"],"name":i["name"],"price":i["price"],"count":str(how)}]
                show_list(d)
                sal = input("\nDo you add to the shopping list? ? y/n \n").strip().lower()
                if sal == "y" :
                    d = {"id":i["id"],"name":i["name"],"price":i["price"],"count":str(how)}
                    products_user.append(d)
                    ta("\nadded .\n")
                else :
                    continue
                
        if m == 0 :
                error("\nThe desired name or ID was not found .\n")

# Delete products
def Delete_user():
    while True :
        h = 0
        m = 0
        show_list(products_user)
        title("\nDelete")
        matn("0_ Back")
        a = input("Enter name or id :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products_user :
            if a == i["name"] or a == i["id"] :
                d = [{"id":i["id"],"name":i["name"],"price":i["price"],"count":i["count"]}]
                show_list(d)
                sal = input("\nDelete ? y/n \n").strip().lower()
                if sal == "y" :
                    del products_user[h]
                    ta("\nDeleted .\n")
                else :
                    continue
                m = 1
                
            h += 1
        if m == 0 :
                error("\nThe desired name or ID was not found .\n")

# edit products user
def edit_user() :
    while True :
        m = 0
        h = 0
        show_list(products_user)
        title("\nEdit")
        matn("0_ Back")
        a = input("Enter name or id :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products_user :
            if a == i["name"] or a == i["id"] :
                now = i
                m = 1
                h1 = h
                continue
            h += 1
        if m == 0 :
                error("\nThe desired name or ID was not found .\n")
        elif m == 1 :
            while True :
                a3 = int(input("Enter count = "+now["count"]+" : ").strip())
                for i in products :
                    if a == i["name"] or a == i["id"] :
                        if a3 <= int(i["count"]) :
                            m = 0
                if m != 0 :
                    error("\nThis number is not available in the store . \n")
                else :
                    d = [{"id":now["id"],"name":now["name"],"price":now["price"],"count":str(a3)}]
                    show_list(d)
                    sal = input("\nsaved ? y/n \n").strip().lower()
                    if sal == "y" :
                        products_user[h1]["count"] = str(a3)
                        break
                    else :
                        break

# search user
def search_user():
    while True :
        products1 = []
        m = 0
        h = 0
        title("\nSearch")
        matn("0_ Back")
        a = input("Enter name or id or character :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products :
            if i["name"].find(a) != -1 or i["id"].find(a) != -1 :
                now = i
                products1.append(now)
                m = 1
                continue
            h += 1
        if m == 0 :
                error("\nThe desired name or ID was not found .")
        else :
            show_list(products1)
            break

    if a != "0" :
        while True :
            m = 0
            h = 0
            title("\nSearch")
            matn("1_ Buy")
            matn("0_ Back")
            a = input("Enter name or id or character :").strip()
            if a == "0" :
                break
            elif a == "" :
                continue
            elif a == "1" :
                buy(products1)
                break
            products1 = []
            for i in products :
                if i["name"].find(a) != -1 or i["id"].find(a) != -1 :
                    now = i
                    products1.append(now)
                    m = 1
                    continue
                h += 1
            if m == 0 :
                    error("\nThe desired name or ID was not found .")
            else :
                show_list(products1)

# payment user
def payment():
    global products_user
    if len(products_user) != 0 :
        while True :
            t_p = 0
            t_c = 0
            for i in products_user :
                t_p += int(i["price"]) * int(i["count"])
                t_c += int(i["count"])
            ab1 = {"id":"total","name":" ", "price":str(t_p) , "count":str(t_c)}
            products_user.append(ab1)
            show_list(products_user)
            matn("\n1_ payment")
            matn("0_ Back")

            a = int(input("Enter namber : ").strip())
            if a == 1 :
                ab = input("\ndo you pay ? y/n ").strip().lower()
                if ab == "y" :
                    for i in products_user :
                        for v in products :
                            if i["id"] == v["id"] :
                                v["count"] = str(int(v["count"]) - int(i["count"]))
                                products_user = []
                    break
                else :
                    del products_user[len(products_user)-1]
                    continue
            elif a == 0 :
                del products_user[len(products_user)-1]
                break
            else :
                error("\nPlease choose a number between 0 and 1 .\n")
    else :
        error("\nList is empty .")

# menu guest
def guest():
    while True :
        matn("\n1_ Show list")
        matn("2_ Search")
        matn("0_ Back")
        a = int(input("Enter namber : ").strip())
        if a == 1 :
            show_list()
        elif a == 2 :
            while True :
                products1 = []
                m = 0
                h = 0
                title("\nSearch")
                matn("0_ Back")
                a = input("Enter name or id or character :").strip()
                if a == "0" :
                    break
                if a == "" :
                    continue
                for i in products :
                    if i["name"].find(a) != -1 or i["id"].find(a) != -1 :
                        now = i
                        products1.append(now)
                        m = 1
                        continue
                    h += 1
                if m == 0 :
                        error("\nThe desired name or ID was not found .")
                else :
                    show_list(products1)
        elif a == 0 :
            return 0
        else:
            error("\nPlease choose a number between 0 and 2 .")

# show list products
def show_list(dic = products) :
    h = "ID"+"\t| "+"name"+"\t\t| "+"price"+"\t\t| "+"count  "
    v = "-"*8+"|"+"-"*15+"|"+"-"*15+"|"+"-"*8
    print (Style.BRIGHT+Back.RED+Fore.WHITE+h+Style.RESET_ALL +Back.RESET+ Fore.RESET)
    print(Fore.YELLOW+"-"*len(v)+Fore.RESET)
    r = 0
    for i in dic :
        if r == 0 :
            r = 1
            if len(i["name"]) >= 6 :
                if len(i["price"]) >= 6 :
                    print (Fore.BLUE+i["id"]+"\t| "+i["name"]+"\t| "+i["price"]+"\t| "+i["count"], Fore.RESET)
                    print(v)
                else :
                    print (Fore.BLUE+i["id"]+"\t| "+i["name"]+"\t| "+i["price"]+"\t\t| "+i["count"], Fore.RESET)
                    print(v)
            else :
                if len(i["price"]) >= 6 :
                    print (Fore.BLUE+i["id"]+"\t| "+i["name"]+"\t\t| "+i["price"]+"\t| "+i["count"], Fore.RESET)
                    print(v)
                else :
                    print (Fore.BLUE+i["id"]+"\t| "+i["name"]+"\t\t| "+i["price"]+"\t\t| "+i["count"], Fore.RESET)
                    print(v)
        elif r == 1 :
            r = 0
            if len(i["name"]) >= 6 :
                if len(i["price"]) >= 6 :
                    print (Fore.RED+i["id"]+"\t| "+i["name"]+"\t| "+i["price"]+"\t| "+i["count"], Fore.RESET)
                    print(v)
                else :
                    print (Fore.RED+i["id"]+"\t| "+i["name"]+"\t| "+i["price"]+"\t\t| "+i["count"], Fore.RESET)
                    print(v)
            else :
                if len(i["price"]) >= 6 :
                    print (Fore.RED+i["id"]+"\t| "+i["name"]+"\t\t| "+i["price"]+"\t| "+i["count"], Fore.RESET)
                    print(v)
                else :
                    print (Fore.RED+i["id"]+"\t| "+i["name"]+"\t\t| "+i["price"]+"\t\t| "+i["count"], Fore.RESET)
                    print(v)
            pass

# exit & save
def ex() :
    a = input("\n\nDo you want to exit ? y/n _ ").strip().lower()
    if a == "y":
        a = input("\n\nDo you save the changes? ? y/n _ ").strip().lower()
        if a == "y" :
                u_f = open(user_file , "w" )
                for i in user :
                    ab = i["user"]+","+i["name"]+","+i["password"]+"\n"
                    u_f.writelines(ab)
                u_f.close()
                d_f = open(data , "w")
                for i in products :
                    ab = i["id"]+","+i["name"]+","+i["price"]+","+i["count"]+"\n"
                    d_f.writelines(ab)
                d_f.close()
                exit()
        else :
            exit()

# add products
def add() :
    while True :
        mm = 0
        title("\nADD")
        matn ("0_ Back")
        name = input("name products : ").strip()
        if name == "0" :
            return 0
        elif name == "" :
            continue
        for m in products :
            if m["name"] == name :
                mm = 1
        if mm == 1 :
            error("\nThis name is on the list.")
            continue
        price = input("price products : ").strip()
        if price == "" :
            continue
        
        count = input("count products : ").strip()
        if count == "" :
            continue
        ab = {"id":str(int(products[len(products)-1]["id"])+1),"name":name, "price":price , "count":count}
        ab1 = [{"id":str(int(products[len(products)-1]["id"])+1),"name":name, "price":price , "count":count}]
        show_list(ab1)
        sal = input("\nsaved ? y/n \n_ ").strip().lower()
        if sal == "y" :
            products.append(ab)
            show_list()

# Delete products
def Delete_admin(dic = products) :
    while True :
        h = 0
        m = 0
        show_list(dic)
        title("\nDelete")
        matn("0_ Back")
        a = input("Enter name or id :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products :
            if a == i["name"] or a == i["id"] :
                d = [{"id":i["id"],"name":i["name"],"price":i["price"],"count":i["count"]}]
                show_list(d)
                sal = input("\nDelete ? y/n \n_ ").strip().lower()
                if sal == "y" :
                    del products[h]
                    ta("\nDeleted .")
                else :
                    continue
                m = 1
                
            h += 1
        if m == 0 :
                error("\nThe desired name or ID was not found .\n")
        else : 
            if dic != products :
                break

# Edit products
def edit(dic = products) :
    while True :
        m = 0
        h = 0
        show_list(dic)
        title("\nEdit")
        matn("0_ Back")
        a = input("Enter name or id :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products :
            if a == i["name"] or a == i["id"] :
                now = i
                m = 1
                h1 = h
                continue
            h += 1
        if m == 0 :
                error("\nThe desired name or ID was not found .\n")
        elif m == 1 :
            a1 = input("Enter name = "+now["name"]+" : ").strip()
            a2 = input("Enter price = "+now["price"]+" : ").strip()
            a3 = input("Enter count = "+now["count"]+" : ").strip()
            if a1 == "" :
                a1 = now["name"]
            if a2 == "" :
                a2 = now["price"]
            if a3 == "" :
                a3 = now["count"]
            d = [{"id":now["id"],"name":a1,"price":a2,"count":a3}]
            show_list(d)
            sal = input("\nsaved ? y/n \n_ ").strip().lower()
            if sal == "y" :
                products[h1]["name"] = a1
                products[h1]["price"] = a2
                products[h1]["count"] = a3
            else :
                continue
        if dic != products :
            break

# search products
def search():
    while True :
        products1 = []
        m = 0
        h = 0
        title("\nSearch")
        matn("0_ Back")
        a = input("Enter name or id or character :").strip()
        if a == "0" :
            break
        if a == "" :
            continue
        for i in products :
            if i["name"].find(a) != -1 or i["id"].find(a) != -1 :
                now = i
                products1.append(now)
                m = 1
                continue
            h += 1
        if m == 0 :
                error("\nThe desired name or ID was not found .")
        else :
            show_list(products1)
            break
    if a != "0" :
        while True :
            m = 0
            h = 0
            title("\nSearch")
            matn("1_ Delete")
            matn("2_ Edit")
            matn("0_ Back")
            a = input("Enter name or id or character :").strip()
            if a == "0" :
                break
            elif a == "" :
                continue
            elif a == "1" :
                Delete_admin(products1)
                break
            elif a == "2" :
                edit(products1)
                break
            products1 = []
            for i in products :
                if i["name"].find(a) != -1 or i["id"].find(a) != -1 :
                    now = i
                    products1.append(now)
                    m = 1
                    continue
                h += 1
            if m == 0 :
                    error("\nThe desired name or ID was not found .")
            else :
                show_list(products1)

while True :
    a = admin_user_guest()
    if a == 1 :
        while True :
            if admin_menu() == 0 :
                break
    elif a == 2 :
        while True :
            if user_menu() == 0 :
                break
    elif a == 3 :
        while True :
            if guest() == 0 :
                break
    elif a == 0 :
        continue
