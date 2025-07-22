# 🧰 Python Utility Module: `my_utils`

This project contains a reusable Python module `my_utils.py` with several beginner-friendly utility functions. It also includes a main script `main.py` for testing the functions and a `user_database.py` file for login functionality.

---

## 📁 Files Structure

```
project/
│
├── main.py              # Main script to run all features
├── my_utils.py          # Custom module with multiple utility functions
├── user_database.py     # Mock user database for login
└── README.md            # Documentation
```

---

## 🔧 Features

### String Utilities
- `find_string(text)`: Print indexes of letter `'i'` in a string.
- `nvowles(word)`: Count and print number of vowels in a word.

### Math Utilities
- `m_table(x)`: Print multiplication tables up to `x`.
- `m_table_list(x)`: Return multiplication tables in nested lists.
- `sort_ascending(arr)`: Sort a list in ascending order.
- `sort_descending(arr)`: Sort a list in descending order.

### Mario Pyramids
- `sample_mario(x)`: Print a Mario-style pyramid.
- `mario_list(x)`: Print pyramid using a list structure.

### User Interaction
- `user_check(name)`: Validate and welcome user.
- `check_login(username, password)`: Check credentials against a static database.
- `email_validate(email)`: Validate email format with 5 retry attempts.

---

## ▶️ How to Run

1. Clone this repo:
```bash
git clone <your-repo-url>
cd project
```

2. Run the `main.py`:
```bash
python main.py
```

Follow the prompts to test different utilities interactively.

---

## 🗃️ Sample Output

```
Enter a string: this is it
in index :  2
in index :  5
in index :  8

Enter number: 3
  *
 **
***

Enter your number: 3
1*1=1
2*1=2
2*2=4
3*1=3
3*2=6
3*3=9

...

Login successful!
Email is valid.
```

---

## ✅ Notes

- This project is beginner-friendly.
- No external libraries required.
- All logic implemented using native Python.

---
