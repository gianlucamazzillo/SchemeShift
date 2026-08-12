'''The purpose of this file is to provide a simple look at the NFL data available through the nflreadpy package.'''

import nflreadpy as nfl
import pandas as pd

SEASON = 2025
TEAM = 'BAL'

print(f'Loading play-by-play data for the {SEASON} season...')

#Convert it to pandas for easier manipulation and analysis.
pbp_polars = nfl.load_pbp(SEASON)
pbp = pbp_polars.to_pandas()

columns_to_show = [
    'game_id',
    'week',
    'posteam', #team with the possession
    'defteam', #defending team
    'play_type',
    'yards_gained',
]

print('\nFirst rows:')
print(pbp[columns_to_show].head(10))

team_plays = pbp[
    (pbp['posteam'] == TEAM)
    & (pbp['play_type'].isin(['run', 'pass']))
].copy()

print(f'\nOffensive plays for {TEAM}')
print(
    team_plays[
        [
            "game_id",
            "week",
            "down",
            "ydstogo",
            "play_type",
            "yards_gained",
        ]
    ].head(20)
)

#Summarize offensive production by play type
summary = (
    team_plays
    .groupby('play_type')
    .agg(
        number_of_plays=('play_type', 'size'),
        total_yards=('yards_gained', 'sum'),
        average_yards=('yards_gained', 'mean'),
    )
    .reset_index()
)

summary['play_percentage'] = (
    summary['number_of_plays']
    / summary['number_of_plays'].sum()
    *100
)

summary['average_yards'] = summary['average_yards'].round(2)
summary['play_percentage'] = summary['play_percentage'].round(1)

print(f'\nOffensive summary for {TEAM}:')
print(summary)
