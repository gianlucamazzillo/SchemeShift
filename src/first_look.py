import nflreadpy as nfl
import pandas as pd

SEASON = 2025

print(f'Carregando dados da temporada {SEASON}...')

pbp_polars = nfl.load_pbp(SEASON)
pbp = pbp_polars.to_pandas()

columns_to_show = [
    'game_id',
    'week',
    'posteam', #time com a posse
    'defteam', #time defendendo
    'play_type',
    'yards_gained',
]

print('\nPrimeiras linhas:')
print(pbp[columns_to_show].head(10))

TEAM = 'BAL'

team_plays = pbp[
    (pbp['posteam'] == TEAM)
    & (pbp['play_type'].isin(['run', 'pass']))
].copy()

print(f'\nJogadas ofensivas de {TEAM}')
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

summary['avarage_yards'] = summary['average_yards'].round(2)
summary['play_percentage'] = summary['play_percentage'].round(1)

print(f'\nResumo ofensivo do {TEAM}:')
print(summary)
