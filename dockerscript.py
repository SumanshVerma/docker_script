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

