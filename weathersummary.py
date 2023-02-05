import requests
from bs4 import BeautifulSoup
import openai
from gtts import gTTS
import time
import os

def get_text():
    url = 'https://www.wpc.ncep.noaa.gov/discussions/hpcdiscussions.php?disc=pmdspd&version=0&fmt=reg'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    div_element = soup.find('div', attrs={'style': "line-height:130%;font-family:verdana;font-size:1em;"})

    text = div_element.text
    print(text)
    return text
def generate_summary(text):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"generate a 200 word summary of this text in a very silly tone in the voice of Ron Burgundy doing the weather for the lair of morpheus \n {text}",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=1,
        api_key="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"
    )

    message = completions.choices[0].text
    return message
while True:
    summary = get_text()
    burgundy= generate_summary(summary)
    tts = gTTS(burgundy)
    tts.save("weather.mp3")

    os.system("mpg321 weather.mp3")
    time.sleep(7200) # sleep for 2 hours