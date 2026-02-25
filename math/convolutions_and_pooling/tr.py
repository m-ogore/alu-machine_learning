# import matplotlib.pyplot as plt
import numpy as np


def convolve_grayscale_valid(images, kernel):
    stride = 1
    (m, h, w) = images.shape
    # m is the number of images
    # h is the height in pixels of the images
    # w is the width in pixels of the images
    (kh, kw) = kernel.shape 
    # kh is the height of the kernel
    # kw is the width of the kernel
    convolved_image = []
    for image in images:
        for row in range(0,w-kw+1,stride):
            for col in range(0,h-kh+1,stride):
                image_region = image[row:row+kh, col:col+kh]
                convolution = np.sum(image_region@ kernel)
                convolved_image.append(convolution)

if __name__ == '__main__':

    #dataset = np.load('../../supervised_learning/data/MNIST.npz') 
    dataset = np.load('/home/seer/alu-machine_learning/supervised_learning/data/MNIST.npz')
    keys = dataset.keys()
    print("Keys in the archive:", keys)
    images = dataset['x_train']
    print(images.shape)
    kernel = np.array([[1 ,0, -1], [1, 0, -1], [1, 0, -1]])
    images_conv = convolve_grayscale_valid(images, kernel)
    print(images_conv.shape)

    # plt.imshow(images[0], cmap='gray')
    # plt.show()
    # plt.imshow(images_conv[0], cmap='gray')
    # plt.show()