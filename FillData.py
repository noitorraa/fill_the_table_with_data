import psycopg2 
import random 

conn = psycopg2.connect( 
    database="postgres", 
    user="postgres", 
    password="Passw0rd", 
    host="localhost", 
    port="5432" 
) 

pol = [1,2] 
imia = ["Егор", "Алексей", "Андрей", "Максим", "Денис", "Антон", "Никита", "Борис", "Данил", "Евгений", "Арнольд", "Аркадий", "Борислав", "Валентин", "Валилий"] 
familia = ["Алексеев", "Андеев", "Денисов", "Максимов", "Крючков", "Брюхов", "Конюк", "Боженов", "Чирков", "Абрамчук","Абрашин","Абрасимов"] 
otchestvo = ["Максимович", "Андреевич", "Денисович", "Егорович", "Михайлович", "Иванович", "Семенович"] 
Job_title = ["Менеджер", "Директор", "Администратор"]
cur = conn.cursor() 

for i in range(100): 
    cur.execute(f"insert into leasing_company.\"Employees\"(\"Name\", \"Last_name\", \"Middle_name\", \"Job_title\", \"Salary\") values (\'{random.choice(imia)}\',\'{random.choice(familia)}\',\'{random.choice(otchestvo)}\',\'{random.choice(Job_title)}\', \'{random.randint(50000, 100000)}\')") 
     
conn.commit() 
cur.close() 
conn.close()
