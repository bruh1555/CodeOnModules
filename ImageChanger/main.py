from PIL import Image
import os

def raci(input_path, output_path2, new_width, new_height, new_format2):
    try:
        with Image.open(input_path) as img:
            if new_format2.upper() == "JPG":
                output_path = output_path2 + '.jpg'
                new_format = "JPEG"
                resized_img = img.resize((new_width, new_height))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                resized_img.save(output_path, format=new_format.upper())
                print(f"Image saved!")
            else:
                output_path = output_path2 + f'.{new_format}'
                new_format = new_format2
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
    op = input("Enter path to save the output image (e.g. output/image) [Please note the extension will be automatically added. You don't need to include an extension.]: ")
    nw = int(input("Enter new width: "))
    nh = int(input("Enter new height: "))
    nf = input("Enter new image format (e.g., PNG, JPEG): ")
    raci(ip, op, nw, nh, nf)
