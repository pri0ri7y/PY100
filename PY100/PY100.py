import urllib 
import json

class PY100:

     def __init__(self):
		self.URL = "https://www.udacity.com/public-api/v0/courses"
		self.postRequest()
    
     def postRequest(self):	     
	    data = urllib.urlopen(self.URL).read()
	    returnset = json.loads(data)
	    print returnset


if __name__ == '__main__':
    py100 =  PY100()
