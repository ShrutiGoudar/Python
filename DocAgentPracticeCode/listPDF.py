import os
#TODO :
def printPdfDetails(pdf):
    return 
def listPDFinFolder(folderPath):
    ## from filehandling exercise I know that import os helps access a file. 
    try:
        files = os.listdir(folderPath)
        pdf = [x for x in files if x.lower().endswith(".pdf")]
        
        ### now i want to list the files
        # printPdfDetails(pdf) #TODO
        pdfCount = len(pdf)
        return pdfCount
    except FileNotFoundError:
        print(f"Folder '{folderPath}' not found!")
        return 0
    except PermissionError:
        print(f"Permission denied to access '{folderPath}'!")
        return 0



## counting the number of  pdf files in a given folder
'''
Steps: 
1. Access a folder and see if there is any premission issue if so report and return
2. look for all files in the folder
3. check if anything in the list ends with .pdf then increment counter. 
4. return the final list
'''

def main():
    folderPath = input("Enter complete folder path : \n")
    print(f"Number of PDF in given path is : {listPDFinFolder(folderPath)}")

if __name__ == "__main__":
    main()