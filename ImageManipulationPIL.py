from PIL import Image

def AfficherImg(NI):
    img = Image.open(NI)
    img.show()
    return img

def convertir_NB(img):
    img_gris = img.convert("L")
    img_gris.show()
    return img_gris

def caracter_img(img):
    pixels = img.load()
    width, height = img.size
    total_pixels = width * height
    black_pixels = 0
    white_pixels = 0

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if pixel == 0:
                black_pixels += 1
            elif pixel == 255:
                white_pixels += 1

    return total_pixels, black_pixels, white_pixels

def resize_and_rotate(img):
    img2 = img.resize((120, 120))
    img2.show()

    img3 = img2.rotate(45)
    img3.show()

    return img2, img3

def black_borders(img, border_size=10):
    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(border_size):
            pixels[x, y] = (0, 0, 0)
        for y in range(height - border_size, height):
            pixels[x, y] = (0, 0, 0)

    for y in range(border_size, height - border_size):
        for x in range(border_size):
            pixels[x, y] = (0, 0, 0)
        for x in range(width - border_size, width):
            pixels[x, y] = (0, 0, 0)

    img.show()
    return img



if __name__ == "__main__":
    img = AfficherImg("C:\\Users\\DELL\\Downloads\\artificial_intelligence.jpg")
    img_gris = convertir_NB(img)
    total_pixels, black_pixels, white_pixels = caracter_img(img_gris)
    print(f"Total pixels: {total_pixels}, Black pixels: {black_pixels}, White pixels: {white_pixels}")
    img2, img3 = resize_and_rotate(img)
    img_with_borders = black_borders(img)
