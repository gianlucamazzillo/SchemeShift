import nflreadpy as nfl
import pandas as pd

SEASON = 2025
TEAM = 'BAL'


def analyze_team_by_down(pbp: pd.DataFrame, team: str,) -> pd.DataFrame:
    team_plays = pbp[
        (pbp["posteam"] == team)
        & (pbp["play_type"].isin(["run", "pass"]))
        & (pbp["down"].isin([1, 2, 3, 4]))
    ].copy()

    team_plays['converted'] = (
        team_plays['first_down'].fillna(0).eq(1)
        |   team_plays['touchdown'].fillna(0).eq(1)
    )
#criação do filtro de conversão ou não das jogadas

    summary = (
        team_plays
        .groupby(['down', 'play_type'], as_index = False)
        .agg(
            number_of_plays = ('play_type', 'size'),
            conversions = ('converted', 'sum'),
            conversion_rate = ('converted', 'mean'),
            average_ydstogo = ('ydstogo', 'mean'),
            average_yards=('yards_gained', 'mean')
        )
    )

    summary['conversion_rate'] = (summary['conversion_rate'] * 100).round(1)
    summary['conversions'] = summary['conversions'].astype(int)

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
    summary["average_ydstogo"] = summary["average_ydstogo"].round(2)

    return summary[
        [
            'down',
            'play_type',
            'number_of_plays',
            'conversion_rate',
            'conversions',
            'play_percentage',
            'average_yards',
            'average_ydstogo',
        ]
    ].sort_values(['down', 'play_type'])

print(f'Carregando a temporada {SEASON}...')

pbp = nfl.load_pbp(SEASON).to_pandas()

result = analyze_team_by_down(pbp, TEAM)

print(f'\nAtaque de {TEAM} por descida: ')
print(result.to_string(index=False))



def analyze_late_downs_by_distance (pbp: pd.DataFrame, team: str) -> pd.DataFrame:
    late_down_plays = pbp[
        (pbp['posteam'] == team)
        & (pbp['play_type'].isin(['run', 'pass']))
        & (pbp['down'].isin([3, 4]))
        & (pbp['ydstogo'] > 0)
    ].copy()

    late_down_plays['converted'] = (
        late_down_plays['first_down'].fillna(0).eq(1)
        |   late_down_plays['touchdown'].fillna(0).eq(1)
    )

    late_down_plays['distance_group'] = pd.cut(
        late_down_plays['ydstogo'],
        bins = [0, 3, 6, float('inf')],
        labels = ['short', 'medium', 'long'],
        include_lowest=True,
        )

    summary = (
        late_down_plays
        .groupby(
            ['down', 'distance_group', 'play_type'],
            observed = True,
            as_index=False,
        )
        .agg(
            number_of_plays = ('play_type', 'size'),
            conversions = ('converted', 'sum'),
            conversion_rate = ('converted', 'mean'),
            average_ydstogo = ('ydstogo', 'mean'),
            average_yards=('yards_gained', 'mean')
            )
    )

    summary ['plays_in_situation'] = (
        summary
        .groupby(
            ['down', 'distance_group'],
            observed = True
        )['number_of_plays']
        .transform('sum')
        )

    summary ['play_percentage'] = (
        summary['number_of_plays']
        / summary['plays_in_situation'] 
        *100
    )

    summary ['conversion_rate'] = (
        summary['conversion_rate'] * 100
    ).round(1)

    summary ['play_percentage'] = (
        summary['play_percentage'].round(1)
    )
    
    summary ['average_ydstogo'] = (
        summary['average_ydstogo'].round(2)
    )

    summary ['average_yards'] = (
        summary['average_yards'].round(2)
    )

    summary ['conversions'] = (
        summary['conversions'].astype(int)
    )

    summary['down'] = summary['down'].astype(int)

    return (
        summary[
            [
            "down",
            "distance_group",
            "play_type",
            "number_of_plays",
            "conversions",
            "conversion_rate",
            "play_percentage",
            "average_yards",
            "average_ydstogo",     
            ]
        ]
        .sort_values(
            ['down', 'distance_group', 'play_type']
        )
    )

distance_result = analyze_late_downs_by_distance(
    pbp,
    TEAM,
)

print(
    f"\nTerceiras e quartas descidas de "
    f"{TEAM} por distância:"
)

print(distance_result.to_string(index=False))

    
