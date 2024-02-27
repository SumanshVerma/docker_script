import os
import subprocess

def dockerstart():
    subprocess.call(['sudo','docker','ps','-a'])
    dockerimagename = input("Enter the image name from the following list to create")
    subprocess.call(['sudo','docker','run','-it',dockerimagename])

def dockeremove():
    subprocess.call(['sudo','docker','ps','-a'])
    dockerdeleteimage = input("Enter the image name from the following list to delete")
    subprocess.call(['sudo','docker','rm', '-f',dockerdeleteimage])

def main():
    while True:
        key = input ("Enter Digits from (1-8) :\n 1. Network Information \n 2. DiskUsage \n 3. Make a new Directory \n 4. Delete a Directory \n 5. RAM Usage \n 6. Add a new user \n 7. Delete a user \n E to exit \n ")

        if key == '1':
            dockerstart()
        
        elif key == '2':
            dockeremove()
if __name__ == "__main__":
    main()
