import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# font = ImageFont.truetype("Arial-Bold.ttf",14)
#font = ImageFont.truetype("Arial.ttf",34)


for i in range(19968,19980):
    font = ImageFont.truetype("chfont.ttf",50)
    img=Image.new("RGBA", (50,50),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0),chr(i),(0,0,0),font=font)
    draw = ImageDraw.Draw(img)
    img.save(chr(i)+"_test.png")
