import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd

def pickupline_dot_net():
    url = "https://pickupline.net"

    with open("pickup_line_files/pickup_lines.txt", "w") as pickup_lines_files:
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

def pickuplines_galore_dot_com():
    # remember to manueally remove the language categories and remove newlines
    url = "https://www.pickuplinesgalore.com"

    with open("pickup_line_files/pickup_lines_galore.txt", "w") as pickup_lines_files:
        response = requests.get(url)
        print(response)

        soup = BeautifulSoup(response.text, "html.parser")
        different_divs = soup.findAll("div", {"class": "coffee-span-4 coffee-558-span-6 coffee-419-pull-0 coffee-419-span-10 coffee-419-push-1 column-1"}) 
        for div in different_divs:
            extension = div.find("a")["href"]
            cat_url = url + "/" + extension

            cat_response = requests.get(cat_url)
            print(cat_url)            
            cat_soup = BeautifulSoup(cat_response.text, "html.parser")
            different_p = cat_soup.findAll("p", {"class": "action-paragraph paragraph"}) 
            
            for p in different_p:
                for sentence in p.text.split("\n"):
                    if "<<" in sentence or len(sentence.split()) > 30 or has_invalid_char(sentence):
                        #print("sentence:", sentence)
                        continue
                    pickup_lines_files.write(sentence.strip() + "\n")
                

def has_invalid_char(sentence):
    valid_chars = "abcdefghijklmnopqrstuvwxyz,.;$#€%&()-?""!1234567890 '"
    for c in sentence.lower():
        if c not in valid_chars:
            return True
    return False


def handle_csv_data_set(path_to_dataset):
    data = pd.read_csv(path_to_dataset)
    with open("dialog_line_files/ubuntu_dialog_lines.txt", "w") as write_file:
        for _, row in data.iterrows():
            write_file.write(str(row['text']))
        

def handle_movie_lines(path_to_dataset):
    with open("dialog_line_files/movie_dialog_lines.txt", "w") as write_file:
        with open(path_to_dataset, "r", errors="ignore") as movie_file:
            for line in movie_file:
                sentence = line.split("+++$+++")[-1]
                write_file.write(sentence)


# movie_dialog har spaces foran alle liner

if __name__ == "__main__":
    #handle_movie_lines("movie_lines.txt")
    #handle_csv_data_set("/Users/jesperbrink/Downloads/ubuntu-dialogue-corpus/Ubuntu-dialogue-corpus/dialogueText_301.csv")
    #pickuplines_galore_dot_com() 