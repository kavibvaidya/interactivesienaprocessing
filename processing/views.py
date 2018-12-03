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

# NOTE: I do not think that this is required it will be destoyed later
class Processed(TemplateView):
    def get(self, request):
        print("processed was invoked")
        lst = []

        for index in os.listdir("processing/static/Data"):
            if not index.startswith("."):
                lst.append(index)
        return render(request, "processed.html", {"list": lst})
    def post(self, request):
        path = "Data/" + request.POST["folder"]
        print(path)
        return render(request, "volume-viewer-demo.html", {"path": path})

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
            fs.save("processing/static/Data/" + file1, request.FILES["File1"])
            fs.save("processing/static/Data/" + file2, request.FILES["File2"])
            process(file1, file2, str(output))

            # request.dirname = output
            # request.file1 = file1
            # request.file2 = file2
            return render(request,"updates.html",  {"output": output, "file1": file1 , "file2": file2})
            #return HttpResponseRedirect("updates")
        else:
            # NOTE:  We will read this in nthe javascript and send a finished
            # that will then compress and send over the file.
            print("ask for updates was recieved.")
            data = request.POST
            with open("processing/static/Data/" + data["output"] + "/output.txt") as f:
                state = f.read()
            return HttpResponse(state)
    def get(self, request):
        return render(request, "homepage.html")

class Download(TemplateView):
    def post(self, request):
        print("ask for download is recieved")
        print(request.POST["output"])
        zipper = "zip processing/static/Data/" + request.POST["output"]
        + " .zip processing/static/Data/" + request.POST["output"]
        print("The input to zip is ", zipper)
        # os.system(zipper)
        #Now we will delete thngs that we do not wantself.
        # delete1 = "rm Data/" + request.POST["file1"]
        # delete2 = "rm Data/" + request.POST["file2"]
        #Now we will be sending a confirmaiton
        return HttpResponse("We have processed the data")

# TODO:  WE have to make a url that will handle compression and sending the data over


def process(file1, file2, output):
    # print("Inside the function")
    # print(os.path.exists("Datafile1))
    # print(os.system("pwd"))
    os.system("mkdir processing/static/Data/" + output)
    out = os.popen("siena processing/static/Data/" + file1 +
    " processing/static/Data/" + file2 + " -o " + "processing/static/Data/" +
    output + "> processing/static/Data/" +
    output + "/output.txt")
    return out
