# Used Car Price Scraper

A Python web scraping project that collects used car information from **TrueCar** and exports the results to a CSV file.

> **Disclaimer**
>
> This project is intended for educational purposes only. The website structure may change over time, which can affect the scraper.

---

## Overview

The application asks the user for a car model, sends an HTTP request to TrueCar, extracts vehicle information using BeautifulSoup, and saves the results to a CSV file.

---

## Features

- Web scraping with BeautifulSoup
- HTTP requests using Requests
- CSV export
- Error handling
- User input
- Automatic file generation

---

## Technologies

- Python
- Requests
- BeautifulSoup4
- CSV

---

## Project Structure

```
Used_Car_Price_Scraper/
│
├── car_scraper.py
├── requirements.txt
├── README.md
├── .gitignore
└── sample_output.csv
```

---

## Installation

```bash
git clone https://github.com/SH-Mizani/Used_Car_Price_Scraper.git

cd Used_Car_Price_Scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program:

```bash
python car_scraper.py
```

Example:

```
Enter car name:
toyota-camry
```

The scraper will generate:

```
toyota-camry_cars_info.csv
```

---

## Output

The CSV file contains:

| Car Name | Price | Mileage |
|----------|-------|----------|

---

## Learning Objectives

- Web scraping
- HTML parsing
- HTTP requests
- CSV processing
- Error handling in Python

---

## Author

**Setareh Mizani**

Computer Engineering Student