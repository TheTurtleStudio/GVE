import os, sys
libs = None
functions = []
def tryCatch(code,):
    try:
        exec(code)
    except Exception as error:
        return f"{type(error).__name__}: {error}\n"
with open(os.path.join(os.getcwd(), 'libraries.txt'), "r") as importLibs:
    libs = importLibs.read().split()
try:
    for i in libs:
        try:
            exec(f"import {i}")
        except Exception as error:
            sys.stderr.write(f"{type(error).__name__}: {error}\n")
            libs.remove(i)
except Exception as error:
    sys.stderr.write(f"{type(error).__name__}: {error}\n")
def print(_input=""):
    sys.stdout.write(f"<<: {_input}\n")
print = print
sys.stdout.write(f"Python {sys.version} I/O BVE\n")
try:
    sys.stdout.write(f"----Predefined libraries: {', '.join(libs)}----\n")
except Exception as error:
    sys.stderr.write(f"{type(error).__name__}: {error}\n")
try:
    sys.stdout.write(f"----Predefined Gevvy functions: {len(os.listdir(os.path.join(os.getcwd(), 'functions')))}----\n\n")
except Exception as error:
    sys.stderr.write(f"{type(error).__name__}: {error}\n")
sys.stdout.write(f"Add or remove predefined libraries in \"{os.path.join(os.getcwd(), 'libraries.txt')}\"\n")
sys.stdout.write(f"Add or remove predefined functions in \"{os.path.join(os.getcwd(), 'functions.txt')}\"\n")
sys.stdout.write(f"To get a list of all predefined libraries, use the function \"_COMM.getLibraries()\"\n")
sys.stdout.write(f"To get a list of all predefined functions, use the function \"_COMM.getFunctions()\"\n\n")
sys.stdout.write(f"----------Gevvy Virtual Environment----------\n\n")
for possibleFunc in os.listdir(os.path.join(os.getcwd(), 'functions')):
    try:
        with open(os.path.join(os.getcwd(), f'functions\\{possibleFunc}'), "r") as file:
            exec(file.read())
            functions.append(file.name.split("\\")[-1])
    except Exception as error:
        sys.stderr.write(f"{type(error).__name__}: {error}\n")
        functions.remove(i)
importLibs = None
while True:
    try:
        inp = input(">>: ")
        exec(inp)
    except Exception as error:
        sys.stderr.write(f"<<: {error}\n")
        

