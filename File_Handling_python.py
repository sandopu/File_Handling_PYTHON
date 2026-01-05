
# With Inheritance
import os

class Create_file:
    def __init__(self,file_location,file_name,file_type):
        self.file_location=file_location
        self.file_name=file_name
        self.file_type=file_type
    def create(self):
        k = self.file_location + "\\" + self.file_name + self.file_type
        try :
            with open(k,'x') as x:
                p=int(input("Press 1 for writeing content (or) Press Enter for Exit"))
                x.close()
                if p==1:
                    with open(k,'w') as w:
                        w.write(input("Enter a file content:-"))
                    w.close()
                    print(f"Successfully {self.file_name} Name file Create With type {self.file_type}" )
                    w.close()
                else:
                    print(f"Successfully {self.file_name} Name file Create With type {self.file_type}" )
        except FileExistsError:
            print("File already Exists")
            print("If You want to overwrite the file content Press 1:-\n If you want to Create Duplicate file press 2:-\n If you want to Exit Press Enter")
            p=int(input("Enter a Number"))
            if p==1:
                content=input("Enter a file content:-")
                with open(k,'w') as w:
                    w.write(content)
                print(f"Successfully replaced {self.file_name}{self.file_type}")
            elif p==2:
                i=0
                while True:
                    k = self.file_location +"\\"+ self.file_name + "(" + str(i) + ")" + self.file_type
                    print(k)
                    try:
                        p=0
                        with open(k,'x') as x:
                            pass
                        p=int(input("press 1 for write file content or Press Enter for Exit"))
                        if p==1:
                            with open(k,'w') as w:
                                w.write(input("Enter a file content Text"))
                            print(f"Successfully {self.file_name}({i}) Name file Create With type {self.file_type}" )
                        else:
                            print(f"Successfully {self.file_name}({i}) Name file Create With type {self.file_type}" )
                        break
                    except FileExistsError:
                        i+=1       
class Read():
    def __init__(self,file_location,file_name,file_type):
        self.file_location=file_location
        self.file_name=file_name
        self.file_type=file_type
    def read_file(self):
        k = self.file_location + "\\" + self.file_name + self.file_type
        try:
            with open(k,"r") as r:
                print(r.read())
        except FileNotFoundError:
            n=int(input("Press 1 for create new file:-\n press enter for exsit"))
            if n==1:
                a=Create_file(self.file_location,self.file_name,self.file_type)
                a.create()
            else:
                print("File Already Exsits")
            
class FileManager(Create_file, Read):
    pass

    
print("Enter 1 to Create File")
print("Press 2 for Read the File")
while True:
    n=int(input("Enter a number"))
    if n == 1:
        file_location=input("Enter a File Location") # smaple input (C:\Users\Rakesh\Desktop\Innomatics) Folder location
        file_name=input("Enter a File name")         # Sample input (file_handling)
        file_type="."+input("Enter a Type")          # sample input #py , html , etc... 
        f=FileManager(file_location,file_name,file_type)
        f.create()
        break
    elif n == 2:
        file_location=input("Enter a File Location") # smaple input (C:\Users\Rakesh\Desktop\Innomatics) Folder location
        file_name=input("Enter a File name")         # Sample input (file_handling)
        file_type="."+input("Enter a Type")          # sample input #py , html , etc... 
        f=FileManager(file_location,file_name,file_type)
        f.read_file()
        break
    else:
        print("Enter again only press 1 or 2")
        pass
