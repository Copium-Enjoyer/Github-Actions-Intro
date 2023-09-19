import requests
import re
import pandas as pd
import datetime
import pytz

x = requests.get('https://lichess.org/')
date = datetime.datetime.now(tz=pytz.timezone('Poland'))

if x.status_code == 200:

    m = re.search(r'("members":\d+\,"rounds":\d+)', x.text)
    print(m.group(0))
    n = re.findall(r'\d+', m.group(0))
    print(n)


    lichess = pd.read_csv("lichess.csv")

    print(lichess)

    data = {
        'Date': [date],
        'Players': [n[0]],
        'Games': [n[1]]
    }

    pd.DataFrame(data).to_csv("lichess.csv", mode='a', index=False, header=False)

    


    # print(x.headers['data-count'])

