# 📧 Email Cleaning Pipeline

A simple Python-based **Data Engineering** project that:

- Fetches 1000 random user emails from a public API
- Generates a mix of valid and invalid email formats
- Validates emails using custom logic
- Removes duplicates by checking saved email files
- Saves valid and invalid emails into separate CSV files

---

## 📁 Project Structure

```
data_engineer/
├── data/
│   ├── valid_emails.csv         # Stores valid emails
│   └── invalid_emails.csv       # Stores invalid emails
│
├── main/
│   ├── pipeline.py              # Main runner script
│   ├── email_generator.py       # Fetches + generates emails
│   ├── email_validator.py       # Email validation logic
│   └── file_utils.py            # File read/write utilities
│
└── README.md
```

---

## ⚙️ How It Works

1. Fetches random user data from `https://randomuser.me/api/`
2. Generates emails with a 70% chance of being valid
3. Applies custom validation rules (must include `@`, `.` in right positions)
4. Filters out already-saved emails (no duplicates)
5. Saves results to two separate files:
   - `data/valid_emails.csv`
   - `data/invalid_emails.csv`

---

## 🚀 How to Run

Make sure you have Python 3.x installed, then:

```bash
# Move into project directory
cd data_engineer

# Run the main pipeline
python main/pipeline.py
```

---

## 🧪 Example Output

```text
✅ Done. Added 703 valid and 297 invalid emails.
```

---

## 📦 Requirements

- Python 3.x
- `requests` library

Install it via pip:
```bash
pip install requests
```

---
