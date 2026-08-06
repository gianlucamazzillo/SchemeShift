import nflreadpy as nfl
import pandas as pd

SEASON = 2025
TEAM = 'PHI'

def format_run_gap(row: pd.Series) -> str:
    '''Função que define os gaps na OL'''
    gap_map = {
        'guard': 'A gap',
        'tackle': 'B gap',
        'end': 'outside',
    }

    original_gap = row['run_gap']
    run_location = row['run_location']

    if pd.isna(original_gap):
        if run_location == 'middle':
            return 'inside - gap unknown'

        return 'unclassified'

    gap = gap_map.get(original_gap, 'unclassified')

    if run_location in ['left', 'right']:
        return f'{run_location} {gap}'

    return gap


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
            "play_percentage",
            'conversion_rate',
            'conversions',
            'average_yards',
            'average_ydstogo',
        ]
    ].sort_values(['down', 'play_type'])

print(f'Loading {SEASON} season...')

pbp = nfl.load_pbp(SEASON).to_pandas()

player_stats = nfl.load_player_stats(SEASON).to_pandas()

player_positions = (
    player_stats[
        [
            'player_id',
            'position',
        ]
    ]
).dropna(subset = ['player_id']).drop_duplicates(subset = ['player_id']).rename(columns = {'player_id': 'rusher_player_id', 'position': 'rusher_position'})

result = analyze_team_by_down(pbp, TEAM)

print(f'\n{TEAM} offense by down: ')
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
            "play_percentage",
            "conversions",
            "conversion_rate",
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
    f"\nThird and fourth downs for "
    f"{TEAM} by distance:"
)

print(distance_result.to_string(index=False))

third_down_runs = pbp[
    (pbp['posteam'] == TEAM)
    & (pbp['play_type'] == "run")
    & (pbp['down'] == 3)
    & (pbp['ydstogo'] >= 4)
].copy()

fourth_down_runs = pbp[
    (pbp['posteam'] == TEAM)
    & (pbp['play_type'] == "run")
    & (pbp['down'] == 4)
    & (pbp['ydstogo'] >= 1)
].copy()

third_down_runs['distance_group'] = pd.cut(
    third_down_runs['ydstogo'],
    bins = [3, 6, float('inf')],
    labels = ['medium', 'long'],
)

fourth_down_runs["distance_group"] = pd.cut(
    fourth_down_runs["ydstogo"],
    bins=[0, 3, 6, float("inf")],
    labels=["short", "medium", "long"],
    include_lowest=True,
)

third_down_runs['converted'] = (
    third_down_runs['first_down'].fillna(0).eq(1)
    |   third_down_runs['touchdown'].fillna(0).eq(1)
)

fourth_down_runs['converted'] = (
    fourth_down_runs['first_down'].fillna(0).eq(1)
    |   fourth_down_runs['touchdown'].fillna(0).eq(1)
)

third_down_runs = third_down_runs.merge(
    player_positions,
    on="rusher_player_id",
    how="left",
)

fourth_down_runs = fourth_down_runs.merge(
    player_positions,
    on="rusher_player_id",
    how="left",
)

third_down_runs['run_gap'] = third_down_runs.apply(
    format_run_gap,
    axis = 1,
)

fourth_down_runs['run_gap'] = fourth_down_runs.apply(
    format_run_gap,
    axis = 1,
)

compact_columns =[
    "week",
    "defteam",
    "distance_group",
    "ydstogo",
    "yards_gained",
    "converted",
    "rusher_player_name",
    "rusher_position",
    "qb_scramble",
    "run_gap",
]

sorted_third_down_runs = third_down_runs.sort_values(
    ["distance_group", "ydstogo", "yards_gained"],
    ascending=[True, True, False],
)

sorted_fourth_down_runs = fourth_down_runs.sort_values(
    ["distance_group", "ydstogo", "yards_gained"],
    ascending=[True, True, False],
)

print(
    f"\nCorridas de {TEAM} em terceiras médias e longas:"
)

print(
    sorted_third_down_runs[compact_columns].to_string(index=False)
)

print(
    f"\n{TEAM} fourth-down runs by distance:"
)

print(
    sorted_fourth_down_runs[compact_columns].to_string(index=False)
)
    
