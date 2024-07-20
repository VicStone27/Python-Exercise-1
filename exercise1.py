
# next section is meant to prompt user to input filename before script begins
import sys
if len(sys.argv) !=2:
    print("Notice: python exercise1.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
# print(filename)

try:
    with open(filename,"r") as file:
        content =  file.read()
        print("Contents of File:")
        print(content)
except FileNotFoundError:
    print(f"Filename: {filename} Not Found")
    sys.exit(1)