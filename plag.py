import sys
import difflib

def check(refFile, sourceFile):
        with open(refFile) as file1:
                with open(sourceFile) as file2:
                        file1_data = file1.read()
                        print (file1_data)

                        file2_data = file2.read()
                        print (file2_data)

                        s= difflib.SequenceMatcher(None,file1_data,file2_data)
                        s1 = s.ratio()*100
                        msg =str(s1)     #plaglarosm detectedzz

                        return msg

#if  __name__=="__main__":
    #refFfile = "ref.txt"
    #sourceFile = "src.txt"
    #check(refFfile, sourceFile)

