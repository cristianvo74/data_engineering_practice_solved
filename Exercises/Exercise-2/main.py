import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_soup_object(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def find_file_url(soup, url):
    time_stamp = '2024-01-19 10:02'
    table = soup.find('table')
    found = False
    for tr in table.find_all('tr'):
        for td in tr.find_all('td'):
            if time_stamp in td.text:
                found = True
                break
        if found:
            break

    if found:
        a_tag = tr.find('a')
        file_url = urljoin(url, a_tag['href'])
    return file_url

def download_file(file_url):
    response = requests.get(file_url)
    file_path = 'file.csv'
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
    return file_path


def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def find_max_temp_records(df):
    max_temp = df['HourlyDryBulbTemperature'].max()
    max_temp_records = df[df['HourlyDryBulbTemperature'] == max_temp]
    return max_temp_records



def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    soup = get_soup_object(url)
    file_url = find_file_url(soup,url)
    file_path = download_file(file_url)
    df = read_csv(file_path)
    records = find_max_temp_records(df)
    print(records)
    pass


if __name__ == "__main__":
    main()
