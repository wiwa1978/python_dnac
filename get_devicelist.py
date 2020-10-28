import requests
import sys
# Add import statement to be able to access the get_token function from the authentication file.
...


def get_device_list(dnac):
   token = get_token(dnac)

   # Complete the base_url and device_url statements
   base_url = ...
   devices_url = ...

   # Create the appropriate headers to retrieve the device list 
   headers = {
      ...
   }

   # Write the appropriate requests statement to get the device list from DNAC 
   response =  ...

   devices = response["response"]

   # Loop over all devices and print the device type and serial number
   for device in devices:
      ...

if __name__ == "__main__":  
   if len(sys.argv) == 4:
      dnac = {
         "host": sys.argv[1],
         "username": sys.argv[2],
         "password": sys.argv[3]
      }
      get_device_list(dnac)      
   else:
      print(f"Usage: python3 get_devices.py <host> <username> <password>")
      