# Administrador de archivos automatizado.
from distutils import extension
from pkgutil import extend_path
from PIL import Image
import os

downloadsFolder = "C:/Users/rodri/Downloads/"
picturesFolder = "C:/Users/rodri/OneDrive/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)



