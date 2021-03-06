import numpy as np
from image import read_image, crop_image, count_hit, count_hit_fast
from time_tracker import simple_time_tracker


@simple_time_tracker()
def count_image_pixels_over_threshold(im, threshold=250):
    """计算大于某个色差值的所有像素比
    """
    pixels = im.width * im.height
    w = im.width
    h = im.height
    hit = count_hit_fast(im, (w, h), threshold)
    ratio = hit / pixels
    return [hit, pixels, ratio]


if __name__ == '__main__':
    im = read_image("WechatIMG7.jpeg")
    hit, pixels, ratio = count_image_pixels_over_threshold(im)

    print(f"White pixels: hit = {hit}, pixels = {pixels}, ratio = {ratio}")
