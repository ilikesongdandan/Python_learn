from PIL import Image
import sys
im=Image.open('test.jpg')
print im.format,im.size,im.mode
# print sys.path
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')