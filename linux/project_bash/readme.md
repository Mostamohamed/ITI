# 🗄️ Bash Shell Script Database Management System (DBMS)

A simple **Database Management System** implemented entirely in **Bash shell scripting**.  
This project simulates basic DBMS operations like creating databases, tables, inserting records, selecting, updating, and deleting — all from the terminal.

---

## ✨ Features

### Main Menu
- 📂 **Create Database**  
- 📜 **List Databases**  
- 🔌 **Connect to Database**  
- ❌ **Drop Database**

### Inside a Database
- 🏗️ **Create Table** (with columns, data types, and primary key)  
- 📋 **List Tables**  
- ❌ **Drop Table**  
- ➕ **Insert Into Table** (with data type + PK validation)  
- 🔍 **Select From Table** (formatted output)  
- 🗑️ **Delete From Table** (by primary key)  
- ✏️ **Update Table** (non-PK columns only)

---

## 🛠️ Implementation Details
- Databases are stored as **directories** under `./DB/`.  
- Each table is a **file**, and its schema is stored in a hidden **metadata file**:
  ```
  users             # table data
  .users.meta       # metadata (col_name:type:is_pk)
  ```
- Data types supported:  
  - `int` (integer values only)  
  - `string` (text without `:`)  
- Enforces **primary key uniqueness**.  
- Clean and aligned **select output** using `awk`.  

---


## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bash-dbms.git
   cd bash-dbms
   ```

2. Make scripts executable:
   ```bash
   chmod +x DataBase_creation.sh Tables.sh
   ```

3. Start the system:
   ```bash
   ./DataBase_creation.sh
   ```

---

## 📚 Usage Example

### Create Database
```
Enter database name: testdb
Database 'testdb' created.
```

### Create Table
```
Enter table name: users
Enter number of columns: 3
Column 1 name: id
Select data type for column id: int
Should id be the primary key? yes
Column 2 name: name
Select data type for column name: string
Column 3 name: age
Select data type for column age: int
Table 'users' created successfully.
```

### Insert Data
```
Enter table name: users
Enter value for column 'id' (int): 1
Enter value for column 'name' (string): mostafa
Enter value for column 'age' (int): 24
Record inserted successfully.
```

### Select Data
```
id             name           age            
1              mostafa         24             
```

---
