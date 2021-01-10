from MySQL_fn import * 

def create_table():
    Tables.create("users", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, use_command VARCHAR(100) NOT NULL, first_value TEXT, second_value TEXT")

def create_user_table(user_id):
    Tables.create(f"user_{user_id}", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, first_value TEXT, second_value TEXT")

def add_user(user_id):
    users = Tables('users')
    try:
        check_user_in_table = users.select('id', 'id')
    except:
        users.insert('id, use_command, first_value, second_value', f'"{user_id}","","",""')
        create_user_table(user_id)