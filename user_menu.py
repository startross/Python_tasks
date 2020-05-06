import user_interface;
from database_accessor import database_accessor;

database_accessor = database_accessor();

def menu(login):
    print("1. Personal account");
    print("2. Buy stocks");
    print("3. Sell stocks");
    print("4. Exit");
    num = input("Enter number: ");
    if int(num) == 1:
        row = database_accessor.select_row("users",login);
        print("Amount of your money: ",row[2]);
        print("Your stocks:");
        flag = database_accessor.show_table(login);
        if flag == 0:
            print("You have not got stocks");
        return 1;
    elif int(num) == 2:
        tmp = 1;
        tmp = user_interface.buy(login);
        if tmp == 0:
            return 0;
        return 2;
    elif int(num) == 3:
        tmp = 1;
        tmp = user_interface.sell(login);
        if tmp == 0:
            return 0;
        return 3;
    elif int(num) == 4:
        return 4;
    else:
        return 1;
