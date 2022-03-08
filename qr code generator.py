import qrcode


image = qrcode.make("https://www.google.com/maps/@10.3775489,78.804495,43m/data=!3m1!1e3")
image.save('location1.jpg')