# 📧 Email Generator & Validator

This Python script generates 1000 random email addresses (both valid and invalid), validates them, and saves them into separate CSV files.

---

## 🚀 Features

- Uses the `randomuser.me` API to fetch user data.
- Creates emails with a 70/30 split of valid and invalid formats.
- Custom email validation logic (not using regex).
- Avoids duplicates by checking existing CSV files.
- Saves results into:
  - `valid_emails.csv`
  - `invalid_emails.csv`

---

## 🛠️ How It Works

1. **Fetch Users:** Get 1000 users from API.
2. **Generate Emails:** Create fake emails using user data.
3. **Validate Emails:** Custom logic to check structure.
4. **Check Duplicates:** Reads existing CSVs to skip old entries.
5. **Save Results:** Writes new valid/invalid emails to files.

---

## 📂 File Output

Each run appends **new** emails only.

- `valid_emails.csv` – All verified emails.
- `invalid_emails.csv` – All invalid formats.

Each file includes a simple header:
```csv
email
example@gmail.com
invalid@com
```

---

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Install `requests` library if not already:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python your_script.py
   ```

---

## ✅ Sample Output

```
✅ Done. Added 693 new valid and 307 new invalid emails.
```

---

## 📄 License

Free to use for educational and testing purposes.