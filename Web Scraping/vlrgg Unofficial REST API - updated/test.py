import sys
sys.path.insert(1, '/Users/fnurr/Documents/WORKPLACE/vlrgg Unofficial REST API - updated/api/')
from scrape import Vlr
vlr = Vlr()

import pandas as pd
import json

vlr.vlr_matchpage(subURL = '60968/thunderbolts-gaming-vs-eternal-fire-open-fire-legacy-playoffs-qf')


