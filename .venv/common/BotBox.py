import mysql.connector

class BotBox:
    def __init__(self,host,username,password,database):
        self.host = host
        self.username = username
        self.password = password
        self.db=database

    def connect(self):
        connection=mysql.connector.connect(
            host=self.host,
            user=self.username,
            passwd=self.password,
            database=self.db
        )
        
        print(connection)
        
        return connection
    
    def register_user(self,values):
        
        database=self.connect()
        init_cursor=database.cursor()
        
        sql=f'INSERT INTO `users`(`id`, `phone_number`, `shopname`) VALUES (%s,%s,%s)'
        val=(values[0],values[1],values[2])
        
        init_cursor.execute(sql,val)
        
        database.commit()
        
        
    def add_transaction(self, values):
        
        database = self.connect()
        
        init_cursor = database.cursor()
        
        sql = f'INSERT INTO `transactions`(`userid`, `id`, `date`, `category`, `description`, `amount`) VALUES (%s, %s, NOW(), %s, %s, %s)'
        
        val = (values[0], values[1], values[2], values[3], values[4])  # Adjusted to match the number of values passed
        
        init_cursor.execute(sql, val)
        
        database.commit()
            
    
    
botbrain=BotBox("localhost","root","5585Anesuchigov@","shopmanager")

add_transaction=botbrain.add_transaction((1, 0, 'cash-in', 'photocopying', 2.00))

print(add_transaction)


# botbrain.register_user((0,"+263788528993","test-shop"))

# db=testConection.connect()


