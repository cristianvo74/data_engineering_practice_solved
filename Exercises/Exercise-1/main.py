import requests
import zipfile
import os


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_file(url:str, download_path: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        local_filename = os.path.join(download_path, url.split('/')[-1])
        with open(local_filename,'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return local_filename
    except Exception as e:
        print(f"URL: {url} does not exists")
        return ""


def extract_file(file_path:str, extract_path) -> None:
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall(extract_path)
        print(f"Extracted {file_path}")
    except Exception as e:
        print(f"Error {e} has ocurred while extracting {file_path}")
    pass


def remove_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error {e} has ocurred while deleting {file_path}")
    pass

def main():
    
    download_path = 'downloads'
    extract_path = 'downloads'

    if not os.path.exists(download_path):
        os.mkdir(download_path)

    for url in download_uris:
        file_path = download_file(url, download_path)
        if file_path:
            extract_file(file_path, extract_path)
            remove_file(file_path)
        

    

if __name__ == "__main__":
    main()
