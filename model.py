# YOUR BOT LOGIC/STORAGE/BACKEND FUNCTIONS HERE
import io
from random import randint
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def get_behind_name(name: str):
    r = requests.get(f"https://www.behindthename.com/name/{name}")
    soup = BeautifulSoup(r.text, 'html.parser')
    namemain = soup.find_all("div", class_ = "namemain")
    if len(namemain) > 0:
        namemain = namemain[0]
        name_content = list(namemain.next_siblings)[1].get_text()
    else:
        print(f"could not find data for name: {name}")
        name_content = None
    msg = name_content if name_content else f"Sorry, I don't know any '{name}'."
    return msg


def matches_plot(callback_data):
    data = [randint(5, 95) for i in range(12)]
    zodiac = ['Aries ♈', 'Taurus ♉', 'Gemini ♊', 'Cancer ♋', 'Leo ♌', 'Virgo ♍', 'Libra ♎', 'Scorpio ♏', 'Sagittarius ♐', 'Capricorn ♑', 'Aquarius ♒', 'Pisces ♓']
    fig, ax = plt.subplots()
    ax: Axes
    ax.barh(zodiac, data, color = "darkviolet")
    title = f"❤ {zodiac[int(callback_data)]} and other signs as a MATCH ❤:"
    ax.set_title(title)
    ax.set_xlim(right=100)
    for i, v in enumerate(data):
        ax.text(v, i, " " + str(v), color = 'black', va = 'center', fontweight = 'bold')
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(bottom = 'off', left = 'off', labelleft = 'off', labelbottom = 'off')
    ax.set_xticks([])
    fig.tight_layout()
    bio = io.BytesIO()
    fig.savefig(bio)
    return bio
