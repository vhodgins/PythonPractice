from PIL import Image
import requests
from io import BytesIO


     

img = Image.open('C:\\Users\\v3hod\\Desktop\\evil1.jpg')
(w,h) = img.size
pixels = []

even = Image.new('RGB', ((w // 2)+1 , (h //2)+1))
odd = Image.new('RGB', ((w // 2)+1 , (h //2)+1))

for y in range(0, int(h)):
    for x in range(0, int(w)):
        if x % 2 == 1:
            even.putpixel((int(x/2), int(y/2)), img.getpixel((x,y)))
        else:
            odd.putpixel((int(x/2), int(y/2)), img.getpixel((x, y)))




even.save('even.jpg')
odd.save('odd.jpg')
