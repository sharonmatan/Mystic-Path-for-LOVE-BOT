# YOUR BOT LOGIC/STORAGE/BACKEND FUNCTIONS HERE
import requests
from bs4 import BeautifulSoup


def get_behind_name(name: str):
    r = requests.get(f"https://www.behindthename.com/name/{name}")
    soup = BeautifulSoup(r.text, 'html.parser')
    namemain = soup.find_all("div", class_ = "namemain")[0]
    name_content = list(namemain.next_siblings)[1].get_text()
    msg = name_content if name_content != '0' else f"Sorry, I don't know any '{name}'."
    return msg
