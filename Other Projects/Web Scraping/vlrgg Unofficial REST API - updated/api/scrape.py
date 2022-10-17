import requests
from bs4 import BeautifulSoup
import utils.resources as res
import asyncio
import re


class Vlr:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }

    def get_soup(self, URL):
        response = requests.get(URL, headers=self.headers)

        html, status_code = response.text, response.status_code
        return BeautifulSoup(html, "html.parser"), status_code

    def vlr_recent(self):
        URL = "https://www.vlr.gg/news"

        soup, status = self.get_soup(URL)

        articles = soup.body.find_all(
            "a", class_="wf-module-item"
        )

        result = []
        for article in articles:

            # Titles of articles
            title = article.find(
                "div",
                attrs={"style": "font-weight: 700; font-size: 15px; line-height: 1.3;"},
            ).text.strip()

            # get descriptions of articles
            desc = article.find(
                "div",
                attrs={
                    "style": " font-size: 13px; padding: 5px 0; padding-bottom: 6px; line-height: 1.4;"
                },
            ).text.strip()

            date_and_author = article.find("div", class_="ge-text-light").text.strip()
            date, by_author = map(lambda s: s.strip(), date_and_author[1:].split("\u2022"))

            # get url_path of articles
            url = article["href"]

            result.append(
                {
                    "title": title,
                    "description": desc,
                    "date": date,
                    "author": by_author[3:],
                    "url_path": url,
                }
            )

        data = {
            "data": {
                "status": status,
                "segments": result
            }
        }

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    def vlr_rankings(self, region = None): # needs to be fixed
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = "https://www.vlr.gg/rankings/" + str(region)
        html = requests.get(URL, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        status = html.status_code

        tbody = soup.find("tbody")
        containers = tbody.findAll("tr")
        result = []
        for container in containers:
            # column 1
            rank_container = container.find("td", {"class": "rank-item-rank"})
            rank = rank_container.a.text.strip()
            # .get_text().strip()

            # column 2 - team
            team_container = container.find("td", {"class": "rank-item-team"})
            team = team_container.a.text.strip()
            team = team.replace("\t", " ")
            team = team.strip().split("  ")[0]

            # column 2 - logo
            logo_container = container.find("td", {"class": "rank-item-team"})
            img = logo_container.find("a").find("img")
            logo = "https:" + img["src"]

            # column 2 - ctry
            ctry_container = container.find("td", {"class": "rank-item-team"})
            ctry = ctry_container.a.div.text.replace("\t", " ").strip()
            ctry = ctry.strip().split("        ")[1]

            # column 4 - last played
            streak_container = container.find(
                "td", {"class": "rank-item-streak mod-right"}
            )
            streak = streak_container.a.span.text.replace("\t", " ").strip()
            streak = streak.replace("", " ").strip()
            streak = streak.replace("W", "Wins")
            streak = streak.replace("L", "Loss(s)")

            # column 4 - last played
            record_container = container.find(
                "td", {"class": "rank-item-record mod-right"}
            )
            record = record_container.a.text.strip()
            record = record.replace("\u2013", "-")

            # column 5 - Winnings
            winnings_container = container.find(
                "td", {"class": "rank-item-earnings mod-right"}
            )
            winnings = winnings_container.a.text.strip()

            # link to team
            profile_container = container.find("td", {"class": "rank-item-team"})
            profile = profile_container.find("a")["href"]

            result.append(
                {
                    "rank": rank,
                    "team": team,
                    "country": ctry,
                    "streak": streak,
                    "record": record,
                    "winnings": winnings,
                    "logo": logo,
                    "url_path": profile,
                }
            )
        segments = {"status": status, "segments": result}

        data = {"data": segments}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    def vlr_score(self, page = 1): # added page keyword
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = "https://www.vlr.gg/matches/results/?page=" + str(page) # added page keyword
        html = requests.get(URL, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        status = html.status_code

        base = soup.find(id="wrapper")

        vlr_module = base.find_all(
            "a",
            {"class": "wf-module-item"},
        )

        result = []
        for module in vlr_module:
            # link to match info
            url_path = module["href"]

            # Match completed time
            eta_container = module.find("div", {"class": "match-item-eta"})
            eta = (
                eta_container.find("div", {"class": "ml-eta mod-completed"})
                .get_text()
                .strip()
            ) + " ago"

            # round of tounranment
            round_container = module.find("div", {"class": "match-item-event text-of"})
            round = (
                round_container.find(
                    "div", {"class": "match-item-event-series text-of"}
                )
                .get_text()
                .strip()
            )
            round = round.replace("\u2013", "-")

            # tournament name
            tourney = (
                module.find("div", {"class": "match-item-event text-of"})
                .get_text()
                .strip()
            )
            tourney = tourney.replace("\t", " ")
            tourney = tourney.strip().split("\n")[1]
            tourney = tourney.strip()

            # tournament icon
            tourney_icon = module.find("img")["src"]
            tourney_icon = f"https:{tourney_icon}"

            # flags # this was causing error with older pages
#             flags_container = module.findAll("div", {"class": "text-of"})
#             flag1 = flags_container[0].span.get("class")[1]
#             flag1 = flag1.replace("-", " ")
#             flag1 = "flag_" + flag1.strip().split(" ")[1]

#             flag2 = flags_container[1].span.get("class")[1]
#             flag2 = flag2.replace("-", " ")
#             flag2 = "flag_" + flag2.strip().split(" ")[1]

            # match items
            match_container = (
                module.find("div", {"class": "match-item-vs"}).get_text().strip()
            )

            match_array = match_container.replace("\t", " ").replace("\n", " ")
            match_array = match_array.strip().split(
                "                                  "
            )
            # 1st item in match_array is first team
            team1 = match_array[0]
            # 2nd item in match_array is first team score
            score1 = match_array[1]
            # 3rd item in match_array is second team                            
            team2 = match_array[2].strip()
            # 4th item in match_array is second team score
            score2 = match_array[-1]

            result.append(
                {
                    "team1": team1,
                    "team2": team2,
                    "score1": score1,
                    "score2": score2,
#                     "flag1": flag1, # this was causing error with older pages
#                     "flag2": flag2, # this was causing error with older pages
                    "time_completed": eta,
                    "round_info": round,
                    "tournament_name": tourney,
                    "match_page": url_path,
                    "tournament_icon": tourney_icon,
                }
            )
        segments = {"status": status, "segments": result}

        data = {"data": segments}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    def vlr_stats(self, region = None, agent = 'all', map_id = 'all'):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = f"https://www.vlr.gg/stats/?event_group_id=all&event_id=all&region={region}&country=all&min_rounds=1&min_rating=1&agent={agent}&map_id={map_id}&timespan=all"
        html = requests.get(URL, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        status = html.status_code

        tbody = soup.find("tbody")
        containers = tbody.findAll("tr")

        result = []
        for container in containers:
            # name of player
            player_container = container.find("td", {"class": "mod-player mod-a"})
            player = player_container.a.div.text.replace("\n", " ").strip()
            player = player.split(" ")[0]

            # org name for player
            org_container = container.find("div", {"class": "stats-player-country"})
            org = org_container.text.strip()

            # stats for player
            stats_container = container.findAll("td", {"class": "mod-color-sq"})
            acs = stats_container[-10].div.text.strip()
            kd = stats_container[-9].div.text.strip()
            adr = stats_container[-7].div.text.strip()
            kpr = stats_container[-6].div.text.strip()
            apr = stats_container[-5].div.text.strip()
            fkpr = stats_container[-4].div.text.strip()
            fdpr = stats_container[-3].div.text.strip()
            hs = stats_container[-2].div.text.strip()
            
            # max kill for player # added
            maxk_container = container.find("td", {"class": "mod-a mod-kmax"})
            maxk = maxk_container.a.text.strip()
            
            # total stats for player # added
            total_container = container.findAll("td")
            rds = total_container[2].text.strip()
            clp = total_container[10].text.strip()
            cl = total_container[13].text.strip()
            totalk = total_container[14].text.strip()
            totald = total_container[15].text.strip()
            totala = total_container[16].text.strip()
            totalfk = total_container[17].text.strip()
            totalfd = total_container[18].text.strip()

            result.append(
                {
                    "player": player,
                    "org": org,
                    
                    "rds": rds, # added total rounds
                    
                    "average_combat_score": acs,
                    "kill_deaths": kd,
                    "average_damage_per_round": adr,
                    
                    "kills_per_round": kpr,
                    "assists_per_round": apr,
                    "first_kills_per_round": fkpr,
                    "first_deaths_per_round": fdpr,
                    "headshot_percentage": hs,
                    "clutch_success_percentage": clp,
                    'clutch (won/played)': cl,
                    'total_kills': totalk,
                    'total_deaths': totald,
                    'total_assists': totala,
                    'total_first_kills': totalfk,
                    'total_first_deaths': totalfd,
                    
                    "map_id": map_id,
                    "agent": agent,
                    "region": region
                }
            )
        segments = {"status": status, "segments": result}

        data = {"data": segments}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    def vlr_upcoming(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = "https://www.vlr.gg/matches"
        html = requests.get(URL, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        status = html.status_code

        base = soup.find(id="wrapper")

        vlr_module = base.find_all(
            "a",
            {"class": "wf-module-item"},
        )

        result = []
        for module in vlr_module:
            # link to match info
            url_path = module["href"]

            # Match completed time
            eta_container = module.find("div", {"class": "match-item-eta"})
            eta = "TBD"
            eta_time = eta_container.find("div", {"class": "ml-eta"})
            if eta_time is not None:
                eta = (
                    eta_time
                    .get_text()
                    .strip()
                ) + " from now"

            # round of tournament
            round_container = module.find("div", {"class": "match-item-event text-of"})
            round = (
                round_container.find(
                    "div", {"class": "match-item-event-series text-of"}
                )
                .get_text()
                .strip()
            )
            round = round.replace("\u2013", "-")

            # tournament name
            tourney = (
                module.find("div", {"class": "match-item-event text-of"})
                .get_text()
                .strip()
            )
            tourney = tourney.replace("\t", " ")
            tourney = tourney.strip().split("\n")[1]
            tourney = tourney.strip()

            # tournament icon
            tourney_icon = module.find("img")["src"]
            tourney_icon = f"https:{tourney_icon}"

            # flags 
            flags_container = module.findAll("div", {"class": "text-of"})
            flag1 = flags_container[0].span.get("class")[1]
            flag1 = flag1.replace("-", " ")
            flag1 = "flag_" + flag1.strip().split(" ")[1]

            flag2 = flags_container[1].span.get("class")[1]
            flag2 = flag2.replace("-", " ")
            flag2 = "flag_" + flag2.strip().split(" ")[1]

            # match items
            match_container = (
                module.find("div", {"class": "match-item-vs"}).get_text().strip()
            )

            match_array = match_container.replace("\t", " ").replace("\n", " ")
            match_array = match_array.strip().split(
                "                                  "
            )
            team1 = "TBD"
            team2 = "TBD"
            if match_array is not None and len(match_array) > 1:
                team1 = match_array[0]
                team2 = match_array[2].strip()
            result.append(
                {
                    "team1": team1,
                    "team2": team2,
                    "flag1": flag1,
                    "flag2": flag2,
                    "time_until_match": eta,
                    "round_info": round,
                    "tournament_name": tourney,
                    "match_page": url_path,
                    "tournament_icon": tourney_icon,
                }
            )
        segments = {"status": status, "segments": result}

        data = {"data": segments}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data
        
    def vlr_matchpage(self, subURL=None):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = "https://www.vlr.gg" + subURL
        html = requests.get(URL, headers=headers)
        soup = BeautifulSoup(html.content, "html.parser")
        status = html.status_code

        base = soup.find(id="wrapper")
        
        result = []
        
        # event link and event name
        match_header = base.find('div', {'class':'match-header-super'})
        event_link = match_header.div.a['href']
        event_name = match_header.div.a.text.strip('\t\n')
        event_name = re.sub('\s+',' ', event_name)

        
        # match date and time
        match_datetime = base.find('div', {'class':'moment-tz-convert'})
        match_utc = match_datetime['data-utc-ts']
        
        # team names
        match_teams = base.findAll('div', {'class':'wf-title-med'})
        team1 = match_teams[0].text.strip()
        team2 = match_teams[1].text.strip()
        
        # team scores
        score1 = base.find('span', {'class':'match-header-vs-score-winner'}).text.strip()
        score2 = base.find('span', {'class':'match-header-vs-score-loser'}).text.strip()
        
        # match type (bo1, bo3, bo5)
        type = base.findAll('div', {'class':'match-header-vs-note'})[1].text.strip()
        
        p_team1 = []
        p_team2 = []
        a_team1 = []
        a_team2 = []
        
        if type.lower() == 'bo1':
            # map name
            map_number = 1
            map_name = base.find('div', {'class':'map'}).span.text.strip()
            map_duration = base.find('div', {'class':'map-duration ge-text-light'}).text.strip()
            
            # map score, t, and ct
            map_team1 = base.find('div', {'class':'team'})
            map_team1_score = map_team1.find('div', {'class': 'score'}).text.strip()
            map_team1_t = map_team1.find('span', {'class':'mod-t'}).text.strip()
            map_team1_ct = map_team1.find('span', {'class':'mod-ct'}).text.strip()
            map_team2 = base.find('div', {'class':'team mod-right'})
            map_team2_score = map_team2.find('div', {'class': 'score'}).text.strip()
            map_team2_t = map_team2.find('span', {'class':'mod-t'}).text.strip()
            map_team2_ct = map_team2.find('span', {'class':'mod-ct'}).text.strip()
            
            # round info - idk
            
            # score table
            scoretable = base.findAll('table', {'class':'wf-table-inset mod-overview'})
            
            # player names
            players = scoretable[0].findAll('div', {'class':'text-of'})
            for p in players:
                p_team1.append(p.text.strip())
            players = scoretable[1].findAll('div', {'class':'text-of'})
            for p in players:
                p_team2.append(p.text.strip())
            
            # agent names
            agents = scoretable[0].findAll('span', {'class':'stats-sq mod-agent small'})
            for a in agents:
                a_team1.append(a.img['title'])             
            agents = scoretable[1].findAll('span', {'class':'stats-sq mod-agent small'})
            for a in agents:
                a_team2.append(a.img['title'])
            
            # player stats
            st = ['acds','k','d','a','kd','kast','adr','hs','fk','fd','fkfd']           
            team1_st = []
            stats = scoretable[0].findAll('td', {'class':'mod-stat'})
            for v in range(len(st)*5):
                team1_st.append(stats[v].text.strip().strip('/'))
            team2_st = []
            stats = scoretable[1].findAll('td', {'class':'mod-stat'})
            for v in range(len(st)*5):
                team2_st.append(stats[v].text.strip().strip('/'))
             
            # bo1 results 
            result.append(
                {
                    'event_link': event_link,
                    'event_name': event_name,                
                    'match_utc': match_utc,
                    'team1': team1,
                    'team2': team2,
                    'score1': score1,
                    'score2': score2,
                    'type': type,
                    
                    'map_number': map_number,
                    'map_name': map_name,
                    'map_duration': map_duration,
                    'map_team1_score': map_team1_score,
                    'map_team1_t': map_team1_t,
                    'map_team1_ct': map_team1_ct,
                    'map_team2_score': map_team2_score,
                    'map_team2_t': map_team2_t,
                    'map_team2_ct': map_team2_ct,
                    
                    'team1_player1': p_team1[0],
                    'team1_player2': p_team1[1],
                    'team1_player3': p_team1[2],
                    'team1_player4': p_team1[3],
                    'team1_player5': p_team1[4],
                    
                    'team1_agent1': a_team1[0],
                    'team1_agent2': a_team1[1],
                    'team1_agent3': a_team1[2],
                    'team1_agent4': a_team1[3],
                    'team1_agent5': a_team1[4],
                    
                    'team1_player1_acs' : team1_st[0],
                    'team1_player1_k' : team1_st[1],
                    'team1_player1_d' : team1_st[2],
                    'team1_player1_a' : team1_st[3],
                    'team1_player1_kd' : team1_st[4],
                    'team1_player1_kast' : team1_st[5],
                    'team1_player1_adr' : team1_st[6],
                    'team1_player1_hs' : team1_st[7],
                    'team1_player1_fk' : team1_st[8],
                    'team1_player1_fd' : team1_st[9],
                    'team1_player1_fkfd' : team1_st[10],
                    
                    'team1_player2_acs' : team1_st[11],
                    'team1_player2_k' : team1_st[12],
                    'team1_player2_d' : team1_st[13],
                    'team1_player2_a' : team1_st[14],
                    'team1_player2_kd' : team1_st[15],
                    'team1_player2_kast' : team1_st[16],
                    'team1_player2_adr' : team1_st[17],
                    'team1_player2_hs' : team1_st[18],
                    'team1_player2_fk' : team1_st[19],
                    'team1_player2_fd' : team1_st[20],
                    'team1_player2_fkfd' : team1_st[21],
                    
                    'team1_player3_acs' : team1_st[22],
                    'team1_player3_k' : team1_st[23],
                    'team1_player3_d' : team1_st[24],
                    'team1_player3_a' : team1_st[25],
                    'team1_player3_kd' : team1_st[26],
                    'team1_player3_kast' : team1_st[27],
                    'team1_player3_adr' : team1_st[28],
                    'team1_player3_hs' : team1_st[29],
                    'team1_player3_fk' : team1_st[30],
                    'team1_player3_fd' : team1_st[31],
                    'team1_player3_fkfd' : team1_st[32],
                    
                    'team1_player4_acs' : team1_st[33],
                    'team1_player4_k' : team1_st[34],
                    'team1_player4_d' : team1_st[35],
                    'team1_player4_a' : team1_st[36],
                    'team1_player4_kd' : team1_st[37],
                    'team1_player4_kast' : team1_st[38],
                    'team1_player4_adr' : team1_st[39],
                    'team1_player4_hs' : team1_st[40],
                    'team1_player4_fk' : team1_st[41],
                    'team1_player4_fd' : team1_st[42],
                    'team1_player4_fkfd' : team1_st[43],
                    
                    'team1_player5_acs' : team1_st[44],
                    'team1_player5_k' : team1_st[45],
                    'team1_player5_d' : team1_st[46],
                    'team1_player5_a' : team1_st[47],
                    'team1_player5_kd' : team1_st[48],
                    'team1_player5_kast' : team1_st[49],
                    'team1_player5_adr' : team1_st[50],
                    'team1_player5_hs' : team1_st[51],
                    'team1_player5_fk' : team1_st[52],
                    'team1_player5_fd' : team1_st[53],
                    'team1_player5_fkfd' : team1_st[54],
                    
                    'team2_player1': p_team2[0],                
                    'team2_player2': p_team2[1],
                    'team2_player3': p_team2[2],
                    'team2_player4': p_team2[3],
                    'team2_player5': p_team2[4],
                    
                    'team2_agent1': a_team2[0],
                    'team2_agent2': a_team2[1],
                    'team2_agent3': a_team2[2],
                    'team2_agent4': a_team2[3],
                    'team2_agent5': a_team2[4],

                    'team2_player1_acs' : team2_st[0],
                    'team2_player1_k' : team2_st[1],
                    'team2_player1_d' : team2_st[2],
                    'team2_player1_a' : team2_st[3],
                    'team2_player1_kd' : team2_st[4],
                    'team2_player1_kast' : team2_st[5],
                    'team2_player1_adr' : team2_st[6],
                    'team2_player1_hs' : team2_st[7],
                    'team2_player1_fk' : team2_st[8],
                    'team2_player1_fd' : team2_st[9],
                    'team2_player1_fkfd' : team2_st[10],
                    
                    'team2_player2_acs' : team2_st[11],
                    'team2_player2_k' : team2_st[12],
                    'team2_player2_d' : team2_st[13],
                    'team2_player2_a' : team2_st[14],
                    'team2_player2_kd' : team2_st[15],
                    'team2_player2_kast' : team2_st[16],
                    'team2_player2_adr' : team2_st[17],
                    'team2_player2_hs' : team2_st[18],
                    'team2_player2_fk' : team2_st[19],
                    'team2_player2_fd' : team2_st[20],
                    'team2_player2_fkfd' : team2_st[21],
                   
                    'team2_player3_acs' : team2_st[22],
                    'team2_player3_k' : team2_st[23],
                    'team2_player3_d' : team2_st[24],
                    'team2_player3_a' : team2_st[25],
                    'team2_player3_kd' : team2_st[26],
                    'team2_player3_kast' : team2_st[27],
                    'team2_player3_adr' : team2_st[28],
                    'team2_player3_hs' : team2_st[29],
                    'team2_player3_fk' : team2_st[30],
                    'team2_player3_fd' : team2_st[31],
                    'team2_player3_fkfd' : team2_st[32],
                    
                    'team2_player4_acs' : team2_st[33],
                    'team2_player4_k' : team2_st[34],
                    'team2_player4_d' : team2_st[35],
                    'team2_player4_a' : team2_st[36],
                    'team2_player4_kd' : team2_st[37],
                    'team2_player4_kast' : team2_st[38],
                    'team2_player4_adr' : team2_st[39],
                    'team2_player4_hs' : team2_st[40],
                    'team2_player4_fk' : team2_st[41],
                    'team2_player4_fd' : team2_st[42],
                    'team2_player4_fkfd' : team2_st[43],
                    
                    'team2_player5_acs' : team2_st[44],
                    'team2_player5_k' : team2_st[45],
                    'team2_player5_d' : team2_st[46],
                    'team2_player5_a' : team2_st[47],
                    'team2_player5_kd' : team2_st[48],
                    'team2_player5_kast' : team2_st[49],
                    'team2_player5_adr' : team2_st[50],
                    'team2_player5_hs' : team2_st[51],
                    'team2_player5_fk' : team2_st[52],
                    'team2_player5_fd' : team2_st[53],
                    'team2_player5_fkfd' : team2_st[54]
                }
            )
            
            segments = {"status": status, "segments": result}
        
        elif type.lower() != 'bo1':    
        
            # find other maps
            maps = []
            map_list = base.findAll('div', {'class':'vm-stats-gamesnav-item js-map-switch'})
            for m in map_list:
                maps.append(m['data-game-id'])
            
            for i, m in enumerate(maps):
                URL = "https://www.vlr.gg" + subURL + "/?game=" + m
                html = requests.get(URL, headers=headers)
                soup = BeautifulSoup(html.content, "html.parser")
                status = html.status_code
    
                # base[i] = soup.find(id="wrapper")
            
                # map name
                map_number = i+1
                
                game_id = soup.find('div', {'class':"vm-stats-game", 'data-game-id':str(m)})
                map_name = game_id.find('div', {'class':'map'}).span.text.strip()
                map_duration = game_id.find('div', {'class':'map-duration ge-text-light'}).text.strip()
                
                # map score, t, and ct
                map_team1 = game_id.find('div', {'class':'team'})
                map_team1_score = map_team1.find('div', {'class': 'score'}).text.strip()
                map_team1_t = map_team1.find('span', {'class':'mod-t'}).text.strip()
                map_team1_ct = map_team1.find('span', {'class':'mod-ct'}).text.strip()
                map_team2 = game_id.find('div', {'class':'team mod-right'})
                map_team2_score = map_team2.find('div', {'class': 'score'}).text.strip()
                map_team2_t = map_team2.find('span', {'class':'mod-t'}).text.strip()
                map_team2_ct = map_team2.find('span', {'class':'mod-ct'}).text.strip()
        
                scoretable = game_id.findAll('table', {'class':'wf-table-inset mod-overview'})
            
                # player names
                players = scoretable[0].findAll('div', {'class':'text-of'})
                for p in players:
                    p_team1.append(p.text.strip())
                players = scoretable[1].findAll('div', {'class':'text-of'})
                for p in players:
                    p_team2.append(p.text.strip())
                
                # agent names
                agents = scoretable[0].findAll('span', {'class':'stats-sq mod-agent small'})
                for a in agents:
                    a_team1.append(a.img['title'])             
                agents = scoretable[1].findAll('span', {'class':'stats-sq mod-agent small'})
                for a in agents:
                    a_team2.append(a.img['title'])
                
                # player stats
                st = ['acds','k','d','a','kd','kast','adr','hs','fk','fd','fkfd']           
                team1_st = []
                stats = scoretable[0].findAll('td', {'class':'mod-stat'})
                for v in range(len(st)*5):
                    team1_st.append(stats[v].text.strip().strip('/'))
                team2_st = []
                stats = scoretable[1].findAll('td', {'class':'mod-stat'})
                for v in range(len(st)*5):
                    team2_st.append(stats[v].text.strip().strip('/'))
                    
                # bo3 results
                
                result.append(
                    {
                        'event_link': event_link,
                        'event_name': event_name,                
                        'match_utc': match_utc,
                        'team1': team1,
                        'team2': team2,
                        'score1': score1,
                        'score2': score2,
                        'type': type,
                        
                        'map_number': map_number,
                        'map_name': map_name,
                        'map_duration': map_duration,
                        'map_team1_score': map_team1_score,
                        'map_team1_t': map_team1_t,
                        'map_team1_ct': map_team1_ct,
                        'map_team2_score': map_team2_score,
                        'map_team2_t': map_team2_t,
                        'map_team2_ct': map_team2_ct,
                        
                        'team1_player1': p_team1[0],
                        'team1_player2': p_team1[1],
                        'team1_player3': p_team1[2],
                        'team1_player4': p_team1[3],
                        'team1_player5': p_team1[4],
                        
                        'team1_agent1': a_team1[0],
                        'team1_agent2': a_team1[1],
                        'team1_agent3': a_team1[2],
                        'team1_agent4': a_team1[3],
                        'team1_agent5': a_team1[4],
                        
                        'team1_player1_acs' : team1_st[0],
                        'team1_player1_k' : team1_st[1],
                        'team1_player1_d' : team1_st[2],
                        'team1_player1_a' : team1_st[3],
                        'team1_player1_kd' : team1_st[4],
                        'team1_player1_kast' : team1_st[5],
                        'team1_player1_adr' : team1_st[6],
                        'team1_player1_hs' : team1_st[7],
                        'team1_player1_fk' : team1_st[8],
                        'team1_player1_fd' : team1_st[9],
                        'team1_player1_fkfd' : team1_st[10],
                        
                        'team1_player2_acs' : team1_st[11],
                        'team1_player2_k' : team1_st[12],
                        'team1_player2_d' : team1_st[13],
                        'team1_player2_a' : team1_st[14],
                        'team1_player2_kd' : team1_st[15],
                        'team1_player2_kast' : team1_st[16],
                        'team1_player2_adr' : team1_st[17],
                        'team1_player2_hs' : team1_st[18],
                        'team1_player2_fk' : team1_st[19],
                        'team1_player2_fd' : team1_st[20],
                        'team1_player2_fkfd' : team1_st[21],
                        
                        'team1_player3_acs' : team1_st[22],
                        'team1_player3_k' : team1_st[23],
                        'team1_player3_d' : team1_st[24],
                        'team1_player3_a' : team1_st[25],
                        'team1_player3_kd' : team1_st[26],
                        'team1_player3_kast' : team1_st[27],
                        'team1_player3_adr' : team1_st[28],
                        'team1_player3_hs' : team1_st[29],
                        'team1_player3_fk' : team1_st[30],
                        'team1_player3_fd' : team1_st[31],
                        'team1_player3_fkfd' : team1_st[32],
                        
                        'team1_player4_acs' : team1_st[33],
                        'team1_player4_k' : team1_st[34],
                        'team1_player4_d' : team1_st[35],
                        'team1_player4_a' : team1_st[36],
                        'team1_player4_kd' : team1_st[37],
                        'team1_player4_kast' : team1_st[38],
                        'team1_player4_adr' : team1_st[39],
                        'team1_player4_hs' : team1_st[40],
                        'team1_player4_fk' : team1_st[41],
                        'team1_player4_fd' : team1_st[42],
                        'team1_player4_fkfd' : team1_st[43],
                        
                        'team1_player5_acs' : team1_st[44],
                        'team1_player5_k' : team1_st[45],
                        'team1_player5_d' : team1_st[46],
                        'team1_player5_a' : team1_st[47],
                        'team1_player5_kd' : team1_st[48],
                        'team1_player5_kast' : team1_st[49],
                        'team1_player5_adr' : team1_st[50],
                        'team1_player5_hs' : team1_st[51],
                        'team1_player5_fk' : team1_st[52],
                        'team1_player5_fd' : team1_st[53],
                        'team1_player5_fkfd' : team1_st[54],
                        
                        'team2_player1': p_team2[0],                
                        'team2_player2': p_team2[1],
                        'team2_player3': p_team2[2],
                        'team2_player4': p_team2[3],
                        'team2_player5': p_team2[4],
                        
                        'team2_agent1': a_team2[0],
                        'team2_agent2': a_team2[1],
                        'team2_agent3': a_team2[2],
                        'team2_agent4': a_team2[3],
                        'team2_agent5': a_team2[4],

                        'team2_player1_acs' : team2_st[0],
                        'team2_player1_k' : team2_st[1],
                        'team2_player1_d' : team2_st[2],
                        'team2_player1_a' : team2_st[3],
                        'team2_player1_kd' : team2_st[4],
                        'team2_player1_kast' : team2_st[5],
                        'team2_player1_adr' : team2_st[6],
                        'team2_player1_hs' : team2_st[7],
                        'team2_player1_fk' : team2_st[8],
                        'team2_player1_fd' : team2_st[9],
                        'team2_player1_fkfd' : team2_st[10],
                        
                        'team2_player2_acs' : team2_st[11],
                        'team2_player2_k' : team2_st[12],
                        'team2_player2_d' : team2_st[13],
                        'team2_player2_a' : team2_st[14],
                        'team2_player2_kd' : team2_st[15],
                        'team2_player2_kast' : team2_st[16],
                        'team2_player2_adr' : team2_st[17],
                        'team2_player2_hs' : team2_st[18],
                        'team2_player2_fk' : team2_st[19],
                        'team2_player2_fd' : team2_st[20],
                        'team2_player2_fkfd' : team2_st[21],
                       
                        'team2_player3_acs' : team2_st[22],
                        'team2_player3_k' : team2_st[23],
                        'team2_player3_d' : team2_st[24],
                        'team2_player3_a' : team2_st[25],
                        'team2_player3_kd' : team2_st[26],
                        'team2_player3_kast' : team2_st[27],
                        'team2_player3_adr' : team2_st[28],
                        'team2_player3_hs' : team2_st[29],
                        'team2_player3_fk' : team2_st[30],
                        'team2_player3_fd' : team2_st[31],
                        'team2_player3_fkfd' : team2_st[32],
                        
                        'team2_player4_acs' : team2_st[33],
                        'team2_player4_k' : team2_st[34],
                        'team2_player4_d' : team2_st[35],
                        'team2_player4_a' : team2_st[36],
                        'team2_player4_kd' : team2_st[37],
                        'team2_player4_kast' : team2_st[38],
                        'team2_player4_adr' : team2_st[39],
                        'team2_player4_hs' : team2_st[40],
                        'team2_player4_fk' : team2_st[41],
                        'team2_player4_fd' : team2_st[42],
                        'team2_player4_fkfd' : team2_st[43],
                        
                        'team2_player5_acs' : team2_st[44],
                        'team2_player5_k' : team2_st[45],
                        'team2_player5_d' : team2_st[46],
                        'team2_player5_a' : team2_st[47],
                        'team2_player5_kd' : team2_st[48],
                        'team2_player5_kast' : team2_st[49],
                        'team2_player5_adr' : team2_st[50],
                        'team2_player5_hs' : team2_st[51],
                        'team2_player5_fk' : team2_st[52],
                        'team2_player5_fd' : team2_st[53],
                        'team2_player5_fkfd' : team2_st[54]
                    }
                )
            
            segments = {"status": status, "segments": result}

        data = {"data": segments}
           
        if status != 200:
            raise Exception("API response: {}".format(status))
        return data