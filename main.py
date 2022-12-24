# This is a simple Qr Code creator and downloader

#Import required library
import qrcode


def generate(qr_url, image_name):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(qr_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(image_name.strip()+".jpg")


#Code Runner
if __name__ == '__main__':
    qr_url = input("Enter url that you want to embed in qr code : ")
    image_name = input("Enter image name that you want to save qr code : ")
    generate(qr_url, image_name);
