from steganography_tools import st
import cv2
import matplotlib.pyplot as plt

def encode():
    img = input("Enter image name(with extension) : ")
    steg = st.LSBSteganography(cv2.imread(img))
    txt = input("Enter data to be encoded : ")
    img_encoded = steg.encode_text(txt)
    cv2.imwrite("image_enc.png", img_encoded)
    plt.imshow(img_encoded)


def decode():
    
    im = cv2.imread("image_enc.png")
    steg = st.LSBSteganography(im)
    print("Text value:",steg.decode_text())


def compare():
    original = cv2.imread('sakura.jpeg')
    lsbEncoded = cv2.imread("image_enc.png")
    original_img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    lsb_encoded_img = cv2.cvtColor(lsbEncoded, cv2.COLOR_BGR2RGB)
    
    compare_images = st.Compare(original_img, lsb_encoded_img)
    compare_images.get_results()



    
if __name__ == "__main__" :

    a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n3. Compare\n"))
    if (a == 1):
         encode()
    elif (a == 2):
         print("Decoded Word : " , decode())
	
    elif (a==3):
         print("Comparison :", compare())
    else:
         raise Exception("Enter correct input")

