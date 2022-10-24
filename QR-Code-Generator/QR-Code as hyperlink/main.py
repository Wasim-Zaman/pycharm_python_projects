# import qrcode
#
# code = qrcode.QRCode(version=1, box_size=36, border=6)
#
# data = 'https://www.google.com'
# code.add_data(data)
#
# code.make()
#
# image = code.make_image(fill_color = 'black', back_color='white')
#
# image.save('./image.png')

# Import module
import wifi_qrcode_generator as qr

# Use wifi_qrcode() to create a QR image
code = qr.wifi_qrcode('Muhammad 1', False, 'WPA', 'malakand')
code.save("./wifiimage.png")