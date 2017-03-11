import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as img

from skimage.data import astronaut
from scipy.misc import imresize

def main():
    img = imresize(astronaut(), (64, 64))
    plt.imshow(img)

if __name__ == "__main__":
    main()
