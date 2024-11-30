import os
print(os.getcwd())                  # Returns the present working directory
print(os.getcwdb())                 # Returs the present working directory as a byte object


os.chdir('D:\\CODEC TECHNOLOGY INTERNSHIP\\FileTest')            # use to change directory
print(os.listdir())                                              # All files and sub directories inside a directory
                                                                 # can be known using the listdir() method
print(os.getcwd())                                               # Returns the present working directory


# used to make a new directory
os.mkdir('Test')

# used to rename a directory
os.rename('Test', 'New_One')  
