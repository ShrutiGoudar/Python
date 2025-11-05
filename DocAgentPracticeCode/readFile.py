#Read a .txt or .pdf file and print its text 

import os 
import PyPDF2       #py -m pip install PyPDF2py -m pip install PyPDF2 need to install: pip install PyPDF2
print("PyPDF2 installed successfully\!")
def readtxtFile(fileName):
    try :
        if os.path.exists(fileName):
            with open(fileName, "r") as file:
                content = file.read()
                print(content)
    except FileNotFoundError:
        print (f"Error in reading File : File not found {fileName}")
        return 0
    except PermissionError:
        print(f"Permission denied to access '{fileName}'")
        return 0
    
def readPDF(fileName): # reading pdf file needs PyPDF2 while i am currently facing problem to install 
    try:
        if os.path.exists(fileName):
            with open(fileName, "rb") as file:
                pdfreadobj = PyPDF2.PdfReader(file)
                numPages = len(pdfreadobj.pages)
                print(f"PDF has {numPages} pages")
                print("=" * 50)
                for page in range(numPages):
                    curPage = pdfreadobj.pages[page]
                    print(f"\n--- Page {page + 1} ---")
                    print(curPage.extract_text())
    except FileNotFoundError:
        print("FileNotFoundError")
        return 0
    except PermissionError:
        print(f"Permission denied to access the file {fileName}")
        return 0
    


def main():
    filepath = input("Enter full path of file to be read: ")
    
    # Check file extension to determine which function to use
    if filepath.lower().endswith('.pdf'):
        readPDF(filepath)
    elif filepath.lower().endswith(('.txt', '.py', '.md', '.log')):
        readtxtFile(filepath)
    else:
        print("Unsupported file type. Trying to read as text file...")
        readtxtFile(filepath)

if __name__ == "__main__":
    main()
