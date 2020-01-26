# YOUR BOT LOGIC/STORAGE/BACKEND FUNCTIONS HERE
import requests


def get_behind_name(name: str):
    r = requests.get(f"https://www.behindthename.com/name/{name}")
    print(r.headers)
    start_index = r.text.find("Meaning & History")
    print(start_index)
    end_index = r.text.find("</div>", start_index+33)
    print(end_index)
    # print(start_index, end_index)
    age = r.text[start_index+35:end_index] if start_index != -1 else '0'
    # print(age, type(age))
    msg = age if age != '0' else f"Sorry, I don't know any '{name}'."
    return msg