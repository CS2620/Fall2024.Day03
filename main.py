from PIL import Image

image = Image.open("car.jpg")

data = image.load()
print(image.width)
print(image.height)

pixel = data[0,0]
print(pixel)
# red = pixel[0]
# green = pixel[1]
# blue = pixel[2]

red, green, blue = pixel
print(red)

packed_int = 0

packed_int += red << 16
packed_int += green << 8
packed_int += blue << 0

print(packed_int)

new_blue = packed_int & 255
packed_int >>= 8
new_green = packed_int & 255
packed_int >>= 8
new_red = packed_int & 255
print(new_red)
print(new_green)
print(new_blue)

def flip_horizontal(original_image):
    blank_image = Image.new("RGB", (original_image.width, original_image.height))
    blank_image_data = blank_image.load()
    original_data = original_image.load()

    for y in range(original_image.height):
        for x in range(original_image.width):
            pixel = original_data[x,y]
            blank_image_data[(original_image.width-1) - x,y] = pixel
    
    return blank_image

def flip_vertical(original_image):
    blank_image = Image.new("RGB", (original_image.width, original_image.height))
    blank_image_data = blank_image.load()
    original_data = original_image.load()

    for y in range(original_image.height):
        for x in range(original_image.width):
            pixel = original_data[x,y]
            blank_image_data[x,original_image.height-1-y] = pixel
    
    return blank_image

flipped_image_horizontal = flip_horizontal(image)
flipped_image_horizontal.save("flipped_horizontal.png")

flipped_image_vertical = flip_vertical(image)
flipped_image_vertical.save("flipped_vertical.png")
