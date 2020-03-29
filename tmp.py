from PIL import Image

im = Image.open("YouDidIt.png")

pix = im.load()

print(im.size)
source = im.split()
print(source)
# print("R=", r, "G=", g, "B=", b)