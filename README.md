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
  anaconda will be of huge help.You can install all the dependancies using ```pip install -r requirements.txt```.

2. Use pip in your virtual environment to get django and pdb.

3. Go to the root folder in your terminal and type:
    ``` python manage.py runserver --insecure```
    Do not be araid of the insecure that just means that people will be able to see the absolute path in console.
4. Copy the link and open in the browser.

5. I have provided a new version of siena with all the interation in the terminal so that we know what is happening in server. You might      want to replace your sieana with this. Make sure that you change the name of this file to siena, or **alternatively**, you can copy the    same filename and keep both siena by changing views.py in processing to call modified siena in the os.system call.
