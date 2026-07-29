import nflreadpy as nfl
import pandas as pd

SEASON = 2025
TEAM = 'BAL'


def analyze_team_by_down(
    pbp: pd.DataFrame,
    team: str,
) -> pd.DataFrame:
    team_plays = pbp[
        (pbp["posteam"] == team)
        & (pbp["play_type"].isin(["run", "pass"]))
        & (pbp["down"].isin([1, 2, 3, 4]))
    ].copy()

    summary = (
        team_plays
        .groupby(['down', 'play_type'], as_index = False)
        .agg(
            number_of_plays = ('play_type', 'size'),
            average_yards=('yards_gained', 'mean')
        )
    )

    summary['plays_on_down'] = (
        summary
        .groupby('down')['number_of_plays']
        .transform('sum')
    )

    summary['play_percentage'] = (
        summary['number_of_plays']
        / summary['plays_on_down']
        *100
    )

    summary["average_yards"] = summary["average_yards"].round(2)
    summary["play_percentage"] = summary["play_percentage"].round(1)

    return summary[
        [
            'down',
            'play_type',
            'number_of_plays',
            'play_percentage',
            'average_yards'
        ]
    ].sort_values(['down', 'play_type'])

print(f'Carregando a temporada {SEASON}...')

pbp = nfl.load_pbp(SEASON).to_pandas()

result = analyze_team_by_down(pbp, TEAM)

print(f'\nAtaque de {TEAM} por decida: ')
print(result.to_string(index=False))
