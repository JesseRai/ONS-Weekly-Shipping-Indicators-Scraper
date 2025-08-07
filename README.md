# ONS Weekly Shipping Indicators Scraper

This Python script automatically scrapes the latest **Weekly Shipping Indicators** dataset from the [UK Office for National Statistics (ONS)](https://www.ons.gov.uk/economy/economicoutputandproductivity/output/datasets/weeklyshippingindicators), downloads the latest `.xlsx` file, and converts all sheets into `.csv` files.

## Features

- Automatically detects the most recent `.xlsx` file based on the date in the filename.
- Downloads the file directly from the ONS website.
- Converts each Excel sheet into a separate CSV file for easy analysis.

## Requirements

- Python 3.7+
- `requests`
- `pandas`
- `beautifulsoup4`
- `lxml` (optional but recommended for better Excel parsing)

Install dependencies using:

```bash
pip install requests pandas beautifulsoup4 lxml
```

## Usage

Clone the repository and run:

```bash
python ons_shipping_scraper.py
```

This will:

1. Print a list of all `.xlsx` links on the page with their parsed dates.
2. Download the latest one.
3. Save each worksheet in the Excel file as a `.csv` file in the current directory.

## File Structure

- `ONS.py`: Main Python script.
- Output: One `.csv` file per Excel sheet from the downloaded dataset.

## Example Output

```bash
Detected Excel files with dates:
/economy/.../weeklyshippingindicators060825.xlsx --> 2025-08-06
Downloading the latest file: https://www.ons.gov.uk/economy/.../weeklyshippingindicators060825.xlsx
Saved sheet 'Summary' as CSV: Summary.csv
Saved sheet 'Data' as CSV: Data.csv
...
```

## Notes

- The script uses regex to detect dates in filenames. If the format changes on the ONS website, it may need adjustment.
- By default, it saves the Excel file and CSVs in the same directory as the script.
