import qrcode

code = qrcode.QRCode(version=1, box_size=36, border=6)

data = 'https://www.google.com'
code.add_data(data)

code.make()

image = code.make_image(fill_color = 'black', back_color='white')

image.save('./image.png')



