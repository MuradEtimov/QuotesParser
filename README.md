# Quotes Parser

This project scrapes quotes from [quotes.toscrape.com](https://quotes.toscrape.com), collects the quote text, author information (name, birth date, and location), and tags, and saves the data into an Excel file (`Quotes.xlsx`).

## Features
- Scrapes multiple pages of quotes
- Extracts author details
- Saves data in Excel format
- Cross-platform launch scripts for Linux and Windows

## Technologies
- Python 3.12
- requests
- BeautifulSoup4
- lxml
- XlsxWriter

## Project Structure

- `Exel_lol.py` – Main scraping script  
- `Les1.py` – Module with scraping functions  
- `run_test.sh` – Linux launch script  
- `run_test.bat` – Windows launch script  
- `requirements.txt` – Python dependencies  
- `README.md` – Project documentation  

## How to Run

### On Linux / Mac
1. Make the script executable (first time only):

```bash
chmod +x run_test.sh
```

Run the script:
```
./run_test.sh
```
# On Windows
Double-click run_test.bat or run it from Command Prompt:
```
run_test.bat
```
After running, the Excel file Quotes.xlsx will be created in the project folder.

# Installing Dependencies Manually

If you prefer to set up manually:

Create and activate a virtual environment:

# Linux / Mac
```
python -m venv venv
source venv/bin/activate
```
# Windows
```
python -m venv venv
venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the main script:
```
python Exel_lol.py
```
Notes

The Excel file is generated automatically; you don’t need to create it manually.

Linux users can use run_test.sh, Windows users can use run_test.bat for one-click execution.

Generated files (Quotes.xlsx, temp_env, __pycache__) should not be included in GitHub and are ignored via .gitignore.


