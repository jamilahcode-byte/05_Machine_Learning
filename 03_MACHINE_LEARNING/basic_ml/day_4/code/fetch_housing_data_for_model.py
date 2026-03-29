#Step1: import modules 
import os 
import tarfile 
import requests
import pandas as pd 

#Step2: url & path 
HOUSING_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/" + "datasets/housing/housing.tgz"
HOUSING_PATH = os.path.join("datasets", "housing")

#Step 3: Function 
def fetch_housing_data(url=HOUSING_URL, path=HOUSING_PATH):
    #Step 4: Error handling
    try:
        #Step 5: Create folder
        os.makedirs(path, exist_ok=True)

        #Step 6: File path 
        tgz_path = os.path.join(path, "housing.tgz")

        #Step 7: Download request 
        response = requests.get(url, stream=True)

        #Step 8: Checks errors 
        response.raise_for_status()

        #Step 9: File size
        total_size = int(response.headers.get("content-length", 0))

        #Step 10: Track download 
        downloaded = 0   

        #Step 11: save file 
        with open(tgz_path, "wb") as file:

            #Step 12: Download in chunks 
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    #Step 13: Write chunk 
                    file.write(chunk)

                    #Step 14: Update progress 
                    downloaded += len(chunk)   

                    #Step 15: Calculate % 
                    percent = (downloaded / total_size) * 100 if total_size else 0 

                    #Step 16: Print progress 
                    print(f"Downloading: {percent:.2f}%", end="\r", flush=True)

        #Step 17: Done message
        print("\nDownload complete!")

        #Step 18:Extract file 
        with tarfile.open(tgz_path) as housing_tgz:
            housing_tgz.extractall(path=path, filter="data")

        #Step 19: Load data
        csv_path = os.path.join(path, "housing.csv")
        df = pd.read_csv(csv_path)

        #Step 20: Show data 
        print(df.head()) 

        #Step 21: Return data 
        return df

    #Step 22: Catch errors
    except Exception as e:
        print("Error occurred:", e)

#Step 23: Run function 
fetch_housing_data()