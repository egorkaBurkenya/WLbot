from MySQL_fn import * 

def create_table():
    Tables.create("users", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, use_command VARCHAR(100) NOT NULL, first_value TEXT, second_value TEXT")

def create_user_table(user_id):
    Tables.create(f"user_{user_id}", "id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, first_value TEXT, second_value TEXT")

def add_user(user_id):
    users = Tables('users')
    try:
        users.select('id', 'id')
    except:
        users.insert('id, use_command, first_value, second_value', f'"{user_id}","","",""')
        create_user_table(user_id)

def add_new_value(user_id, position, value):
	table = Tables('users')
	if position == 1:
		table.update(f'first_value = "{value}"', f'id = "{user_id}"')
	if position == 2:
		table.update('second_value', f'"{value}"')

def set_use_command(user_id, command):
	users = Tables('users')
	users.update(f'use_command = "{command}"', f'id = "{user_id}"') 

def cheack_use_command(user_id, command):
	users = Tables('users')
	try:
		use_command = users.select('use_command', f'id = "{user_id}"')
		if use_command['use_command'] == command: 
			return True
		else:
			logger.info(use_command, '|', command)
			return False 
	except:
		logger.info('error') 
		return False 

def check_value(user_id, value):
	try:
		table = Tables('users')
		table.select('first_value', f'id = "{user_id}"')
		return False
	except:
		return True
