class Desct:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Closing the db connection")

a = Desct()
print("End the program")
del a

class FileHandler:
    def __init__(self,filename):
        self.file = open(filename,'w')
        print("File is opened")

    def readfile(self,filename):
        print("reading the file")

    def __del__(self):
        self.file.close()
        print("File closed")

f = FileHandler("test.txt")
f.readfile("test.txt")
del f