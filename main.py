import mysql.connector
import random

class DatabaseConnection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='oop_bank')
            self.cur = self.conn.cursor()
            print('Connection successful')
        except mysql.connector.Error as err:
            print('Connection failed:', err)

db = DatabaseConnection()

class Bank:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.home()
    
    def home(self):
        login_or_signup = input('1. Enter 1 to login\n2. Enter 2 to signup.\n')
        if login_or_signup == '1':
            self.login()
        elif login_or_signup == '2':
            self.to_db()
        else:
            print('Enter valid input\n')
    
    def register(self):
        name = input('Enter Your name: \n')
        email = input('Enter your email: \n')
        pin = input('Enter 6 number pin: \n')

        return name, email, pin

    def to_db(self):
        name, email, pin = self.register()
        user_bank_id = random.randint(10000, 10000000)

        sql = 'INSERT INTO user_info(user_name, pin, balance, email, user_bank_id) VALUES (%s, %s, %s, %s, %s)'
        datas = (name, pin, self.balance, email, user_bank_id)

        db.cur.execute(sql, datas)
        db.conn.commit()
        print(f'Your bank id is {user_bank_id}\n')
        print('Register successfully\n')
    
    def login(self):
        user_id_input = input('Enter your bank id: \n')
        user_pin = input('Enter your pin: \n')

        sql = 'SELECT * FROM user_info WHERE user_bank_id = %s'
        db.cur.execute(sql, (user_id_input,))
        temp_id = db.cur.fetchone()

        if temp_id != None:
            name, self.pin, email, self.balance, user_id, user_bank_id = temp_id

            if user_bank_id == int(user_id_input) and self.pin == user_pin:
                print(f'Welcome {name}')
                self.menu(user_bank_id)
            else:
                print('Pin or user id may be incorrect\n')
                self.login()
        else:
            print('Invalid User\n\n')
            self.home()
    
    def menu(self, user_bank_id):
        option = input('1. Enter 1 to deposit balance.\n2. Enter 2 to withdraw balance.\n3. Enter 3 to check balance.\n4. Enter 4 to change pin.\n5. Enter 5 to delete account.\n6. Enter q to quit\n')

        if option == '1':
            self.deposit(user_bank_id)
        elif option == '2':
            self.withdraw(user_bank_id)
        elif option == '3':
            self.check_balance()
        elif option == '4':
            self.change_pin(user_bank_id)
        elif option == '5':
            self.delete_acc(user_bank_id)
        elif option == 'q':
            self.home()
        else:
            print('Invalid Option\n\n')
            self.menu(user_bank_id)
    
    def deposit(self, user_bank_id):
        amt = int(input('Please provide the amount you wish to deposit.\n'))
        self.balance += amt

        sql = 'UPDATE user_info SET balance = %s where user_bank_id = %s'
        db.cur.execute(sql, (self.balance, user_bank_id))
        db.conn.commit()
        print(f'Successfully deposited {amt} in your account\n')
        self.menu(user_bank_id)
    
    def withdraw(self, user_bank_id):
        amt = int(input('Please provide the amount you wish to withdraw.\n'))
        if amt <= self.balance:
            self.balance -= amt

            sql = 'UPDATE user_info SET balance = %s where user_bank_id = %s'
            db.cur.execute(sql, (self.balance, user_bank_id))
            db.conn.commit()
            print(f'Successfully withdrew {amt} from your account.\n')
        
        else:
            print('Insufficent Balance.\n')
        
    def check_balance(self):
        print(f'Your Current balance is {self.balance}\n')
    
    def change_pin(self, user_bank_id):
        old_pin = input('Enter old pin: ')
        if old_pin == self.pin:
            new_pin = input('Enter new pin: ')
            sql = 'UPDATE user_info SET pin = %s where user_bank_id = %s'
            db.cur.execute(sql, (new_pin, user_bank_id))
            db.conn.commit()
        else:
            print('Please enter your previous PIN correctly.\n')
        
    def delete_acc(self, user_bank_id):
        user_pin = input('Enter pin to delete your account:\n')
        
        if user_pin == self.pin and self.balance == 0:
            option = input('Do you really want to delete your account?(y|n) ').lower()
            if option == 'y':
                sql = 'DELETE FROM user_info WHERE user_bank_id = %s'
                db.cur.execute(sql, (user_bank_id, ))
                db.conn.commit()
                print('Account Deleted successfully\n')
        else:
            print('To delete your account, please ensure your PIN is entered correctly and that your account balance is zero.\n')


while True:
    b = Bank()
    choice = input('Enter c to continue and q to quit\n').lower()
    if choice == 'c':
        b = Bank()
    elif choice == 'q':
        break
    else:
        print('Wrong input')