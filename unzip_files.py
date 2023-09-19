from zipfile import ZipFile
import os, json

DATA_PATH = "data"
year_path = "2013"

with open("zip_file.json", "r") as f:
    zip_file = json.load(f)

data_year_path = os.path.join(DATA_PATH, year_path)
zipfiles_names = os.listdir(data_year_path)

for zf in zipfiles_names:
    file_name = zip_file[zf]
    full_zip_path = os.path.join(data_year_path, zf)

    print(f"Extracting {zf}...")
    with ZipFile(full_zip_path, "r") as z:
        z.infolist()[0].filename = file_name
        z.extract(z.infolist()[0], data_year_path)
    print(f"{zf} Extracted.\n\n")
    os.remove(full_zip_path)