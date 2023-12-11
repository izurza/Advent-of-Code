import requests
from pathlib import Path

def get_input(day=1, year=2023):
    cookies = {
        'session': '<COOKIE-VALUE>'
    }
    r = requests.post(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)

    p = Path(f'{year}/day{day}')
    p.mkdir(parents=True, exist_ok=True)

    with open(f'{p}/day{day}.in','w+') as f:
        f.write(r.text)

get_input()
