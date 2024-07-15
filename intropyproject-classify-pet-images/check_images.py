#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time(10)
    sleep(20)## Sets start time
## Sets end time
end_time = time(40)

## Computes overall runtime in seconds
tot_time = end_time - start_time

## Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")
print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" +
          str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
          str( int(  ( (tot_time % 3600) % 60 ) ) ) ) 
    
    # TODO 1: Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    in_arg = get_input_args()
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type = str, default = 'pet_images/', 
                    help = 'path to the folder of pet images') 
    in_args = parser.parse_args()
    print("Argument 1:", in_args.dir)

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)

    
    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
    # Once the get_pet_labels function has been defined replace 'None' 
    # in the function call with in_arg.dir  Once you have done the replacements
    # your function call should look like this: 
    #             get_pet_labels(in_arg.dir)
    # This function creates the results dictionary that contains the results, 
    # this dictionary is returned from the function call as the variable results
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)
    from os import listdir  

## Retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")

## Print 10 of the filenames from folder pet_images/
print("\nPrints 10 filenames from folder pet_images/")
for idx in range(0, 10, 1):
    print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
results_dic = dict()

## Determines number of items in dictionary
items_in_dic = len(results_dic)
print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

## Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
## a List that contains only one item - the pet image label
filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
pet_labels = ["beagle", "boston terrier"]
for idx in range(0, len(filenames), 1):
    if filenames[idx] not in results_dic:
         results_dic[filenames[idx]] = [pet_labels[idx]]
    else:
         print("** Warning: Key=", filenames[idx], 
               "already exists in results_dic with value =", 
               results_dic[filenames[idx]])

#Iterating through a dictionary printing all keys & their associated values
print("\nPrinting all key-value pairs in dictionary results_dic:")
for key in results_dic:
    print("Filename=", key, "   Pet Label=", results_dic[key][0])
pet_image = "Boston_terrier_02259.jpg"

## Sets string to lower case letters
low_pet_image = pet_image.lower()

## Splits lower case string by _ to break into words 
word_list_pet_image = low_pet_image.split("_")

## Create pet_name starting as empty string
pet_name = ""

## Loops to check if word in pet name is only
## alphabetic characters - if true append word
## to pet_name separated by trailing space 
for word in word_list_pet_image:
    if word.isalpha():
        pet_name += word + " "

## Strip off starting/trailing whitespace characters 
pet_name = pet_name.strip()

## Prints resulting pet_name
print("\nFilename=", pet_image, "   Label=", pet_name)


    # TODO 3: Define classify_images function within the file classify_images.py
    # Once the classify_images function has been defined replace first 'None' 
    # in the function call with in_arg.dir and replace the last 'None' in the
    # function call with in_arg.arch  Once you have done the replacements your
    # function call should look like this: 
    #             classify_images(in_arg.dir, results, in_arg.arch)
    # Creates Classifier Labels with classifier function, Compares Labels, 
    # and adds these results to the results dictionary - results
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results    
    check_classifying_images(results) 
    filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]

## Defining empty dictionary
results_dic = dict()
    
## Populates empty dictionary with both labels &indicates if they match (idx 2)
for idx in range (0, len(filenames), 1):
    # If first time key is assigned initialize the list with pet & 
    # classifier labels
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]
 
    # Determine if pet_labels matches classifier_labels using in operator
    # - so if pet label is 'in' classifier label it's a match
    # ALSO since Key already exists because labels were added, append 
    # value to end of list for idx 2 
    # if pet image label was FOUND then there is a match 
    if pet_labels[idx] in classifier_labels[idx]:
        results_dic[filenames[idx]].append(1)
            
    # if pet image label was NOT found then there is no match
    else:
        results_dic[filenames[idx]].append(0)

## Populates dictionary with whether or not labels indicate a dog image (idx 3&4)
for idx in range (0, len(filenames), 1):
    # Key already exists, extend values to end of list for idx 3 & 4
    results_dic[filenames[idx]].extend([pet_label_is_dog[idx], 
                                       classifier_label_is_dog[idx]])
        
## Iterates through the list to print the results for each filename
for key in results_dic:
    print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])                        

    # Provides classifications of the results
    if sum(results_dic[key][2:]) == 3:
        print("*Breed Match*")
    if sum(results_dic[key][3:]) == 2:
        print("*Is-a-Dog Match*")
    if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
        print("*NOT-a-Dog Match*")


    
    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    # Once the adjust_results4_isadog function has been defined replace 'None' 
    # in the function call with in_arg.dogfile  Once you have done the 
    # replacements your function call should look like this: 
    #          adjust_results4_isadog(results, in_arg.dogfile)
    # Adjusts the results dictionary to determine if classifier correctly 
    # classified images as 'a dog' or 'not a dog'. This demonstrates if 
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, in_arg.arch)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)


    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats    
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)


    # TODO 6: Define print_results function within the file print_results.py
    # Once the print_results function has been defined replace 'None' 
    # in the function call with in_arg.arch  Once you have done the 
    # replacements your function call should look like this: 
    #      print_results(results, results_stats, in_arg.arch, True, True)
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt
     > resnet_pet-images.txt
    python check_images.py --dir pet_images/ --arch alexnet  --dogfile dognames.txt  
     > alexnet_pet-images.txt
    python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt 
     > vgg_pet-images.txt
    print_results(results, results_stats, in_arg.dogfiles, True, True)
    
    # TODO 0: Measure total program runtime by collecting end time
    end_time = time()
    
    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
