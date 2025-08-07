import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from datetime import datetime


def date_extractor(href):

    match = re.search(r'(\d{6})', href)
    if match:
        try:
            return datetime.strptime(match.group(1), "%d%m%y")
        except ValueError:
            return datetime.min
    return datetime.min

def get_latest_file_url():
    base_url = "https://www.ons.gov.uk/economy/economicoutputandproductivity/output/datasets/weeklyshippingindicators"

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. HTTP Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    file_links = [link['href'] for link in links if link['href'].endswith('.xlsx')]

    if not file_links:
        print("No Excel file links found on the page.")
        return None

    file_links.sort(key=date_extractor, reverse=True)

    print("Detected Excel files with dates:")
    for link in file_links:
        print(f"{link} --> {date_extractor(link).strftime('%Y-%m-%d')}")

    latest_file_url = file_links[0]
    full_url = f"https://www.ons.gov.uk{latest_file_url}"
    return full_url

def download_and_save_as_csv():
    file_url = get_latest_file_url()
    if not file_url:
        return

    print(f"Downloading the latest file: {file_url}")

    response = requests.get(file_url)
    if response.status_code == 200:
        excel_filename = file_url.split('/')[-1]
        with open(excel_filename, 'wb') as file:
            file.write(response.content)

        xls = pd.ExcelFile(excel_filename)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            csv_filename = f"{sheet_name}.csv"
            df.to_csv(csv_filename, index=False)
            print(f"Saved sheet '{sheet_name}' as CSV: {csv_filename}")
    else:
        print(f"Failed to retrieve the file. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    download_and_save_as_csv()
