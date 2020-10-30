import os

from PIL import Image

def read_image(img_name):
    """从当前目录读取图片
    """
    image_path = os.path.join(os.path.dirname(__file__), img_name)
    im = Image.open(image_path)
    return im


def crop_image(im, view_rect, output_path):
    cropped_im = im.crop(view_rect)
    cropped_im.save(output_path)
    return cropped_im


def count_hit(matrix, threshold):
    hit = 0
    for row in matrix:
        for pixel in row:
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]

            if r >= threshold and g >= threshold and b >= threshold:
                hit = hit + 1

    return hit
