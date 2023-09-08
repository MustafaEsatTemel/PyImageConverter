from PIL import Image

image = Image.open("download.jpeg").convert("RGB").save("new.png")
print("image converted.")

