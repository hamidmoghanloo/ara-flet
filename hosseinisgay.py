import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
    
""")

users = cursor.fetchall()

for user in users:
    print(user)

cursor.close()
conn.close()