# Distributed Databases Project
 
MSc Student in *Software Engineering*  
LUT University  

---

## Project Overview
This project demonstrates a distributed database system implemented using **Microsoft SQL Server** and **Python (PyODBC)**.

The system includes:
- **One central database:** `db_central`  
- **Three local databases:** `db_kouvola`, `db_lahti`, `db_lappeenranta`  

Each database contains at least **five tables** and **ten records**.  
Half of the data is **replicated** (shared) across databases, while the other half is **fragmented** (unique to each location).  
The project allows users to **select a database**, **view data**, **update records**, and **create backups**.

---

## Database Structure

| Database | Description |
|-----------|--------------|
| `db_central` | Contains complete user and department information shared by all local databases. |
| `db_kouvola` | Local database for the Kouvola campus, including student and service data. |
| `db_lahti` | Local database for the Lahti campus. |
| `db_lappeenranta` | Local database for the Lappeenranta campus. |

Each database contains the following tables:

- `Appointment`  
- `Student`  
- `Consultant`  
- `Feedback`  
- `Ticket`

---

## Data Replication and Fragmentation
- **Replicated data:** shared across all databases (e.g., first 5 users and departments).  
- **Fragmented data:** unique to each local database (e.g., student and feedback records specific to each campus).  

Example:
> In each `Student` table, the first 5 records are the same in all databases, and the last 5 are different for each location.

---

## Technologies Used
- **Microsoft SQL Server**
- **Python 3.10+**
- **PyODBC library**

---

## Program Features

1. **Database Selection**
   - When the program starts, it asks the user to choose which campus database to connect to.
   - Example:
     ```
     Select a campus database:
     1. Kouvola
     2. Lahti
     3. Lappeenranta
     ```
   - Once selected, the program connects and confirms:
     ```
     Connected to Kouvola database successfully!
     ```

2. **Data Viewing**
   - Displays student information by joining local `Student` data with `User` and `Department` from `db_central`.

3. **Data Updating**
   - Allows editing student name and email:
     ```
     Enter StudentID to update:
     Enter new First Name:
     Enter new Last Name:
     Enter new Email:
     ```
   - Confirms update:
     ```
     StudentID information updated successfully!
     ```

4. **Automatic Database Backup**
   - Each time the program runs, it creates a backup of the **central database (`db_central`)**.  
   - The backup is stored in:
     ```
     C:\BackupCentral\
     ```
   - Example:
     ```
     db_central_backup_20251109_173255.bak
     ```

---

## How to Run the Program

### Prerequisites
- Python installed  
- SQL Server with the four databases restored  
- `pyodbc` installed via:
  ```bash
  pip install pyodbc
  ```

### Run
From the terminal or VS Code:
```bash
python main.py
```

---

## How to Restore Databases

You can restore the databases using the provided `.bak` files or SQL script.

### Option 1: Using SQL Server (.bak files)
1. Open **SQL Server Management Studio (SSMS)**  
2. Right-click on *Databases → Restore Database*  
3. Choose *Device → Browse*  
4. Select:
   - `db_central.bak`
   - `db_kouvola.bak`
   - `db_lahti.bak`
   - `db_lappeenranta.bak`
5. Click **OK** and restore each.

### Option 2: Using SQL Script
Alternatively, run `db_restore_script.sql` to recreate tables and insert dummy data.

---

## Example Output

```
Select a campus database:
1. Kouvola
2. Lahti
3. Lappeenranta
Enter your choice (1-3): 1

Connected to Kouvola database successfully!

--- Student Data ---
(1, 'Aino', 'Korhonen', 'aino.k@lut.fi', 'Mechanical Engineering', 'MSc', '2023-08-20')

=== Starting Backup for db_central ===
Backup completed successfully! File saved at: C:\BackupCentral\db_central_backup_20251109_173255.bak

--- Update Student and User Information ---
Enter StudentID to update: 1
Enter new First Name: Anna
Enter new Last Name: Korhonen
Enter new Email: anna.k@lut.fi

StudentID 1 information updated successfully!
```

---

## Video Demonstration

The demo video shows:
1. The three local databases and one central database in SQL Server  
2. Running the Python script  
3. Selecting and connecting to a campus database  
4. Displaying and updating student data  
5. Viewing the updated record in SQL Server  
6. Showing the generated backup file  

---

## Summary
This project demonstrates a small distributed database environment with both replication and fragmentation.  
The Python program enables multi-database access, interactive data viewing and updating, and automatic central database backup.  
