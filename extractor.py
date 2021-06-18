'''
author: Evan Putnam
description: A cmd-line tool that takes a sprite sheet and breaks it down into its individual images.
'''
from PIL import Image
import glob
import sys
import os

DEFAULT_FOLDER = "extract/"

def extract_images(path, x_dim, y_dim):
    im = Image.open(path)
    width, height = im.size
    if width % x_dim != 0 and height % y_dim != 0:
        print("Error: dimensions of " + str((width, height)) + " can not be broken in tiles of sizes " + str((x_dim, y_dim)))
        exit(-1)
    delete_old_files()
    total_x_tiles = int(width / x_dim)
    total_y_tiles = int(height / y_dim)
    for y in range(0, total_y_tiles):
        for x in range(0, total_x_tiles):
            name = DEFAULT_FOLDER + str(x) + "_" + str(y) + ".png"
            dimensions = ((x * x_dim), (y * y_dim), (x * x_dim) + x_dim, (y * y_dim) + y_dim)
            cropped_image = im.crop(dimensions)
            cropped_image.save(name)
            cropped_image.close()
    im.close()

def delete_old_files():
    files = glob.glob(DEFAULT_FOLDER + '*')
    for f in files:
        os.remove(f)

def handle_pathing(image_path):
    r_image_path = image_path
    if os.path.exists(image_path):
        r_image_path = os.path.abspath(r_image_path)
    else:
        print("Error: Image path does not exist.")
        exit(-1)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    return r_image_path

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        exit(-1)
    image_path = handle_pathing(sys.argv[1])
    x_dim = int(sys.argv[2])
    y_dim = int(sys.argv[3])
    extract_images(image_path, x_dim, y_dim)