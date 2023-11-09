from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

### WEB VARIABLES ###
web = 'web_scraping_practice\\FBref\\fbref_pl_match.html'
result = open(web, 'r', encoding='utf8')
content = result.read()

### GET FROM DATABASE ###
home_team_id = '47c64c55'
away_team_id = '18bb7c10'

var_home_summary = f'stats_{home_team_id}_summary'
var_home_passing = f'stats_{home_team_id}_passing'
var_home_passing_types = f'stats_{home_team_id}_passing_types'
var_home_defense = f'stats_{home_team_id}_defense'
var_home_possession = f'stats_{home_team_id}_possession'
var_home_misc = f'stats_{home_team_id}_misc'
var_home_keeper = f'keeper_stats_{home_team_id}'

var_away_summary = f'stats_{away_team_id}_summary'
var_away_passing = f'stats_{away_team_id}_passing'
var_away_passing_types = f'stats_{away_team_id}_passing_types'
var_away_defense = f'stats_{away_team_id}_defense'
var_away_possession = f'stats_{away_team_id}_possession'
var_away_misc = f'stats_{away_team_id}_misc'
var_away_keeper = f'keeper_stats_{away_team_id}'

var_home_shots = f'shots_{home_team_id}'
var_away_shots = f'shots_{away_team_id}'

soup = BeautifulSoup(content, 'lxml')
body = soup.find('div', class_='box', id='content')

### ALL TABLES ###

table_home_summary = body.find('table', id=var_home_summary).find('tbody')
table_home_passing = body.find('table', id=var_home_passing).find('tbody')
table_home_passing_types = body.find('table', id=var_home_passing_types).find('tbody')
table_home_defense = body.find('table', id=var_home_defense).find('tbody')
table_home_possession = body.find('table', id=var_home_possession).find('tbody')
table_home_misc = body.find('table', id=var_home_misc).find('tbody')
table_home_keeper = body.find('table', id=var_home_keeper).find('tbody')

table_away_summary = body.find('table', id=var_away_summary).find('tbody')
table_away_passing = body.find('table', id=var_away_passing).find('tbody')
table_away_passing_types = body.find('table', id=var_away_passing_types).find('tbody')
table_away_defense = body.find('table', id=var_away_defense).find('tbody')
table_away_possession = body.find('table', id=var_away_possession).find('tbody')
table_away_misc = body.find('table', id=var_away_misc).find('tbody')
table_away_keeper = body.find('table', id=var_away_keeper).find('tbody')

# table_all_shots = body.find('table', id='shots_all').find('tbody')
table_home_shots = body.find('table', id=var_home_shots).find('tbody')
table_away_shots = body.find('table', id=var_away_shots).find('tbody')

# var summary
sum_match = []
sum_team_id = []
sum_opponent_id = []
sum_player = []
sum_player_link = []
sum_nationality = []
sum_position = []
sum_age = []
sum_minutes_played = []
sum_goals = []
sum_assists = []
sum_penalty_kick = []
sum_penalty_kick_att = []
sum_shots = []
sum_shots_on_target = []
sum_yellow_cards = []
sum_red_cards = []
sum_touches = []
sum_tackles = []
sum_intercepts = []
sum_blocks = []
sum_xg = []
sum_npxg = []
sum_xag = []
sum_sca = []
sum_gca = []
sum_passes_completed = []
sum_passes_att = []
sum_pass_pct = []
sum_progressive_passes = []
sum_carries = []
sum_progressive_carries = []
sum_takeon_att = []
sum_takeon_successful = []

# var passing
psg_total_cmp = []
psg_total_att = []
psg_total_pct = []
psg_total_totdist = []
psg_total_prgdist = []
psg_short_cmp = []
psg_short_att = []
psg_short_pct = []
psg_medium_cmp = []
psg_medium_att = []
psg_medium_pct = []
psg_long_cmp = []
psg_long_att = []
psg_long_pct = []
psg_ast = []
psg_xag = []
psg_xa = []
psg_kp = []
psg_1_3 = []
psg_ppa = []
psg_crspa = []
psg_prgp = []

# var passing types
pst_att = []
pst_live = []
pst_dead = []
pst_fk = []
pst_tb = []
pst_sw = []
pst_crs = []
pst_ti = []
pst_ck = []
pst_ck_in = []
pst_ck_out = []
pst_ck_str = []
pst_out_cmp = []
pst_out_off = []
pst_out_blocks = []

# var defensive
def_tac_tkl = []
def_tac_tklw = []
def_tac_def3rd = []
def_tac_mid3rd = []
def_tac_att3rd = []
def_cha_tkl = []
def_cha_att = []
def_cha_tklpct = []
def_cha_lost = []
def_blo_blocks = []
def_blo_sh = []
def_blo_pass = []
def_int = []
def_tklint = []
def_clr = []
def_err = []

# var possession
pos_tou_touches = []
pos_tou_defpen = []
pos_tou_def3rd = []
pos_tou_mid3rd = []
pos_tou_att3rd = []
pos_tou_attpen = []
pos_tou_live = []
pos_tko_att = []
pos_tko_succ = []
pos_tko_succpct = []
pos_tko_tkld = []
pos_tko_tkldpct = []
pos_car_carries = []
pos_car_totdist = []
pos_car_prgdist = []
pos_car_prgc = []
pos_car_1_3 = []
pos_car_cpa = []
pos_car_mis = []
pos_car_dis = []
pos_rcv_rec = []
pos_rcv_prgr = []

# var misc
mis_per_crdy = []
mis_per_crdr = []
mis_per_2crdy = []
mis_per_fls = []
mis_per_fld = []
mis_per_off = []
mis_per_crs = []
mis_per_int = []
mis_per_tklw = []
mis_per_pkwon = []
mis_per_pkcon = []
mis_per_og = []
mis_per_recov = []
mis_aer_won = []
mis_aer_lost = []
mis_aer_wonpct = []

# var keeper
kpr_match = []
kpr_team_id = []
kpr_opponent_id = []
kpr_player = []
kpr_player_link = []
kpr_nationality = []
kpr_age = []
kpr_minutes_played = []
kpr_ss_sota = []
kpr_ss_ga = []
kpr_ss_saves = []
kpr_ss_savepct = []
kpr_ss_psxg = []
kpr_lau_cmp = []
kpr_lau_att = []
kpr_lau_cmppct = []
kpr_pas_att = []
kpr_pas_thr = []
kpr_pas_launchpct = []
kpr_pas_avglen = []
kpr_gk_att = []
kpr_gk_launchpct = []
kpr_gk_avglen = []
kpr_crs_opp = []
kpr_crs_stp = []
kpr_crs_stppct = []
kpr_swp_opa = []
kpr_swp_avgdist = []

# var shots
sht_match = []
sht_opponent = []
sht_minute = []
sht_player = []
sht_player_link = []
sht_squad = []
sht_squad_link = []
sht_xg = []
sht_psxg = []
sht_outcome = []
sht_distance = []
sht_body_part = []
sht_notes = []
sht_sca1_player = []
sht_sca1_player_link = []
sht_sca1_event = []
sht_sca2_player = []
sht_sca2_player_link = []
sht_sca2_event = []

### HOME TEAM ###
# home team summary
for r in table_home_summary.find_all('tr'):
    sum_match.append(web)
    sum_team_id.append(home_team_id)
    sum_opponent_id.append(away_team_id)
    sum_player.append(str.strip(r.find('th').get_text()))
    sum_player_link.append(r.find('th').find('a')['href'])
    l = []
    for d in r.find_all('td'):
        l.append(d)
    sum_nationality.append(l[1].get_text())
    sum_position.append(l[2].get_text())
    sum_age.append(l[3].get_text())
    sum_minutes_played.append(l[4].get_text())
    sum_goals.append(l[5].get_text())
    sum_assists.append(l[6].get_text())
    sum_penalty_kick.append(l[7].get_text())
    sum_penalty_kick_att.append(l[8].get_text())
    sum_shots.append(l[9].get_text())
    sum_shots_on_target.append(l[10].get_text())
    sum_yellow_cards.append(l[11].get_text())
    sum_red_cards.append(l[12].get_text())
    sum_touches.append(l[13].get_text())
    sum_tackles.append(l[14].get_text())
    sum_intercepts.append(l[15].get_text())
    sum_blocks.append(l[16].get_text())
    sum_xg.append(l[17].get_text())
    sum_npxg.append(l[18].get_text())
    sum_xag.append(l[19].get_text())
    sum_sca.append(l[20].get_text())
    sum_gca.append(l[21].get_text())
    sum_passes_completed.append(l[22].get_text())
    sum_passes_att.append(l[23].get_text())
    sum_pass_pct.append(l[24].get_text())
    sum_progressive_passes.append(l[25].get_text())
    sum_carries.append(l[26].get_text())
    sum_progressive_carries.append(l[27].get_text())
    sum_takeon_att.append(l[28].get_text())
    sum_takeon_successful.append(l[29].get_text())

# home team passing
for r in table_home_passing.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    psg_total_cmp.append(l[5].get_text())
    psg_total_att.append(l[6].get_text())
    psg_total_pct.append(l[7].get_text())
    psg_total_totdist.append(l[8].get_text())
    psg_total_prgdist.append(l[9].get_text())
    psg_short_cmp.append(l[10].get_text())
    psg_short_att.append(l[11].get_text())
    psg_short_pct.append(l[12].get_text())
    psg_medium_cmp.append(l[13].get_text())
    psg_medium_att.append(l[14].get_text())
    psg_medium_pct.append(l[15].get_text())
    psg_long_cmp.append(l[16].get_text())
    psg_long_att.append(l[17].get_text())
    psg_long_pct.append(l[18].get_text())
    psg_ast.append(l[19].get_text())
    psg_xag.append(l[20].get_text())
    psg_xa.append(l[21].get_text())
    psg_kp.append(l[22].get_text())
    psg_1_3.append(l[23].get_text())
    psg_ppa.append(l[24].get_text())
    psg_crspa.append(l[25].get_text())
    psg_prgp.append(l[26].get_text())

# home team passing types
for r in table_home_passing_types.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    pst_att.append(l[5].get_text())
    pst_live.append(l[6].get_text())
    pst_dead.append(l[7].get_text())
    pst_fk.append(l[8].get_text())
    pst_tb.append(l[9].get_text())
    pst_sw.append(l[10].get_text())
    pst_crs.append(l[11].get_text())
    pst_ti.append(l[12].get_text())
    pst_ck.append(l[13].get_text())
    pst_ck_in.append(l[14].get_text())
    pst_ck_out.append(l[15].get_text())
    pst_ck_str.append(l[16].get_text())
    pst_out_cmp.append(l[17].get_text())
    pst_out_off.append(l[18].get_text())
    pst_out_blocks.append(l[19].get_text())

# home team defensive actions
for r in table_home_defense.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    def_tac_tkl.append(l[5].get_text())
    def_tac_tklw.append(l[6].get_text())
    def_tac_def3rd.append(l[7].get_text())
    def_tac_mid3rd.append(l[8].get_text())
    def_tac_att3rd.append(l[9].get_text())
    def_cha_tkl.append(l[10].get_text())
    def_cha_att.append(l[11].get_text())
    def_cha_tklpct.append(l[12].get_text())
    def_cha_lost.append(l[13].get_text())
    def_blo_blocks.append(l[14].get_text())
    def_blo_sh.append(l[15].get_text())
    def_blo_pass.append(l[16].get_text())
    def_int.append(l[17].get_text())
    def_tklint.append(l[18].get_text())
    def_clr.append(l[19].get_text())
    def_err.append(l[20].get_text())

# home team possessions
for r in table_home_possession.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    pos_tou_touches.append(l[5].get_text())
    pos_tou_defpen.append(l[6].get_text())
    pos_tou_def3rd.append(l[7].get_text())
    pos_tou_mid3rd.append(l[8].get_text())
    pos_tou_att3rd.append(l[9].get_text())
    pos_tou_attpen.append(l[10].get_text())
    pos_tou_live.append(l[11].get_text())
    pos_tko_att.append(l[12].get_text())
    pos_tko_succ.append(l[13].get_text())
    pos_tko_succpct.append(l[14].get_text())
    pos_tko_tkld.append(l[15].get_text())
    pos_tko_tkldpct.append(l[16].get_text())
    pos_car_carries.append(l[17].get_text())
    pos_car_totdist.append(l[18].get_text())
    pos_car_prgdist.append(l[19].get_text())
    pos_car_prgc.append(l[20].get_text())
    pos_car_1_3.append(l[21].get_text())
    pos_car_cpa.append(l[22].get_text())
    pos_car_mis.append(l[23].get_text())
    pos_car_dis.append(l[24].get_text())
    pos_rcv_rec.append(l[25].get_text())
    pos_rcv_prgr.append(l[26].get_text())

# home team miscellaneous
for r in table_home_misc.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    mis_per_crdy.append(l[5].get_text())
    mis_per_crdr.append(l[6].get_text())
    mis_per_2crdy.append(l[7].get_text())
    mis_per_fls.append(l[8].get_text())
    mis_per_fld.append(l[9].get_text())
    mis_per_off.append(l[10].get_text())
    mis_per_crs.append(l[11].get_text())
    mis_per_int.append(l[12].get_text())
    mis_per_tklw.append(l[13].get_text())
    mis_per_pkwon.append(l[14].get_text())
    mis_per_pkcon.append(l[15].get_text())
    mis_per_og.append(l[16].get_text())
    mis_per_recov.append(l[17].get_text())
    mis_aer_won.append(l[18].get_text())
    mis_aer_lost.append(l[19].get_text())
    mis_aer_wonpct.append(l[20].get_text())

### AWAY TEAM ###
# away team summary
for r in table_away_summary.find_all('tr'):
    sum_match.append(web)
    sum_team_id.append(away_team_id)
    sum_opponent_id.append(home_team_id)
    sum_player.append(str.strip(r.find('th').get_text()))
    sum_player_link.append(r.find('th').find('a')['href'])
    l = []
    for d in r.find_all('td'):
        l.append(d)
    sum_nationality.append(l[1].get_text())
    sum_position.append(l[2].get_text())
    sum_age.append(l[3].get_text())
    sum_minutes_played.append(l[4].get_text())
    sum_goals.append(l[5].get_text())
    sum_assists.append(l[6].get_text())
    sum_penalty_kick.append(l[7].get_text())
    sum_penalty_kick_att.append(l[8].get_text())
    sum_shots.append(l[9].get_text())
    sum_shots_on_target.append(l[10].get_text())
    sum_yellow_cards.append(l[11].get_text())
    sum_red_cards.append(l[12].get_text())
    sum_touches.append(l[13].get_text())
    sum_tackles.append(l[14].get_text())
    sum_intercepts.append(l[15].get_text())
    sum_blocks.append(l[16].get_text())
    sum_xg.append(l[17].get_text())
    sum_npxg.append(l[18].get_text())
    sum_xag.append(l[19].get_text())
    sum_sca.append(l[20].get_text())
    sum_gca.append(l[21].get_text())
    sum_passes_completed.append(l[22].get_text())
    sum_passes_att.append(l[23].get_text())
    sum_pass_pct.append(l[24].get_text())
    sum_progressive_passes.append(l[25].get_text())
    sum_carries.append(l[26].get_text())
    sum_progressive_carries.append(l[27].get_text())
    sum_takeon_att.append(l[28].get_text())
    sum_takeon_successful.append(l[29].get_text())

# away team passing
for r in table_away_passing.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    psg_total_cmp.append(l[5].get_text())
    psg_total_att.append(l[6].get_text())
    psg_total_pct.append(l[7].get_text())
    psg_total_totdist.append(l[8].get_text())
    psg_total_prgdist.append(l[9].get_text())
    psg_short_cmp.append(l[10].get_text())
    psg_short_att.append(l[11].get_text())
    psg_short_pct.append(l[12].get_text())
    psg_medium_cmp.append(l[13].get_text())
    psg_medium_att.append(l[14].get_text())
    psg_medium_pct.append(l[15].get_text())
    psg_long_cmp.append(l[16].get_text())
    psg_long_att.append(l[17].get_text())
    psg_long_pct.append(l[18].get_text())
    psg_ast.append(l[19].get_text())
    psg_xag.append(l[20].get_text())
    psg_xa.append(l[21].get_text())
    psg_kp.append(l[22].get_text())
    psg_1_3.append(l[23].get_text())
    psg_ppa.append(l[24].get_text())
    psg_crspa.append(l[25].get_text())
    psg_prgp.append(l[26].get_text())

# away team passing types
for r in table_away_passing_types.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    pst_att.append(l[5].get_text())
    pst_live.append(l[6].get_text())
    pst_dead.append(l[7].get_text())
    pst_fk.append(l[8].get_text())
    pst_tb.append(l[9].get_text())
    pst_sw.append(l[10].get_text())
    pst_crs.append(l[11].get_text())
    pst_ti.append(l[12].get_text())
    pst_ck.append(l[13].get_text())
    pst_ck_in.append(l[14].get_text())
    pst_ck_out.append(l[15].get_text())
    pst_ck_str.append(l[16].get_text())
    pst_out_cmp.append(l[17].get_text())
    pst_out_off.append(l[18].get_text())
    pst_out_blocks.append(l[19].get_text())

# away team defensive actions
for r in table_away_defense.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    def_tac_tkl.append(l[5].get_text())
    def_tac_tklw.append(l[6].get_text())
    def_tac_def3rd.append(l[7].get_text())
    def_tac_mid3rd.append(l[8].get_text())
    def_tac_att3rd.append(l[9].get_text())
    def_cha_tkl.append(l[10].get_text())
    def_cha_att.append(l[11].get_text())
    def_cha_tklpct.append(l[12].get_text())
    def_cha_lost.append(l[13].get_text())
    def_blo_blocks.append(l[14].get_text())
    def_blo_sh.append(l[15].get_text())
    def_blo_pass.append(l[16].get_text())
    def_int.append(l[17].get_text())
    def_tklint.append(l[18].get_text())
    def_clr.append(l[19].get_text())
    def_err.append(l[20].get_text())

# away team possessions
for r in table_away_possession.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    pos_tou_touches.append(l[5].get_text())
    pos_tou_defpen.append(l[6].get_text())
    pos_tou_def3rd.append(l[7].get_text())
    pos_tou_mid3rd.append(l[8].get_text())
    pos_tou_att3rd.append(l[9].get_text())
    pos_tou_attpen.append(l[10].get_text())
    pos_tou_live.append(l[11].get_text())
    pos_tko_att.append(l[12].get_text())
    pos_tko_succ.append(l[13].get_text())
    pos_tko_succpct.append(l[14].get_text())
    pos_tko_tkld.append(l[15].get_text())
    pos_tko_tkldpct.append(l[16].get_text())
    pos_car_carries.append(l[17].get_text())
    pos_car_totdist.append(l[18].get_text())
    pos_car_prgdist.append(l[19].get_text())
    pos_car_prgc.append(l[20].get_text())
    pos_car_1_3.append(l[21].get_text())
    pos_car_cpa.append(l[22].get_text())
    pos_car_mis.append(l[23].get_text())
    pos_car_dis.append(l[24].get_text())
    pos_rcv_rec.append(l[25].get_text())
    pos_rcv_prgr.append(l[26].get_text())

# away team miscellaneous
for r in table_away_misc.find_all('tr'):
    l = []
    for d in r.find_all('td'):
        l.append(d)
    mis_per_crdy.append(l[5].get_text())
    mis_per_crdr.append(l[6].get_text())
    mis_per_2crdy.append(l[7].get_text())
    mis_per_fls.append(l[8].get_text())
    mis_per_fld.append(l[9].get_text())
    mis_per_off.append(l[10].get_text())
    mis_per_crs.append(l[11].get_text())
    mis_per_int.append(l[12].get_text())
    mis_per_tklw.append(l[13].get_text())
    mis_per_pkwon.append(l[14].get_text())
    mis_per_pkcon.append(l[15].get_text())
    mis_per_og.append(l[16].get_text())
    mis_per_recov.append(l[17].get_text())
    mis_aer_won.append(l[18].get_text())
    mis_aer_lost.append(l[19].get_text())
    mis_aer_wonpct.append(l[20].get_text())

### KEEPER STATS ###
# home keeper stats
for r in table_home_keeper.find_all('tr'):
    kpr_match.append(web)
    kpr_team_id.append(home_team_id)
    kpr_opponent_id.append(away_team_id)
    kpr_player.append(str.strip(r.find('th').get_text()))
    kpr_player_link.append(r.find('th').find('a')['href'])
    l = []
    for d in r.find_all('td'):
        l.append(d)
    kpr_nationality.append(l[0].get_text())
    kpr_age.append(l[1].get_text())
    kpr_minutes_played.append(l[2].get_text())
    kpr_ss_sota.append(l[3].get_text())
    kpr_ss_ga.append(l[4].get_text())
    kpr_ss_saves.append(l[5].get_text())
    kpr_ss_savepct.append(l[6].get_text())
    kpr_ss_psxg.append(l[7].get_text())
    kpr_lau_cmp.append(l[8].get_text())
    kpr_lau_att.append(l[9].get_text())
    kpr_lau_cmppct.append(l[10].get_text())
    kpr_pas_att.append(l[11].get_text())
    kpr_pas_thr.append(l[12].get_text())
    kpr_pas_launchpct.append(l[13].get_text())
    kpr_pas_avglen.append(l[14].get_text())
    kpr_gk_att.append(l[15].get_text())
    kpr_gk_launchpct.append(l[16].get_text())
    kpr_gk_avglen.append(l[17].get_text())
    kpr_crs_opp.append(l[18].get_text())
    kpr_crs_stp.append(l[19].get_text())
    kpr_crs_stppct.append(l[20].get_text())
    kpr_swp_opa.append(l[21].get_text())
    kpr_swp_avgdist.append(l[22].get_text())

# away keeper stats
for r in table_away_keeper.find_all('tr'):
    kpr_match.append(web)
    kpr_team_id.append(away_team_id)
    kpr_opponent_id.append(home_team_id)
    kpr_player.append(str.strip(r.find('th').get_text()))
    kpr_player_link.append(r.find('th').find('a')['href'])
    l = []
    for d in r.find_all('td'):
        l.append(d)
    kpr_nationality.append(l[0].get_text())
    kpr_age.append(l[1].get_text())
    kpr_minutes_played.append(l[2].get_text())
    kpr_ss_sota.append(l[3].get_text())
    kpr_ss_ga.append(l[4].get_text())
    kpr_ss_saves.append(l[5].get_text())
    kpr_ss_savepct.append(l[6].get_text())
    kpr_ss_psxg.append(l[7].get_text())
    kpr_lau_cmp.append(l[8].get_text())
    kpr_lau_att.append(l[9].get_text())
    kpr_lau_cmppct.append(l[10].get_text())
    kpr_pas_att.append(l[11].get_text())
    kpr_pas_thr.append(l[12].get_text())
    kpr_pas_launchpct.append(l[13].get_text())
    kpr_pas_avglen.append(l[14].get_text())
    kpr_gk_att.append(l[15].get_text())
    kpr_gk_launchpct.append(l[16].get_text())
    kpr_gk_avglen.append(l[17].get_text())
    kpr_crs_opp.append(l[18].get_text())
    kpr_crs_stp.append(l[19].get_text())
    kpr_crs_stppct.append(l[20].get_text())
    kpr_swp_opa.append(l[21].get_text())
    kpr_swp_avgdist.append(l[22].get_text())

### SHOTS STATS ###
# home shots stats
for r in table_home_shots.find_all('tr'):
    if 'spacer' in r['class']:
        continue
    l = []
    for d in r.find_all('td'):
        l.append(d)
    sht_match.append(web)
    sht_opponent.append(away_team_id)
    sht_minute.append(r.find('th').get_text())
    sht_player.append(str.strip(l[0].get_text()))
    sht_player_link.append(l[0].find('a')['href'])
    sht_squad.append(str.strip(l[1].get_text()))
    sht_squad_link.append(l[1].find('a')['href'])
    sht_xg.append(l[2].get_text())
    sht_psxg.append(l[3].get_text())
    sht_outcome.append(l[4].get_text())
    sht_distance.append(l[5].get_text())
    sht_body_part.append(l[6].get_text())
    sht_notes.append(l[7].get_text())
    if l[8].get_text() != '':
        sht_sca1_player.append(l[8].get_text())
        sht_sca1_player_link.append(l[8].find('a')['href'])
    else:
        sht_sca1_player.append('')
        sht_sca1_player_link.append('')
    sht_sca1_event.append(l[9].get_text())
    if l[10].get_text() != '':
        sht_sca2_player.append(l[10].get_text())
        sht_sca2_player_link.append(l[10].find('a')['href'])
    else:
        sht_sca2_player.append('')
        sht_sca2_player_link.append('')
    sht_sca2_event.append(l[11].get_text())

# away shots stats
for r in table_away_shots.find_all('tr'):
    if 'spacer' in r['class']:
        continue
    l = []
    for d in r.find_all('td'):
        l.append(d)
    sht_match.append(web)
    sht_opponent.append(home_team_id)
    sht_minute.append(r.find('th').get_text())
    sht_player.append(str.strip(l[0].get_text()))
    sht_player_link.append(l[0].find('a')['href'])
    sht_squad.append(str.strip(l[1].get_text()))
    sht_squad_link.append(l[1].find('a')['href'])
    sht_xg.append(l[2].get_text())
    sht_psxg.append(l[3].get_text())
    sht_outcome.append(l[4].get_text())
    sht_distance.append(l[5].get_text())
    sht_body_part.append(l[6].get_text())
    sht_notes.append(l[7].get_text())
    if l[8].get_text() != '':
        sht_sca1_player.append(l[8].get_text())
        sht_sca1_player_link.append(l[8].find('a')['href'])
    else:
        sht_sca1_player.append('')
        sht_sca1_player_link.append('')
    sht_sca1_event.append(l[9].get_text())
    if l[10].get_text() != '':
        sht_sca2_player.append(l[10].get_text())
        sht_sca2_player_link.append(l[10].find('a')['href'])
    else:
        sht_sca2_player.append('')
        sht_sca2_player_link.append('')
    sht_sca2_event.append(l[11].get_text())

### PANDAS DATAFRAME ###
# df stats
df_stats = pd.DataFrame.from_dict({
    'sum_match':sum_match,
    'sum_team_id':sum_team_id,
    'sum_opponent_id':sum_opponent_id,
    'sum_player':sum_player,
    'sum_player_link':sum_player_link,
    'sum_nationality':sum_nationality,
    'sum_position':sum_position,
    'sum_age':sum_age,
    'sum_minutes_played':sum_minutes_played,
    'sum_goals':sum_goals,
    'sum_assists':sum_assists,
    'sum_penalty_kick':sum_penalty_kick,
    'sum_penalty_kick_att':sum_penalty_kick_att,
    'sum_shots':sum_shots,
    'sum_shots_on_target':sum_shots_on_target,
    'sum_yellow_cards':sum_yellow_cards,
    'sum_red_cards':sum_red_cards,
    'sum_touches':sum_touches,
    'sum_tackles':sum_tackles,
    'sum_intercepts':sum_intercepts,
    'sum_blocks':sum_blocks,
    'sum_xg':sum_xg,
    'sum_npxg':sum_npxg,
    'sum_xag':sum_xag,
    'sum_sca':sum_sca,
    'sum_gca':sum_gca,
    'sum_passes_completed':sum_passes_completed,
    'sum_passes_att':sum_passes_att,
    'sum_pass_pct':sum_pass_pct,
    'sum_progressive_passes':sum_progressive_passes,
    'sum_carries':sum_carries,
    'sum_progressive_carries':sum_progressive_carries,
    'sum_takeon_att':sum_takeon_att,
    'sum_takeon_successful':sum_takeon_successful,
    'psg_total_cmp':psg_total_cmp,
    'psg_total_att':psg_total_att,
    'psg_total_pct':psg_total_pct,
    'psg_total_totdist':psg_total_totdist,
    'psg_total_prgdist':psg_total_prgdist,
    'psg_short_cmp':psg_short_cmp,
    'psg_short_att':psg_short_att,
    'psg_short_pct':psg_short_pct,
    'psg_medium_cmp':psg_medium_cmp,
    'psg_medium_att':psg_medium_att,
    'psg_medium_pct':psg_medium_pct,
    'psg_long_cmp':psg_long_cmp,
    'psg_long_att':psg_long_att,
    'psg_long_pct':psg_long_pct,
    'psg_ast':psg_ast,
    'psg_xag':psg_xag,
    'psg_xa':psg_xa,
    'psg_kp':psg_kp,
    'psg_1_3':psg_1_3,
    'psg_ppa':psg_ppa,
    'psg_crspa':psg_crspa,
    'psg_prgp':psg_prgp,
    'pst_att':pst_att,
    'pst_live':pst_live,
    'pst_dead':pst_dead,
    'pst_fk':pst_fk,
    'pst_tb':pst_tb,
    'pst_sw':pst_sw,
    'pst_crs':pst_crs,
    'pst_ti':pst_ti,
    'pst_ck':pst_ck,
    'pst_ck_in':pst_ck_in,
    'pst_ck_out':pst_ck_out,
    'pst_ck_str':pst_ck_str,
    'pst_out_cmp':pst_out_cmp,
    'pst_out_off':pst_out_off,
    'pst_out_blocks':pst_out_blocks,
    'def_tac_tkl':def_tac_tkl,
    'def_tac_tklw':def_tac_tklw,
    'def_tac_def3rd':def_tac_def3rd,
    'def_tac_mid3rd':def_tac_mid3rd,
    'def_tac_att3rd':def_tac_att3rd,
    'def_cha_tkl':def_cha_tkl,
    'def_cha_att':def_cha_att,
    'def_cha_tklpct':def_cha_tklpct,
    'def_cha_lost':def_cha_lost,
    'def_blo_blocks':def_blo_blocks,
    'def_blo_sh':def_blo_sh,
    'def_blo_pass':def_blo_pass,
    'def_int':def_int,
    'def_tklint':def_tklint,
    'def_clr':def_clr,
    'def_err':def_err,
    'pos_tou_touches':pos_tou_touches,
    'pos_tou_defpen':pos_tou_defpen,
    'pos_tou_def3rd':pos_tou_def3rd,
    'pos_tou_mid3rd':pos_tou_mid3rd,
    'pos_tou_att3rd':pos_tou_att3rd,
    'pos_tou_attpen':pos_tou_attpen,
    'pos_tou_live':pos_tou_live,
    'pos_tko_att':pos_tko_att,
    'pos_tko_succ':pos_tko_succ,
    'pos_tko_succpct':pos_tko_succpct,
    'pos_tko_tkld':pos_tko_tkld,
    'pos_tko_tkldpct':pos_tko_tkldpct,
    'pos_car_carries':pos_car_carries,
    'pos_car_totdist':pos_car_totdist,
    'pos_car_prgdist':pos_car_prgdist,
    'pos_car_prgc':pos_car_prgc,
    'pos_car_1_3':pos_car_1_3,
    'pos_car_cpa':pos_car_cpa,
    'pos_car_mis':pos_car_mis,
    'pos_car_dis':pos_car_dis,
    'pos_rcv_rec':pos_rcv_rec,
    'pos_rcv_prgr':pos_rcv_prgr,
    'mis_per_crdy':mis_per_crdy,
    'mis_per_crdr':mis_per_crdr,
    'mis_per_2crdy':mis_per_2crdy,
    'mis_per_fls':mis_per_fls,
    'mis_per_fld':mis_per_fld,
    'mis_per_off':mis_per_off,
    'mis_per_crs':mis_per_crs,
    'mis_per_int':mis_per_int,
    'mis_per_tklw':mis_per_tklw,
    'mis_per_pkwon':mis_per_pkwon,
    'mis_per_pkcon':mis_per_pkcon,
    'mis_per_og':mis_per_og,
    'mis_per_recov':mis_per_recov,
    'mis_aer_won':mis_aer_won,
    'mis_aer_lost':mis_aer_lost,
    'mis_aer_wonpct':mis_aer_wonpct,
})

# df_keeper
df_keeper = pd.DataFrame.from_dict({
    'kpr_match':kpr_match,
    'kpr_team_id':kpr_team_id,
    'kpr_opponent_id':kpr_opponent_id,
    'kpr_player':kpr_player,
    'kpr_player_link':kpr_player_link,
    'kpr_nationality':kpr_nationality,
    'kpr_age':kpr_age,
    'kpr_minutes_played':kpr_minutes_played,
    'kpr_ss_sota':kpr_ss_sota,
    'kpr_ss_ga':kpr_ss_ga,
    'kpr_ss_saves':kpr_ss_saves,
    'kpr_ss_savepct':kpr_ss_savepct,
    'kpr_ss_psxg':kpr_ss_psxg,
    'kpr_lau_cmp':kpr_lau_cmp,
    'kpr_lau_att':kpr_lau_att,
    'kpr_lau_cmppct':kpr_lau_cmppct,
    'kpr_pas_att':kpr_pas_att,
    'kpr_pas_thr':kpr_pas_thr,
    'kpr_pas_launchpct':kpr_pas_launchpct,
    'kpr_pas_avglen':kpr_pas_avglen,
    'kpr_gk_att':kpr_gk_att,
    'kpr_gk_launchpct':kpr_gk_launchpct,
    'kpr_gk_avglen':kpr_gk_avglen,
    'kpr_crs_opp':kpr_crs_opp,
    'kpr_crs_stp':kpr_crs_stp,
    'kpr_crs_stppct':kpr_crs_stppct,
    'kpr_swp_opa':kpr_swp_opa,
    'kpr_swp_avgdist':kpr_swp_avgdist,
})

# df shots
df_shots = pd.DataFrame.from_dict({
    'sht_match':sht_match,
    'sht_opponent':sht_opponent,
    'sht_minute':sht_minute,
    'sht_player':sht_player,
    'sht_player_link':sht_player_link,
    'sht_squad':sht_squad,
    'sht_squad_link':sht_squad_link,
    'sht_xg':sht_xg,
    'sht_psxg':sht_psxg,
    'sht_outcome':sht_outcome,
    'sht_distance':sht_distance,
    'sht_body_part':sht_body_part,
    'sht_notes':sht_notes,
    'sht_sca1_player':sht_sca1_player,
    'sht_sca1_player_link':sht_sca1_player_link,
    'sht_sca1_event':sht_sca1_event,
    'sht_sca2_player':sht_sca2_player,
    'sht_sca2_player_link':sht_sca2_player_link,
    'sht_sca2_event':sht_sca2_event,
})

# save to csv
df_stats.to_csv('web_scraping_practice\\FBref\\player_stats_england.csv', index=False, encoding='utf-8', sep=';')
df_keeper.to_csv('web_scraping_practice\\FBref\\keeper_stats_england.csv', index=False, encoding='utf-8', sep=';')
df_shots.to_csv('web_scraping_practice\\FBref\\shots_stats_england.csv', index=False, encoding='utf-8', sep=';')