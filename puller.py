
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlparse
import urllib.request
import time

PAUSE_TIME = 1

data = open("page.html").read()

soup = BeautifulSoup(data,"html.parser")

count = 0
for d in soup.find_all("div"):
    jsdata = d.get("jsdata")
    if jsdata and "mp3" in jsdata:
        
        # find the url in the mess
        idx = jsdata.find("https")
        real_url = jsdata[idx:]
        resp = urlparse(real_url)

        # this the path and contains the filename
        # but still need to isolate the name
        real_path = resp.path

        # find last slash, search for the right
        slash_pos = resp.path.rfind("/")
        final_filename = resp.path[slash_pos+1:]

        print(real_url,final_filename," ... attempting to get file...")
        with urllib.request.urlopen(real_url) as u, open(final_filename,"wb") as outf:
            outf.write(u.read())
        print("finished with",final_filename)
        
        print("sleeping...")
        time.sleep(PAUSE_TIME)

        count+=1

print(f"total count is {count}")