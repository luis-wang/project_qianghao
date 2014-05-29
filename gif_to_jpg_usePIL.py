'''
Created on 2014-2-6

@author: Administrator
'''
import Image
import sys,os

def gif_2_jpeg_use_pil(infile, outfile):
    """
    "输入文件全路径，然后输出到指定的目录文件
    """
    
    try:
        im = Image.open(infile)
    except IOError:
        print "Cant load", infile
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save(outfile)

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence
    

def processImage(infile, file):
    try:
        im = Image.open(infile)
    except IOError:
        print "Cant load", infile
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save('E:/2kkkkk/cheliang_captcha/rgb/'+ file)

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence


dir = 'E:/2kkkkk/cheliang_captcha/'

for file in os.listdir(dir):
    if file.endswith('.jpg'):
        print 'filename:',dir + file
        processImage(dir + file, file)

print 'succ'

'''
im1 = Image.open("foo0.png")

print im1.format, im1.size, im1.mode

#image.save(outfile,"jpeg",quality=75)
sys.exit(0)

'''




