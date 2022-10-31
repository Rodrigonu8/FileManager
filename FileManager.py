# Administrador de archivos automatizado.
from distutils import extension
from gettext import install
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
            picture.save(picturesFolder + "compressed_" +
                         filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".exe"]:
            installFolder = "C:/Users/rodri/Instaladores/"
            os.rename(downloadsFolder + filename, installFolder + filename)
            print(name + ": " + extension)

        if extension in [".docx"]:
            wordFolder = "C:/Users/rodri/OneDrive - Emtec Group/Documentos/Word/"
            os.rename(downloadsFolder + filename, wordFolder + filename)
            print(name + ": " + extension)

        if extension in [".xlsx"]:
            excelFolder = "C:/Users/rodri/OneDrive - Emtec Group/Documentos/Excel/"
            os.rename(downloadsFolder + filename, excelFolder + filename)
            print(name + ": " + extension)

        if extension in [".pptx"]:
            pptsFolder = "C:/Users/rodri/OneDrive - Emtec Group/Documentos/Ppt/"
            os.rename(downloadsFolder + filename, pptsFolder + filename)
            print(name + ": " + extension)
        
        if extension in [".pdf"]:
            pdfFolder = "C:/Users/rodri/OneDrive - Emtec Group/Documentos/Pdf/"
            os.rename(downloadsFolder + filename, pdfFolder + filename)
            print(name + ": " + extension)

        if extension in [".zip", ".rar"]:
            compFolder = "C:/Users/rodri/Comprimido/"
            os.rename(downloadsFolder + filename, compFolder + filename)
            print(name + ": " + extension)