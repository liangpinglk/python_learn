#coding:utf-8
from PIL import Image
from numpy import * 
import pytesseract 
im = Image.open('ex.png') 
im = im.convert('RGB') 
#拉长图像，方便识别。
im = im.resize((200,80)) 
a = array(im) 
for i in xrange(len(a)): 
	for j in xrange(len(a[i])): 
		if a[i][j][0] == 255: 
			a[i][j]=[0,0,0] 
		else: 
			a[i][j]=[255,255,255] 
im = Image.fromarray(a) 
im.show() 
vcode = pytesseract.image_to_string(im) 
print vcode 
