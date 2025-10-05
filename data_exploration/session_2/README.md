# 🧠 Data Scraping Projects – Amazon Electronics & Movies

This repository contains two Jupyter Notebook projects focused on **web scraping** real-world data and exporting it into clean, structured **CSV datasets**.  
Both projects demonstrate the use of Python for collecting, cleaning, and organizing data for later analysis.

---

## 📂 Project Structure

```
├── amazon_electronics.ipynb     # Scrapes product data from Amazon Electronics
├── movies.ipynb                 # Scrapes movie-related data (titles, ratings, etc.)
├── amazon.csv                   # exported CSV files
├── top_200_movies.csv           # exported CSV files
└── README.md                    # Project documentation
```

---

## 🔍 Project 1: Amazon Electronics Scraper

**Goal:**  
Extract detailed information about electronics products listed on Amazon, such as:
- Product name  
- Price  
- Rating  
- Number of reviews  
- Product URL  

**Output:**  
The notebook generates a CSV file (`amazon_electronics.csv`) containing all the scraped product data, ready for analysis or integration into data pipelines.

**Tech Stack:**  
- Python  
- `requests`, `BeautifulSoup4` for web scraping  
- `pandas` for data cleaning and export  
- `time`, `random` for polite scraping delays  

---

## 🎬 Project 2: Movies Scraper

**Goal:**  
Scrape movie-related information from an online movie database (e.g., IMDb, TMDB, etc.), including:
- Movie title  
- Year  
- Genre  
- Rating  
- Description  

**Output:**  
A structured CSV file (`movies.csv`) containing movie metadata for further exploration and visualization.

**Tech Stack:**  
- Python  
- `requests`, `BeautifulSoup4`  
- `pandas` for organizing the data  

---

## 🧾 Output Examples

| Product | Price | Rating | Reviews | URL |
|----------|--------|---------|----------|-----|
| Example Product | $199.99 | 4.5 | 1250 | [View on Amazon](https://amazon.com/example) |

| Movie | Year | Genre | Rating | Description |
|-------|------|--------|---------|--------------|
| Example Movie | 2024 | Action | 8.1 | A thrilling story of... |

---