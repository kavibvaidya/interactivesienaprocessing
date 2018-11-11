# interactivesienaprocessing

## Goals:
1. To allow researchers use the sieana software without the installation.
2. To make the output visible so that the researchers can know what is going wrong.

## Completed Tasks
1. We have made the functionality to send the file to our servers. 
2. We have made made the backend such that we can start the processing and write all the outputs in a text file.
3. The webpage now has the functionality to read the file and print that.

## Todo's

1. We have to read the file such that if the processing is complete, we will compress the file and send it  so that it can we downloaded. 
2. After the client has downloaded the zipped folder, we have to continue and delete the files and the folders. 

## How to use

1. First, it is recommanded to make a virtual environment to use the libraries required to run this program.
  anaconda will be of huge help.

2. Use pip in your virtual environment to get django and pdb.

3. Go to the root folder in your terminal and type:
    ``` python manage.py runserver ```
4. Copy the link and open in the browser.
