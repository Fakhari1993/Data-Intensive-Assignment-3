while True:
 import pyodbc
 import os
 from datetime import datetime


# Database connections

 connections = {
    "Kouvola": "Driver={SQL Server};Server=.;Database=db_kouvola;Trusted_Connection=yes;",
    "Lahti": "Driver={SQL Server};Server=.;Database=db_lahti;Trusted_Connection=yes;",
    "Lappeenranta": "Driver={SQL Server};Server=.;Database=db_lappeenranta;Trusted_Connection=yes;"
}


# Database selection

 print("Select a campus database:")
 for i, name in enumerate(connections.keys(), start=1):
    print(f"{i}. {name}")

 choice = int(input("Enter your choice (1-3): "))
 db_name = list(connections.keys())[choice - 1]

# Connect to the selected database to display data
 conn = pyodbc.connect(connections[db_name])
 cursor = conn.cursor()
 print(f"\nConnected to {db_name} database successfully!")

# Display student information
 cursor.execute("""
SELECT s.StudentID, u.FirstName, u.LastName, u.Email, d.DeptName, s.StudyLevel, s.Enrolledat
FROM dbo.Student AS s
INNER JOIN db_central.dbo.[User] AS u ON s.UserID = u.UserID
INNER JOIN db_central.dbo.Department AS d ON s.DeptID = d.DeptID
""")
 rows = cursor.fetchall()

 print("\n--- Student Data ---")
 for row in rows:
    print(row)


# Backup from db_central

 print("\n=== Starting Backup for db_central ===")

 database = 'db_central'
 backup_dir = r"C:\BackupCentral"

 if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
 backup_conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=.;DATABASE=master;Trusted_Connection=yes;',
    autocommit=True
)

 backup_cursor = backup_conn.cursor()
 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
 backup_path = os.path.join(backup_dir, f"{database}_backup_{timestamp}.bak")

 try:
    print(f"Backing up database: {database} ...")
    backup_cursor.execute(f"""
    BACKUP DATABASE [{database}]
    TO DISK = N'{backup_path}'
    WITH INIT, STATS = 5
    """)
    print(f"Backup completed successfully! File saved at: {backup_path}\n")
 except Exception as e:
    print(f"Backup failed: {e}\n")

 backup_cursor.close()
 backup_conn.close()
 print("Backup process finished!\n")


# Update Users Table

 print("--- Update Student and User Information ---")
 student_id = input("Enter StudentID to update: ")
 new_fname = input("Enter new First Name: ")
 new_lname = input("Enter new Last Name: ")
 new_email = input("Enter new Email: ")


 if not new_fname and not new_lname and not new_email or not student_id:
        print("\n Nothing was updated.")
        exit()
 else:
  update_user = """
UPDATE u
SET u.FirstName = ?, u.LastName = ?, u.Email = ?
FROM db_central.dbo.[User] AS u
INNER JOIN dbo.Student AS s ON u.UserID = s.UserID
WHERE s.StudentID = ?;
"""

 cursor.execute(update_user, (new_fname, new_lname, new_email, student_id))
 conn.commit()
 print(f"\n StudentID {student_id} information updated successfully!")

 cursor.close()
 conn.close()

 repeat = input("\nDo you want to restart the program? (y/n): ").lower()
 if repeat != 'y':
        print("\nExiting program...")
        break
