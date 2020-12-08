import os
from PIL import Image, ImageEnhance

save_path = input("Where am I saving images?")
num_imgs = input("How many images are needed?")
med_name = input("What is the medicine name?")

for i in xrange(0, num_imgs):
    orig_img_path = '/{}/{}{}.jpg'.format(save_path,med_name, i)
    print("Saving image to {}".format(orig_img_path))
    os.system('fswebcam  --no-banner --save {} -d /dev/video2 2> /dev/null -S 2 -s brightness=30% -s Contrast=15%  -s Gamma=25%  -p YUYV -r 299x299 --jpeg 80 -s Sharpness=40% -s Saturation=15%'.format(orig_img_path))
    input("Press Enter to continue...")
