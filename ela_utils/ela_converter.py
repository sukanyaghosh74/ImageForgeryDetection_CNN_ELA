from PIL import Image, ImageChops, ImageEnhance

def convert_to_ela_image(path, quality=90):
    original = Image.open(path).convert('RGB')
    original.save('temp.jpg', 'JPEG', quality=quality)
    compressed = Image.open('temp.jpg')
    ela_image = ImageChops.difference(original, compressed)
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale = 255.0 / max_diff if max_diff != 0 else 1
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    return ela_image
