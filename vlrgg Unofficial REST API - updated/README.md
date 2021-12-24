# vlrggapi

An Unofficial REST API for [vlr.gg](https://www.vlr.gg/), a site for Valorant Esports match and news coverage.

Built by [Andre Saddler](https://github.com/rehkloos/)
Original GitHub: [Link](https://github.com/axsddlr/vlrggapi)

[![heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Edited by [Fakhri Nurrahmadi](https://github.com/fnurrahmadi) - first update on 2021-12-24
Editid GitHub: [Link](https://github.com/fnurrahmadi/data-science-portfolio/tree/main/vlrgg%20Unofficial%20REST%20API%20-%20updated)

## Current Endpoints

All endpoints are relative to https://vlrggapi.herokuapp.com.

### `/news`

Working as of 2021-12-24.

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                  'title': str,
                  'description': str,
                  'date': str,
                  'author': str,
                  'url_path': str
              }
          ],
      }
  }
  ```

### `/matches/results`

Working as of 2021-12-24.

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                "team1": str,
                "team2": str,
                "score1": str,
                "score2": str,
                "time_completed": str,
                "round_info": str,
                "tournament_name": str,
                "match_page": str,
                "tournament_icon": str
              }
          ],
      }
  }
  ```

### `/rankings/<region>`

Rankings currently not working as rankings page is in beta and vlr.gg keep updating the layout.

- Method: `GET`
- Region: `north-america`, `europe`, `asia-pacific`, `latin-america`, `oceania`, `korea`, `mena`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                  'rank': str,
                  'team': str,
                  'country': str,
                  'streak': str,
                  'record': str,
                  'winnings': str,
                  'logo': str,
                  'url_path': str
              }
          ],
      }
  }
  ```

### `/stats/<region>`

Working as of 2021-12-24.

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Region: `na`, `eu`, `ap`, `sa`, `oce`, `mn`
- Agents: 'astra','breach','brimstone','chamber','cypher',
         'jett','kayo','killjoy','omen','phoenix','raze',
         'reyna','sage','skye','sova','viper','yoru'
- Map IDs: '1': bind, '2': haven, '3': split, '5': ascent, '6': icebox, '8': breeze, '9': fracture
- Response: 
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                    "player": str,
                    "org": str,
                    
                    "rds": str,
                    
                    "average_combat_score": str,
                    "kill_deaths": str,
                    "average_damage_per_round": str,
                    
                    "kills_per_round": str,
                    "assists_per_round": str,
                    "first_kills_per_round": str,
                    "first_deaths_per_round": str,
                    "headshot_percentage": str,
                    "clutch_success_percentage": str,
                    'clutch (won/played)': str,
                    'total_kills': str,
                    'total_deaths': str,
                    'total_assists': str,
                    'total_first_kills': str,
                    'total_first_deaths': str,
                    
                    "map_id": str,
                    "agent": str,
                    "region": str
              }
          ],
      }
  }
  ```

## Installation

### Source

```
$ git clone https://github.com/rehkloos/vlrggapi/
$ cd vlrggapi
$ pip3 install -r requirements.txt
```

### Usage

```
python3 main.py
```

'''
Edited: Please find the .ipynb notebook for reference on how to call the functions.
'''

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Flask-Caching](https://github.com/sh4nks/flask-caching)
- [gunicorn](https://gunicorn.org/)

## Contributing

*to the original creators*

Feel free to submit a [pull request](https://github.com/rehkloos/vlrggapi/pull/new/master) or an [issue](https://github.com/rehkloos/vlrggapi/issues/new)!

## License

The MIT License (MIT)
