from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os


class MyGoogleDisk:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
        self.drive = GoogleDrive(self.gauth)

    def create_folder(self, name_folder):
        folder_metadata = {
        'title': name_folder,
        # Define the file type as folder
        'mimeType': 'application/vnd.google-apps.folder',
        # ID of the parent folder
        }

        folder_disk = self.drive.CreateFile(folder_metadata)
        folder_disk.Upload()

        return folder_disk['id']

    def upload_file(self, images, folder_local, folder_disk):
        id_folder = self.create_folder(folder_disk)
        for image in images:
            file5 = self.drive.CreateFile({'title': image, 'parents': [{'id': id_folder}]})
            #Read file and set it as a content of this instance.
            file5.SetContentFile(f'{folder_local}/{image}')
            file5.Upload() # Upload the file.


if __name__ == '__main__':
    google_disk = MyGoogleDisk()
    images = os.listdir('images')
    google_disk.upload_file(images, 'images', 'vk')
