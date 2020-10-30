import concurrent.futures
import numpy as np

from image import read_image, crop_image, count_hit
from time_tracker import simple_time_tracker


@simple_time_tracker()
def count_image_pixels_over_threshold(im, threshold=250):
    """计算大于某个色差值的所有像素比
    """
    pixels = im.width * im.height
    matrix = np.asarray(im)
    hit = 0

    ml = len(matrix)
    part_list = [
        [0, ml // 4],
        [ml // 4, ml // 2],
        [ml // 2, ml - ml // 4],
        [ml - ml // 4, ml]
    ]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(
            count_hit, matrix[part[0]:part[1]], threshold) for part in part_list]

        for rc in concurrent.futures.as_completed(results):
            part_hits = rc.result()
            hit += part_hits

    ratio = hit / pixels
    return [hit, pixels, ratio]


if __name__ == '__main__':
    im = read_image("WechatIMG7.jpeg")
    hit, pixels, ratio = count_image_pixels_over_threshold(im)

    print(f"White pixels: hit = {hit}, pixels = {pixels}, ratio = {ratio}")
