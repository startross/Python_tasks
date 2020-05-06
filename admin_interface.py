from database_accessor import database_accessor;

database_accessor = database_accessor();

def output_table():
    print("Names of tables: stocks, users, users names");
    table = input("Enter name of table: ");
    if table == "stocks" or table == "users":
        database_accessor.show_table(table);
    else:
        row = database_accessor.select_row("users",table);
        if row == None:
            print("Table with this name does not exist");
            return 1;
        else:
            flag = database_accessor.show_table(table);
            if flag == 0:
                print("User has not got stocks");

def update_table():
    table = input("Enter name of table: ");
    if table == "stocks":
        flag1 = 0;
        while flag1 == 0:
            company = input("Enter name of company: ");
            row = database_accessor.select_row("stocks",company);
            if row == None:
                flag1 = 0;
                print("There is no such company in the database. Try again.");
            else:
                flag1 = 1;
        flag2 = 0;
        while flag2 == 0:
            param = input("What do you want to update? ");
            if param == "company" or param == "id":
                tmp = input("Enter new data: ");
                database_accessor.update_row("stocks",param,tmp,company);
                flag2 = 1;
            elif param == "price" or param == "stocks_amount":
                tmp = input("Enter new data: ");
                database_accessor.update_row("stocks",param,int(tmp),company);
                flag2 = 1;
            else:
                print("Incorrect parameter. Try again.");
    elif table == "users":
        flag1 = 0;
        while flag1 == 0:
            lgn = input("Enter login: ");
            row = database_accessor.select_row("users",lgn);
            if row == None:
                flag1 = 0;
                print("There is no such login in the database. Try again.");
            else:
                flag1 = 1;
        flag2 = 0;
        while flag2 == 0:
            param = input("What do you want to update? ");
            if param == "login" or param == "password":
                tmp = input("Enter new data: ");
                database_accessor.update_row("users",param,tmp,lgn);
                flag2 = 1;
            elif param == "money":
                tmp = input("Enter new data: ");
                database_accessor.update_row("users",param,int(tmp),lgn);
                flag2 = 1;
            else:
                print("Incorrect parameter. Try again.");              
    else:
        row = database_accessor.select_row("users",table);
        if row == None:
            print("Table with this name does not exist");
            return 0;
        else:
            flag1 = 0;
            while flag1 == 0:
                company = input("Enter company: ");
                row = select_row(table,company);
                if row == None:
                    flag1 = 0;
                    print("There is no such login in the database. Try again.");
                else:
                    flag1 = 1;
            flag2 = 0;
            while flag2 == 0:
                param = input("What do you want to update? ");
                if param == "copmany" or param == "id":
                    tmp = input("Enter new data: ");
                    database_accessor.update_row(table,param,tmp,company);
                    flag2 = 1;
                elif param == "stocks_amount":
                    tmp = input("Enter new data: ");
                    database_accessor.update_row(table,param,int(tmp),company);
                    flag2 = 1;
                else:
                    print("Incorrect parameter. Try again.");   
