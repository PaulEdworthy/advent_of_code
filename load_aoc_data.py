import requests
import os
from dotenv import load_dotenv


load_dotenv()

def get_aoc_input(year, day):
    session_cookie = {'session': os.getenv('AOC_SESSION_COOKIE')}
    
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(url, cookies=session_cookie)
    return response.text.strip().split('\n') # strip whitespace and split into lines

    # or save the data to a file
    # with open('aoc_data.txt', w) as f:
    #     f.write(response.text)

    if response.status_code == 200:
        print("Data downloaded successfully")
        return data

    else:
        print(f"Failed to download input for Day {day}")
        return None
