# -------------------------------------------------------
# Title: Images labeling
# Description: This simple program is used to rename(label) images in a directory under the same category with indexed numbers.
# Author: Omar Khaled Ahmed.
# Contact by: https://www.linkedin.com/in/omar-khaled-527b6a214/
# -------------------------------------------------------

# NOTE: the images to be labeled is direct in the directory. 
# NOTE: the images will be renamed and saved in the same directory.
# NOTE: the image extension will not be changed

# The function parameters:
#              [1] directory: the path of the directory that holds the images to be labeled.
#              [2] category: a string of the label to rename the images under the same category.


import os
def images_labeling(directory , category):
    images_list = os.listdir(directory) # return all images inside the passed directory.
    image_index = 1 # as start index 
    # Loop over all images
    for image in images_list:
        # get image extension
        image_extension = image.split('.')[-1]
        # rename each image under the same category with index
        image_label = f'{category}.{image_index}.{image_extension}'
        src_img_path    = f'{directory}/{image}'
        dest_img_path   = f'{directory}/{category}.{image_label}'
        os.rename(src_img_path , dest_img_path)
        image_index += 1