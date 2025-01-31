#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Jason Blakely
# DATE CREATED: 11/6/2022                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates empty dictionary named results_dic and lists for word parsing
    results_dic = dict()
    pet_labels = []
    pet_labels_slpit = []

    # Print number of items in dictionary
    #print("\nEmpty Dictionary results_dic - n items=", len(items_in_dic))

    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)

    #split all words in each filename and save to list
    pet_labels_slpit = [filename_list[i].lower().split("_") for i in range(len(filename_list))]

    #combine and append only alphabetic words to label list
    for words in pet_labels_slpit:
        pet_label = ""
        for word in words:
            if word.isalpha():
               pet_label += word + " "
        pet_labels.append(pet_label.strip())
    
    #create dictionary keys=filenames, values=pet labels
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx] not in results_dic:
              results_dic[filename_list[idx]] = [pet_labels[idx]]
        else:
            print("** Warning: Key=", filename_list[idx], 
               "already exists in results_dic with value =", 
              results_dic[filename_list[idx]])

    # Print number of items in dictionary
    #print("\nPet Labels Dictionary results_dic items=", len(results_dic))
    return results_dic
