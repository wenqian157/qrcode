import qrcode
import qrcode.constants

data = "https://concrete.ethz.ch/apps/ar/torsion/"

qr = qrcode.QRCode(
    version=2, # size
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, # size of each box
    border=4, #border size minimum 4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("qrcode2.png")