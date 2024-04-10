from PIL import Image

def resize_image(image_name):
    basewidth = 100
    img = Image.open(image_name)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    img.save(image_name)

for i in range(0, 100):
    # mention the directory in which you want to resize the images followed by the image name
    resize_image("dataset/fist_test/fist_" + str(i) + '.png')
    resize_image("dataset/palm_test/palm_" + str(i) + '.png')
    resize_image("dataset/swing_test/swing_" + str(i) + '.png')

for i in range(0, 1000):
    resize_image("dataset/fist_train/fist_" + str(i) + '.png')
    resize_image("dataset/palm_train/palm_" + str(i) + '.png')
    resize_image("dataset/swing_train/swing_" + str(i) + '.png')

