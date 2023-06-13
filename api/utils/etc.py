import zipfile

from django.core.files.uploadedfile import InMemoryUploadedFile
from pdf2image import convert_from_bytes
import io


class CustomResponse(object):
    def __init__(self):
        self.success = True
        self.message = ""
        self.response = []

    def default_out(self):
        return {
            "success": self.success,
            "message": self.message,
            "response": self.response,
        }


def has_special_char(s):
    return any(item in ["!", "\"", "\'", "#", "@", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "\\", "|", "~", "`", "[", "]", "{", "}", "<", ",", ">", ".", "/", "?"] for item in s)


def pdf_to_image_zip(file):
    # change pdf to image
    try:
        images = convert_from_bytes(file.read())
    except Exception as e:
        raise Exception("PDF_TO_IMAGE_ERROR")

    # change image to bytes
    for i in range(len(images)):
        file_object = io.BytesIO()
        images[i].save(file_object, "png")
        images[i].close()
        images[i] = file_object

    # zip images
    images_zip = io.BytesIO()
    with zipfile.ZipFile(images_zip, 'w') as zip_folder:
        for image in images:
            try:
                zip_folder.writestr(str(images.index(image)) + ".png", image.getvalue())
            except Exception as e:
                raise Exception("ZIP_ERROR")

    # change bytes to file
    images_zip = InMemoryUploadedFile(images_zip, None, "images.zip", "application/zip", images_zip.getbuffer().nbytes, None)

    return images_zip
