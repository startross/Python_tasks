from database_accessor import database_accessor;

database_accessor = database_accessor();

error = "error";

def create_user():
    table = "users";
    i = 1;
    while i <= 3:
        flag = 1;
        print("REGISTRATION");
        while flag:
            login = input("Enter your login: ");
            row = database_accessor.select_row(table,login);
            if row == None:
                break;
            print("Sorry, this login is busy.");
        password = input("Enter your password: ");
        money = input("What amount do you want to save for your acoount? ");
        print();
        database_accessor.insert_row(table,login,password,money);
        row = database_accessor.select_row(table,login);
        if row != None:
            print("Registration successful!");
            print(f"Hello {login}!");
            database_accessor.create_table(login);
            return login;
        else:
            i = i+1;
    return error;

def user_type():
    table = "users";
    user_tp = "user";
    flag = 1;
    while flag == 1:
        ans_type = input("Are you admin? ");
        if ans_type == "yes":
            psw = input("Enter password: ");
            if (psw == "qwerty"):
                print("Hello admin!");
                user_tp = "admin";
                return user_tp;
            else:
                print("You are not admin.");
        elif ans_type == "no":
            ans_account = input("Have you got the account? ");
            if ans_account == "yes":
                i = 1;
                while i <= 3:
                    lgn = input("Enter your login: ");
                    pwrd = input("Enter your password: ");
                    row = database_accessor.check_user(lgn,pwrd);
                    if row != None:
                        print(f"Hello {lgn}!");
                        user_tp = lgn;
                        return user_tp;
                    else:
                        print("Login or password is incorrect. Please, try again.");
                        i = i+1;
                print("Your attempts are over.");
                ans_register = input("Would you like to register? ");
                if ans_register == "no":
                    return error;
                elif ans_register == "yes":
                    tmp = create_user();
                    if tmp != error:
                        user_tp = tmp;
                        return user_tp;
                    else:
                        return error;
            elif ans_account == "no":
                tmp = create_user();
                if tmp != error:
                    user_tp = tmp;
                    return user_tp;
                else:
                    return error;

def buy(login):
    print("All stocks:");
    database_accessor.show_table("stocks");
    row = database_accessor.select_row("users",login);
    if row == None:
        return 0;
    money = row[2];
    flag1 = 0;
    while flag1 == 0:
        company = input("Which company.s stocks do you want to buy? ");
        if company == "no":
            return 1;
        row = database_accessor.select_row("stocks",company);
        if row == None:
            flag1 = 0;
            print("There is no such company in the database. Try again.");
        else:
            flag1 = 1;
    id_company = row[1];
    price = row[2];
    stocks = row[3];
    amount = input("How many stocks do you want to buy? ");
    flag2 = 0;
    while flag2 == 0:
        flag2 = 1;
        if int(amount)*price > money:
            flag2 = 0;
            amount = input("Not enough money. Enter again: ");
        if int(amount) > stocks:
            flag2 = 0;
            amount = input("Wrong quantity stocks. Enter again: ");
    row = database_accessor.select_row(login,company);
    if row == None:
        database_accessor.insert_row(login,company,id_company,int(amount));
    else:
        tmp = row[2]
        database_accessor.update_row(login,"stocks_amount",tmp+int(amount),company);
    row = database_accessor.select_row("users",login);
    tmp = row[2];
    database_accessor.update_row("users","money",tmp-int(amount)*price,login);
    row = database_accessor.select_row("stocks",company);
    tmp = row[3];
    database_accessor.update_row("stocks","stocks_amount",tmp-int(amount),company);
    print("Complete");

def sell(login):
    print("Your stocks:");
    database_accessor.show_table(login);
    row = database_accessor.select_row("users",login);
    if row == None:
        return 0;
    flag1 = 0;
    while flag1 == 0:
        company = input("Which company.s stocks do you want to sell? ");
        if company == "no":
            return 1;
        row = database_accessor.select_row(login,company);
        if row == None:
            flag1 = 0;
            print("There is no such company in the database. Try again.");
        else:
            flag1 = 1;
    id_company = row[1];
    stocks = row[2];
    amount = input("How many stocks do you want to sell? ");
    flag2 = 0;
    while flag2 == 0:
        flag2 = 1;
        if int(amount) > stocks:
            flag2 = 0;
            amount = input("Wrong quantity stocks. Enter again: ");
    if int(amount) == stocks:
        database_accessor.delete_row(login,company,id_company);
    else:
        database_accessor.update_row(login,"stocks_amount",stocks-int(amount),company);
    row = database_accessor.select_row("stocks",company);
    price = row[2];
    tmp = row[3];
    database_accessor.update_row("stocks","stocks_amount",tmp+int(amount),company);
    row = database_accessor.select_row("users",login);
    tmp = row[2];
    database_accessor.update_row("users","money",tmp+int(amount)*price,login);
    print("Complete");
