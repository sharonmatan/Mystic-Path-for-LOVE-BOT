# YOUR BOT LOGIC/STORAGE/BACKEND FUNCTIONS HERE
import io
from random import randint
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def get_behind_name(name: str):
    r = requests.get(f"https://www.behindthename.com/name/{name}")
    soup = BeautifulSoup(r.text, 'html.parser')
    namemain = soup.find_all("div", class_ = "namemain")[0]
    name_content = list(namemain.next_siblings)[1].get_text()
    msg = name_content if name_content else f"Sorry, I don't know any '{name}'."
    return msg


def matches_plot():
    data = [randint(1, 100) for i in range(12)]
    zodiac = ['Aries ♈', 'Taurus ♉', 'Gemini ♊', 'Cancer ♋', 'Leo ♌', 'Virgo ♍', 'Libra ♎', 'Scorpio ♏', 'Sagittarius ♐', 'Capricorn ♑', 'Aquarius ♒', 'Pisces ♓']
    plt.barh(zodiac, data, color = "darkviolet")
    plt.title('Your Matches:')
    plt.xlim(right = 100)
    for i, v in enumerate(data):
        plt.text(v, i, " " + str(v), color = 'black', va = 'center', fontweight = 'bold')
    plt.tight_layout()
    bio = io.BytesIO()
    plt.savefig(bio)
    return bio
