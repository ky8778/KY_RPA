
from io import BytesIO
import win32clipboard
from PIL import Image

def send_to_clipboard(clip_type, data):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(clip_type, data)
	win32clipboard.CloseClipboard()

def copy_to_clipboard(path):
	# BASEPATH = 'images/'
	# print("What is your image file? : ")
	# IMGPATH = input()
	# filepath = BASEPATH + IMGPATH + '.jpg'
	img = Image.open(path)
	output = BytesIO()
	img.convert("RGB").save(output, "BMP")
	data = output.getvalue()[14:] # The file header off-set of BMP is 14bytes
	output.close()
	send_to_clipboard(win32clipboard.CF_DIB, data)
