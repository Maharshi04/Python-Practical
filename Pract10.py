# ID : 20CE048
# Name : Maharshi Limbachiya

# AIM : Generate PDF file of your 3rd Semester Mark-sheet

# github repository link : https://github.com/Maharshi04/Python-Practical/blob/main/Pract10.py



from PIL import Image

# Path for your image where it is
image_1 = Image.open(
    r'C:\Users\RAKESH\Desktop\Maharshi\sem3 ms.png')

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(r'C:\Users\RAKESH\Desktop\Documents\VS CODE\Python\Python Practicals\Pract10.pdf')