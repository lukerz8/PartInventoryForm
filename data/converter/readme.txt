#--------------------------------------------------#
# LEGO Inventory CSV to JSON Converter             #
# Version 1.0                                      #
#                                                  #
#                                                  #
# ************************************************ #
# Welcome!                                         #
# ************************************************ #
#                                                  #
# This program converts a LEGO inventory .csv file #
# to a .json file, in the format needed for        #
# 'PartsInventory.htm'.                            #
#                                                  #
# ************************************************ #
# Instructions:                                    #
# ************************************************ #
# 1. Download or create a .csv file of LEGO parts. #
#    This can be found at http://www.brickset.com, #
#    or created in Excel.                          #
# 2. Correctly format the .csv file                #
#    The .csv file needs to have the following 4   #
#    headers, in this order:                       #
#        PartID,Quantity,Category,PartName         #
#    You can sort the data by any one of these     #
#    categories, but I would suggest sorting it by #
#    Category. This can also be done in Excel.     #
# 3. Place the .csv file in the input directory    #
#    This dir is located at:                       #
#        LegoForm/data/converter/input/            #
#    A shortcut to here is in the LegoForm dir.    #
# 4. Run csvToJson script, and enter the file name #
#    The program will look in the input dir for    #
#    the file name you enter.                      #
# 5. Enter the kit name                            #
#    The program will then run, and create a .json #
#    file with this kit name in:                   #
#        LegoForm/data/converter/kits/             #
#    A shortcut to here is in the LegoForm dir.    #
# 5. Open PartsInventory.htm, and click the kit    #
#    name you would like an inventory form for.    #
# 6. Use the form at the top of the page to adjust #
#    the size of each element (experimental)       #
# 7. Press print!                                  #
#                                                  #
#--------------------------------------------------#