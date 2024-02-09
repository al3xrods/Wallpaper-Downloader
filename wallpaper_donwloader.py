import os
import glob
import shutil
import requests
import random
import config

# Constants
CLIENT = config.API_KEY
DOWNLOAD_DIR = r"C:\Users\al3xr\Downloads\Donwloaded Wallpapers"
MOVE_TO_DIR = r"C:\Users\al3xr\OneDrive\Pictures\Wallpapers"

THEMES = ["Fractal", 
          "Universe", 
          "Cosmic", 
          "Texture", 
          "Cosmos", 
          "Abstract",
          "Pattern"]

random_theme = random.choice(THEMES)


def download_images(theme, quantity):
    response = requests.get(f'https://api.unsplash.com/photos/random?query={theme}&count={quantity}&fit=max&client_id={CLIENT}')
    if response.status_code == 200:
        data = response.json()
        if not os.path.exists(DOWNLOAD_DIR):
            os.makedirs(DOWNLOAD_DIR)
        os.chdir(DOWNLOAD_DIR)

        images_downloaded = 0

        for img_data in data:
            file_name = f"{img_data['id']}.png"
            img_url = img_data['urls']['raw']
            with requests.get(img_url, stream=True) as r:
                with open(file_name, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    images_downloaded += 1
                    print(f"{images_downloaded}/{quantity} images downloaded.")
        print('Download from Unsplash completed.')
    else:
        print('Error in downloading images.')

def move_new_images():
    for f in os.listdir(DOWNLOAD_DIR):
        if f.endswith(('.jpg', '.jpeg', '.png')):
            shutil.move(os.path.join(DOWNLOAD_DIR, f), MOVE_TO_DIR)
    print('New images moved to wallpaper directory.')

def delete_old_wallpapers(directory):
    # Check if directory exists
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    # Deleting all files in the directory
    for f in glob.glob(os.path.join(directory, "*")):
        try:
            os.remove(f)
        except Exception as e:
            print(f'Error deleting file {f}: {e}')

    # Removing the directory
    try:
        os.rmdir(directory)
        print('Old wallpapers and directory deleted.')
    except Exception as e:
        print(f'Error deleting directory {directory}: {e}')

def main():
    quantity = input('How many wallpapers would you like to download? (Max 30 per session.) ')
    try:
        quantity = int(quantity)
        if quantity > 30:
            print("Quantity exceeds the maximum limit of 30.")
            return
    except ValueError:
        print("Invalid input for quantity.")
        return

    download_images(random_theme, quantity)
    move_new_images()
    delete_old_wallpapers()

if __name__ == "__main__":
    main()
