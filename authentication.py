import requests
import json

def get_token(dnac): 
   # Complete the URL
   url = ...

   # The dnac object is passed as a parameter into the get_token function. Take the username and password and put them in a tuple
   credentials = ...

   # Add the appropriate headers
   headers = {
      ...
   }

   requests.packages.urllib3.disable_warnings()

   # Write the appropriate requests statement to perform the login into DNAC
   response = ...

   # From the response, parse the token. Hint: in case of doubt use a print statement to print out the response
   token = ...

   return token

if __name__ == "__main__":
   token = get_token()
