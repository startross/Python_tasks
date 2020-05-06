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
            self.cursor.execute("INSERT INTO stocks VALUES ('Apple','AAPL','425','10000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Bank of America','BAC','40','8000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Microsoft','MSFT','306','15000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Pfizer','PFE','67','3000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Facebook','FB','308','12000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Twitter','TWTR','47','30000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Intel','INTC','108','17000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('NVIDIA','NVDA','486','9000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('The Gap','GPS','11','60000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('The Walt Disney','DIS','186','20000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Starbucks','SBUX','127','8000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('General Motors','GM','36','15000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Oracle','ORCL','98','13000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('HP','HPQ','27','19000')");
            self.cursor.execute("INSERT INTO stocks VALUES ('Visa','V','302','7000')");
            self.conn.commit();
        elif table == "users":
            self.cursor.execute("INSERT INTO users VALUES ('startross','12345','10000')");
            self.cursor.execute("INSERT INTO users VALUES ('mindhunter','23456','5000')");
            self.cursor.execute("INSERT INTO users VALUES ('jonny','34567','12000')");
            self.cursor.execute("INSERT INTO users VALUES ('ninja','45678','7000')");
            self.cursor.execute("INSERT INTO users VALUES ('kelly','56789','4000')");
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
