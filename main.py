import user_interface;
import user_menu;
import admin_menu;

user_tp = user_interface.user_type();
flag = 100;
if (user_tp == 'admin'):
    while (flag != 3):
        flag = admin_menu.menu();
else:
    while (flag != 4):
        flag = user_menu.menu(user_tp);
        if (flag == 0):
            print("Error");
            break;
