# Prerequisites 
* Python3 installed
* Git installed
* Visual Studio or other (Python) IDE

# Introduction

You will find two Python files. One to authenticate to a DNAC system (authentication.py) and one to retrieve the devices from DNAC (get_devicelist.py). In both Python files you will find comments and placeholders (the 3 dots). The goal is to replace the placeholders with appropriate Python code to ensure the application runs smoothly by running the  get_devicelist main function.

Below you find the various steps to complete this exercise.

### Step 1)	Clone repository
* Clone this repository onto your PC or MAC
* Once cloned, create a new git branch (give the branch a name (e.g. your username or full name)

### Step 2)	Modify the Python scripts

- Modify the Python scripts to accomplish the following:
  * Part 1: Log into DNAC and print the token
  * Part 2: Print an overview of all devices with their serial number
  As mentioned in the introduction, there are placeholders in the Python script to help you.

### Step 3) Push repository
* Once finished, add your code back to the Github repository. Push your code to the same Github repo under the branch you created in step 1

### Hints:

- API Documentation for DNAC can be found [here](https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-1-2-x-api-overview)
- You can use the following credentials to test your implementation
  * Host: sandboxdnac2.cisco.com
  * Username: devnetuser
  * Password: Cisco123!
