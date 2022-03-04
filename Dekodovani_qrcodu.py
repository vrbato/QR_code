from pyzbar.pyzbar import decode
from PIL import Image # import knihovny

img = Image.open("C:/Users/vrbat/PycharmProjects/QR_code/my_qr1.jpg")

result = decode(img)

print(result[0][0]) # vrací to list - přes indexy se dostanu jen na tu hlavní informaci z listu


