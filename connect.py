import pyodbc

server = 'N/A.database.windows.net'
database = 'N/A'
username = 'N/A'
password = 'N/A'

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Interns")

print("-" * 80)
print("Intern Database")
print("-" * 80)

for intern_id, name, role, email in cursor.fetchall():
    print(f"ID    : {intern_id}")
    print(f"Name  : {name}")
    print(f"Role  : {role}")
    print(f"Email : {email}")
    print("-" * 80)

conn.close()