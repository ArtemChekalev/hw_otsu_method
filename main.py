from matplotlib import image as mpimg
from config import images_path


def image_to_gray_scale(rgb_image: list[list[list[int]]]) -> list[list[int]]:
    """Function to convert an image into gray scale"""
    height, width = len(rgb_image), len(rgb_image[0])
    grayscale = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            # Count gray scale with formula from lecture
            r, g, b = rgb_image[i][j]
            grayscale[i][j] = int(0.299 * r + 0.587 * g + 0.114 * b)
    return grayscale


def count_histogram(grayscale_image: list[list[int]]) -> list[int]:
    """Counts histogram for image in grayscale"""
    histogram = [0] * 256
    for row in grayscale_image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram


def otsu_threshold(histogram, total_pixels):
    """Find otsu treshold"""
    total_brightness = sum(i * histogram[i] for i in range(256))
    sum_background, background_pixels_probability, max_variance, threshold = 0, 0, 0, 0

    for t in range(256):
        # w_0(T) + w_1(T) = total_pixels
        background_pixels_probability += histogram[t]  # w_0(T)
        if background_pixels_probability == 0:  # except division by zero
            break
        object_pixels_probability = total_pixels - background_pixels_probability  # w_1(T)
        if object_pixels_probability == 0:  # except division by zero
            break
        sum_background += t * histogram[t]  # i * p(i)

        # mu_0(T) + mu_1(T) = total_brightness
        mean_background_brightness = sum_background / background_pixels_probability  # mu_0(T)
        mean_object_brightness = (total_brightness - sum_background) / object_pixels_probability  # mu_1(T)

        # w_0(T) * w_1(T) * (mu_0(T) - mu_1(T))^2
        variance_between = background_pixels_probability * object_pixels_probability * (mean_background_brightness -
                                                                                        mean_object_brightness) ** 2

        # threshold = argmax(variance)
        if variance_between > max_variance:
            max_variance = variance_between
            threshold = t

    return threshold


def binarize_image(grayscale, threshold):
    """Binarize an image with threshold."""
    height, width = len(grayscale), len(grayscale[0])
    binary = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            binary[i][j] = 1 if grayscale[i][j] >= threshold else 0
    return binary


def otsu_main(image):
    """Main function"""
    grayscale = image_to_gray_scale(image)
    histogram = count_histogram(grayscale)
    total_pixels = len(image) * len(image[0])  # sum(p[i]) == total_pixels
    threshold = otsu_threshold(histogram, total_pixels)
    binary_image = binarize_image(grayscale, threshold)
    return binary_image


if __name__ == '__main__':
    image_path = images_path + 'noise_img.jpg'
    img = mpimg.imread(image_path)
    res = otsu_main(img)
    print(res)
    