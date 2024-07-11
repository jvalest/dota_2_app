import requests

match_id = input('Please enter a match id: ')

url = f'https://api.opendota.com/api/matches/{match_id}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    match_time = data['duration']
    match_winner = data['radiant_win']
    radiant_kill_count = data['radiant_score']
    dire_kill_count = data['dire_score']
    print(f'for match id: {match_id} the following happened:')
    if match_winner == True:
        print(f'Radiant Victory!')
    else:
        print(f'Dire Victory!')
    print(f'Radiant had {radiant_kill_count} kills while Dire had {dire_kill_count}')
else:
    print(f'Trouble locating match id {match_id}, please double check your match id.')