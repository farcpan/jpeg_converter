from PIL import Image
import glob
import os


def main():
    print("=" * 30)
    print ("JPEG Converter: png files to jpg")
    print("=" * 30)
    print("input directory path: ")
    input_path = input()
    full_path = input_path.strip("\"").strip("'").strip()   # remove the first/last ' and "
    if full_path == 'q':
        print("finish.")
        return 1
    
    target_pattern = os.path.join(full_path, "*.png")
    png_file_path_list = glob.glob(target_pattern)
    for image_path in png_file_path_list:
        im = Image.open(image_path)
        img = im.convert("RGB")
        
        # a/b/c.png -> a
        dirname = os.path.dirname(image_path)
        parent_dirname = os.path.dirname(dirname)

        # a/b/c.png -> c.png
        basename = os.path.basename(image_path)

        # c.png -> c.jpeg
        jpeg_filename = basename.replace(".png", ".jpeg")

        # c.jpeg -> a/c.jpeg
        file_path = os.path.join(parent_dirname, jpeg_filename)

        print(file_path)
        im.save(file_path)

    return 0


if __name__ == '__main__':
    ret = 0
    while ret != 1:
        ret = main()
