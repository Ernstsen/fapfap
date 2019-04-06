import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# TODO: 
# - find more data
# - tokenize

def pickupline_dot_net():
    url = "https://pickupline.net"

    with open("pickup_lines.txt", "w") as pickup_lines_files:
        response = requests.get(url)
        print(response)

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.findAll("tr")

        for row in rows:
            theme = row.findAll("td")
            if theme:
                theme_url = theme[0].find("a")["href"]
                try:
                    theme_response = requests.get(theme_url) 
                except:
                    print("error")
                    continue
                # scrabe the current theme
                soup = BeautifulSoup(theme_response.text, "html.parser")
                pickup_rows = soup.findAll("tr")

                for pickup_row in pickup_rows:
                    pickup_col = pickup_row.findAll("td")
                    if pickup_col:
                        pickup_line = pickup_col[0].renderContents().strip().decode("utf-8")
                        pickup_lines_files.write(pickup_line + "\n")
    
 
