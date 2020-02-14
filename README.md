## With just your name and zodiac sign we will find your love!

A telegram bot that mystically examines your future love.
* It first shows details of your name (from the API).
* He then checks your chances of success with any luck and shows them in the graph.
* Finally, he asks you to choose a magician who will read your fortunes and tell you exactly when and where you will find your love.

By:
* Hagit Ram
* Matan Shaorn

## How to Run This Bot
### Prerequisites
* Python 3.7 or 3.8
* pipenv
* {ADD MORE DEPENDENCIES HERE - FOR EXAMPLE MONGODB OR ANYTHING ELSE}

### Setup
* Clone this repo from github
* Install dependencies: `pipenv install`
* Get a BOT ID from the [botfather](https://telegram.me/BotFather).
* Create a `secrets.py` file:

        BOT_TOKEN = "your-bot-token-here"

### Run
To run the bot use:

    pipenv run python bot.py

### Running tests
First make sure to install all dev dependencies:

    pipenv install --dev

To run all test  use:

    pipenv run pytest

(Or just `pytest` if running in a pipenv shell.)

## Credits and References
* [Telegram Docs](https://core.telegram.org/bots)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* Thanks for: Udi Oron, Yaniv mirel, Eran keidar, Itzak Hirschman, Omer Daniel, Rinat Nadav ,Ibrahim Abu Rmailah.
* also to:
* https://matplotlib.org/gallery/lines_bars_and_markers/barh.html
* https://stackoverflow.com/questions/12998430/remove-xticks-in-a-matplotlib-plot
* https://www.behindthename.com/
* https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard.py
* https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
* https://www.numerology.com/numerology-numbers/6
* https://www.horoscope.com/us/tarot/tarot-egyptian-love.aspx
* https://justastrologythings.com/pages/chart/

