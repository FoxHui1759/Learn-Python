"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from image import Image
import numpy as np


def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    image.array = image.array * factor


def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    image.array = (image.array - mid) * factor + mid


def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    side_size = kernel_size // 2
    x, y, c = image.array.shape
    new_image = Image(x, y, c)
    for i in range(x):
        for j in range(y):
            sum = np.zeros(c)
            for i_c in range(max(0, i - side_size), min(i + 1 + side_size, x)):
                for j_c in range(max(0, j - side_size), min(j + 1 + side_size, y)):
                    sum += image.array[i_c, j_c]
            new_image.array[i, j] = sum / (kernel_size**2)
    image.array = new_image.array


def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    side_size = len(kernel[0]) // 2
    print(side_size)
    x, y, c = image.array.shape
    new_image = Image(x, y, c)
    for i in range(x):
        for j in range(y):
            sum = np.zeros(c)
            for i_c in range(max(0, i - side_size), min(i + 1 + side_size, x)):
                for j_c in range(max(0, j - side_size), min(j + 1 + side_size, y)):
                    i_v = i_c - i + side_size
                    j_v = j_c - j + side_size
                    kernel_value = kernel[i_v, j_v]
                    sum += image.array[i_c, j_c] * kernel_value
            new_image.array[i, j] = sum
    image.array = new_image.array


def combine_images(image1, image2):
    x, y, c = image1.array.shape
    new_image = Image(x, y, c)
    new_image.array = (image1.array**2 + image2.array**2) ** 0.5
    return new_image


if __name__ == "__main__":
    lake = Image(filename="lake.png")
    city = Image(filename="city.png")

    new_image = combine_images(
        Image(filename="new_city.png"), Image(filename="new_lake.png")
    )
    new_image.write_image("great_city.png")
