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
    dockersaveimage = input("Enter the TAR archive name to save the image")
    subprocess.call(['sudo','docker','save',dockersaveimage,'-o',''])

def main():
    print("Welcome to Command Selector!")
    print("1. Start Docker Container ")
    print("2. Remove Docker Container ")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("0. Exit")
    
    while True:
        key = input ("Enter Digits from (1-8) \n")

        if key == '1':
            dockerstart()
        
        elif key == '2':
            dockeremove()
if __name__ == "__main__":
    main()
