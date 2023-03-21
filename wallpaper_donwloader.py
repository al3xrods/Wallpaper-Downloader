import os
import glob
import shutil
import time
import requests
import urllib.request as url


#Donwload Images From Unsplash API.
CLIENT = "Your Unsplash Client Name"

QUANTITY = int(input('How many wallpapers would you like to download? (Max 30 per session.)'))

THEME = str(input('What theme would you like to download? ')).lower() # Desire Theme to Donwload

r = requests.get(f'https://api.unsplash.com/photos/\
                 random?query={THEME}\
                 &count={QUANTITY}\
                 &orientation=landscape\
                 &fit=max\
                 &client_id={CLIENT}')

data = r.json() # Converting r into json format.
os.chdir("Working Directory") # New Working Directory.

for img_data in data :
    file_name = str(img_data['id']) + '.png' # Name of every image is the id + .png extension
    img_url = img_data['urls']['raw'] # Getting url of every image
    url.urlretrieve(img_url, file_name) # Download mage to new working directory

print('Donwload From Unsplash Completed.')
print('='*40)
print('\n')


# Script For Deleting Old Wallpapers.
old_wallpaper_dir = "Current Windows/Mac Wallpaper Folder" # Directory Old Wallpaper Images
filelist = glob.glob(os.path.join(old_wallpaper_dir, "*"))
try:
    for f in filelist:
        os.remove(f)
    print('Images from Wallpapers deleted.')
except:
    print('Could not be found images to delete.')

time.sleep(2)

print('='*40)
print('\n')

# Script for Transfering Donwloaded Wallpapers :
path = "Folder with Donwloaded Wallpapers"
moveto = "Folder to Move Donwloaded Wallpapers"
files = os.listdir(path)
try:
    for f in files:
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            scr = path+f
            dest = moveto+f
            shutil.move(scr, dest)
    print('New images moved to Wallpaper.')
except:
    print('Files not found.')
        

