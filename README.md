# Name-Switcher
This is a simple script to switch two folder names

Instructions: 

Insert the paths of the two folders in folders.json under folder1 and folder 2. Insert a temporary folder path that is not used by any other folder. 

Example JSON: 

{
  "temp": "C:\\Users\\Daniel\\OneDrive\\Desktop\\TemporaryFolder",
  "folder1": "C:\\Users\\Daniel\\OneDrive\\Desktop\\Sample1",
  "folder2": "C:\\Users\\Daniel\\OneDrive\\Desktop\\Sample2"
}

Run the script from the command line:
1.) Navigate inside the folder directory with dir [directory name] to list directories and cd [directory name] to enter directories
2.) Type python switch.py 
