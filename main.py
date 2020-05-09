import user_interface;
import user_menu;
import admin_menu;

user_type = user_interface.user_type();
number_of_menu = 100;
if (user_type == 'admin'):
    while (number_of_menu != 3):
        number_of_menu = admin_menu.menu();
else:
    while (number_of_menu != 4):
        number_of_menu = user_menu.menu(user_type);
        if (number_of_menu == 0):
            print("Error");
            break;
