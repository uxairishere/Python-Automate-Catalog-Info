from PIL import Image
import glob
from os import listdir, path


images = glob.glob('supplier-data/images/*.tiff')
i = 0
newsize = (600,400)
for image in images:
    file, ext = path.splitext(image)
    im = Image.open(image).convert("RGB").resize(newsize).save( file +'.jpeg')
    i+=1