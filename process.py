import os
import argparse


def process(file1, file2, output):
    # print("Inside the function")
    # print(os.path.exists("Datafile1))
    # print(os.system("pwd"))
    output = os.system("siena Data/" + file1 + " Data/" + file2 + " -o " + "Data/" + output)
    return output

parser = argparse.ArgumentParser(description="Processing")
parser.add_argument("file1", metavar="f1", type=str, help="This is file1")
parser.add_argument("file2", metavar="f2", type=str, help="This is file2")
parser.add_argument("output", metavar="o", type=str, help="This is the output")

process(parser.parse_args().file1, parser.parse_args().file2, parser.parse_args().output)
