from PIL import Image
import os.path
import glob

# python function
# Function: Convert a jpg file to pgm format file
# Parameter: jpg_file: jpg file name to be converted
# pgm_dir: directory to store pgm files
def jpg2pgm (jpg_file, pgm_dir):
    # First open the jpg file
    jpg = Image.open (jpg_file)
    # resize to 100 * 100, bilinear interpolation
    jpg = jpg.resize ((100,100), Image.BILINEAR)
    # Call the python functions os.path.join, os.path.splitext, os.path.basename to generate the target pgm file name
    name = (str) (os.path.join (pgm_dir, os.path.splitext (os.path.basename (jpg_file)) [0])) + ".pgm"
    # Create target pgm file
    jpg.save (name)

# Place all jpg files in the current working directory, or cd {the directory where the jpg files are stored}
for jpg_file in glob.glob ("test_model_images/selena/*.jpeg"):
    jpg2pgm (jpg_file, "test_model_images/selena/pgm/")
# path = 'test_model_images/anjelina'

# print(glob.glob(f"{path}/*"))


