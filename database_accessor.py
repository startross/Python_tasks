import sqlite3;

class database_accessor:
    
    conn = sqlite3.connect("mydatabase1.db");
    cursor = conn.cursor();
    
    def create_table(self,table):
        if table == "stocks":
            self.cursor.execute("CREATE TABLE stocks (company text,id text,price integer,stocks_amount integer)");
        elif table == "users":
            self.cursor.execute("CREATE TABLE users (login text,password text,money integer)");
        else:
            self.cursor.execute(f"CREATE TABLE {table} (company text,id text,stocks_amount integer)");
            

    def init_table(self,table):
        if table == "stocks":
            f = open("stocks.txt","r");
            for line in f:
                line = line.strip().split("/");
                company = line[0];
                id_company = line[1];
                price = line[2];
                stocks_amount = line[3];
                self.cursor.execute(f"INSERT INTO {table} VALUES (?,?,?,?)",(company,id_company,int(price),int(stocks_amount)));
            f.close;
            self.conn.commit();
        elif table == "users":
            f = open("users.txt","r");
            for line in f:
                line = line.strip().split("/");
                login = line[0];
                password = line[1];
                money = line[2];
                self.cursor.execute(f"INSERT INTO {table} VALUES (?,?,?)",(login,password,int(money)));
            f.close;
            self.conn.commit();

    def show_table(self,table):
        if table == "stocks":
            for row in self.cursor.execute("SELECT * FROM stocks"):
                print("{:20s}{:7s}{:7d}{:10d}".format(row[0],row[1],row[2],row[3]));
        elif table == "users":
            for row in self.cursor.execute("SELECT * FROM users"):
                print("{:15s}{:10s}{:10d}".format(row[0],row[1],row[2]));
        else:
            flag = 0;
            for row in self.cursor.execute(f"SELECT * FROM {table}"):
                print("{:15s}{:7s}{:10d}".format(row[0],row[1],row[2]));
                flag = 1;
            return flag;

    
    def select_row(self,table,param):
        if table == "users":
            self.cursor.execute("SELECT * FROM users WHERE login = :login",{"login":param});
            row = self.cursor.fetchone();
            return row;
        elif table == "stocks":
            self.cursor.execute("SELECT * FROM stocks WHERE company = :company",{"company":param});
            row = self.cursor.fetchone();
            return row;
        else:
            self.cursor.execute("SELECT * FROM users WHERE login = :login",{"login":table});
            row = self.cursor.fetchone();
            if row == None:
                return 0;
            else:
                self.cursor.execute(f"SELECT * FROM {table} WHERE company = :company",{"company":param});
                row = self.cursor.fetchone();
                return row;

    def check_user(self,param1,param2):
        self.cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?",(param1,param2));
        row = self.cursor.fetchone();
        return row;

    def insert_row(self,table,param1,param2,param3):
        if table == "users":
            self.cursor.execute("INSERT INTO users VALUES (?,?,?)",(param1,param2,param3));
            self.conn.commit();
        else:
            self.cursor.execute(f"INSERT INTO {table} VALUES (?,?,?)",(param1,param2,param3));
            self.conn.commit();

    def update_row(self,table,column,param1,param2):
        if table == "stocks":
            self.cursor.execute(f"UPDATE stocks SET {column} = ? WHERE company = ?",(param1,param2));
            self.conn.commit();
        elif table == "users":
            self.cursor.execute(f"UPDATE users SET {column} = ? WHERE login = ?",(param1,param2));
            self.conn.commit();
        else:
            self.cursor.execute(f"UPDATE {table} SET {column} = ? WHERE company = ?",(param1,param2));
            self.conn.commit();

    def delete_row(self,table,param1,param2):
        self.cursor.execute(f"DELETE FROM {table} WHERE company = ? AND id = ?",(param1,param2));
        self.conn.commit();
