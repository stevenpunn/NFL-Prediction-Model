import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# map team names to abbreviations
team_abbreviations = {
    'Arizona Cardinals': 'ARI',
    'Atlanta Falcons': 'ATL',
    'Baltimore Ravens': 'BAL',
    'Buffalo Bills': 'BUF',
    'Carolina Panthers': 'CAR',
    'Chicago Bears': 'CHI',
    'Cincinnati Bengals': 'CIN',
    'Cleveland Browns': 'CLE',
    'Dallas Cowboys': 'DAL',
    'Denver Broncos': 'DEN',
    'Detroit Lions': 'DET',
    'Green Bay Packers': 'GB',
    'Houston Texans': 'HOU',
    'Indianapolis Colts': 'IND',
    'Jacksonville Jaguars': 'JAX',
    'Kansas City Chiefs': 'KC',
    'Las Vegas Raiders': 'LV',
    'Los Angeles Chargers': 'LAC',
    'Los Angeles Rams': 'LA',
    'Miami Dolphins': 'MIA',
    'Minnesota Vikings': 'MIN',
    'New England Patriots': 'NE',
    'New Orleans Saints': 'NO',
    'New York Giants': 'NYG',
    'New York Jets': 'NYJ',
    'Philadelphia Eagles': 'PHI',
    'Pittsburgh Steelers': 'PIT',
    'San Francisco 49ers': 'SF',
    'Seattle Seahawks': 'SEA',
    'Tampa Bay Buccaneers': 'TB',
    'Tennessee Titans': 'TEN',
    'Washington Commanders': 'WAS'
}

# clean the data
pbp2024 = pd.read_csv('/content/NFL_pbp_24.csv')
boxscores2024 = pd.read_csv('/content/boxScores2024.csv')

# change 'GameDate' format in play by play file to match 'Date' format in box scores
pbp2024['GameDate'] = pd.to_datetime(pbp2024['GameDate']).dt.strftime('%m/%d/%y')

# find abbreviated names for teams from box scores
homeTeam_unique = boxscores2024['Home'].unique()
visitorTeam_unique = boxscores2024['Visitor'].unique()

# find abbreviated names for teams in the play-by-play data
pbpName_unique = set(pbp2024['OffenseTeam'].dropna().unique()).union(set(pbp2024['DefenseTeam'].dropna().unique()))

# replace team names with abbreivations
pbp2024['OffenseTeam'] = pbp2024['OffenseTeam'].map(team_abbreviations)
pbp2024['DefenseTeam'] = pbp2024['DefenseTeam'].map(team_abbreviations)