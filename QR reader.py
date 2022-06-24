from pyzbar.pyzbar import decode
from PIL import Image

file_name = input('Enter filename: ')

#open image and decode the qrcode
url = decode(Image.open(file_name))

#print the url
print('url: ', url[0].data.decode('ascii'))


