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

def dockersave():
    subprocess.call(['sudo','docker','ps','-a'])
    dockersaveimage = input("Enter the image to be saved")
    dockertarimage = input("Enter the TAR archive name to save the image")
    subprocess.call(['sudo','docker','save',dockersaveimage,'-o',dockertarimage])
    
def dockerload(dockertarimage):
    subprocess.call(['docker','load','-i',dockertarimage])

def runningcontainer():
    subprocess.call(['sudo','docker','ps'])

def stoppedcontainer():
    subprocess.call(['sudo','docker', 'ps', '-f', 'status=exited'])

def showimages():
    subprocess.call(['sudo','docker','images','ls'])

def main():
    print("Welcome to Command Selector!")
    print("1. Start Docker Container ")
    print("2. Remove Docker Container ")
    print("3. Save an Image")
    print("4. Load the saved image")
    print("5. Show running containers")
    print("6. Show stopped containers")
    print("7. Show all images ")
    print("0. Exit")
    
    while True:
        key = input ("Enter Digits from (1-8) \n")

        if key == '1':
            dockerstart()

        elif key == '2':
            dockeremove()
        elif key == '3':
            dockersave()
        elif key == '4':
            dockerload()
        elif key == '5':
            runningcontainer()
        elif key == '6':
            stoppedcontainer()
        elif key == '7':
            showimages()
        elif key == 'e': 
            print("Exiting program.")
            break
        else:
            print("Invalid key. Please press a number key from 1-7.")                     

if __name__ == "__main__":
    main()
