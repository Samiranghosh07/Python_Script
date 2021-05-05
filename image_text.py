#Extract Text from Image

from pytesseract import pytesseract
from PIL import Image
tesseract_locate = pytesseract.normpath("E:/Program Files/Tesseract-OCR/tesseract.exe")
locate_image = Image.open("E:/Program Files/MY_STUDY/Python/My_Projects/Pygame/gameProject/pic.png")
pytesseract.tesseract_cmd = tesseract_locate
file = pytesseract.image_to_string(locate_image)
print(file[:-1])

locate_image2 = Image.open("E:/Program Files/MY_STUDY/Python/My_Projects/Pygame/gameProject/pic2.png")
pytesseract.tesseract_cmd = tesseract_locate
file2 = pytesseract.image_to_string(locate_image2)
print(file2[:-1])
