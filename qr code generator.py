import qrcode #lib for qr generation


image = qrcode.make("link for generation of the qr")
image.save('image name.jpg')
