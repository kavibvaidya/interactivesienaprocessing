from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

import os
import datetime
import subprocess
import pdb
import random

# Create your views here.

class Updates(TemplateView):
    def get(self, request):
        return render(request, "updates.html")

class HomePage(TemplateView):
    def post(self, request):
        global id
        if not request.is_ajax():
            print("the request was recieved")
            #print(request.FILES["File1"])
            fs = FileSystemStorage()
            file1 = request.FILES["File1"].name
            file2 = request.FILES["File2"].name
            output = file1 + "to" + file2
            # file1 = "file1.nii"
            # file2 = "file2.nii"
            fs.save("Data/" + file1, request.FILES["File1"])
            fs.save("Data/" + file2, request.FILES["File2"])
            process(file1, file2, str(output))

            # request.dirname = output
            # request.file1 = file1
            # request.file2 = file2
            return render(request,"updates.html",  {"output": output, "file1": file1 , "file2": file2, "state": "Kavi"})
            #return HttpResponseRedirect("updates")
        else:
            # NOTE:  We will read this in nthe javascript and send a finished
            # that will then compress and send over the file.
            data = request.POST
            with open("Data/" + data["output"] + "/output.txt") as f:
                state = f.read()
            return HttpResponse(state)
    def get(self, request):
        return render(request, "homepage.html")

# TODO:  WE have to make a url that will handle compression and sending the data over


def process(file1, file2, output):
    # print("Inside the function")
    # print(os.path.exists("Datafile1))
    # print(os.system("pwd"))
    os.system("mkdir Data/" + output)
    out = os.popen("siena Data/" + file1 + " Data/" + file2 + " -o " + "Data/" + output + "> Data/" +
    output + "/output.txt")
    return out
