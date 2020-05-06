import admin_interface;
from database_accessor import database_accessor;

database_accessor = database_accessor();

def menu():
    print("1. Output table");
    print("2. Update data");
    print("3. Exit");
    num = input("Enter number: ");
    if int(num) == 1:
        admin_interface.output_table();
    elif int(num) == 2:
        admin_interface.update_table()
        return 2;
    elif int(num) == 3:
        return 3;
    else:
        return 1;
