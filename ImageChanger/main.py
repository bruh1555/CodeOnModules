from PIL import Image
import os

def raci(input_path, output_path, new_width, new_height, new_format):
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((new_width, new_height))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            resized_img.save(output_path, format=new_format.upper())
            print(f"Image saved!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Image Changer")
    print("v0.1.0")
    print("")
    ip = input("Enter path to input image: ")
    op = input("Enter path to save the output image (e.g. output/image.png): ")
    nw = int(input("Enter new width: "))
    nh = int(input("Enter new height: "))
    nf = input("Enter new image format (e.g., PNG, JPEG): ")
    raci(ip, op, nw, nh, nf)
