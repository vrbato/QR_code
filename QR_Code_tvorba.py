import qrcode #potřebuji importovat knihovnu qrcode (instalovat)

#co chci do qr kodu - cokoli, adresa
data = "Ahoj, jak se máš?"

img = qrcode.make(data) #tvoří to obrázek
img.save("my_qr_code.jpg") #nemusím zadávat cestu, uloží se to do adresáře, kde je hlavní modul

