import pandas as pd

def format_run_gap(row: pd.Series) -> str:
    '''Convert nflverse run-gap data into an OL gap label'''
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

def prepare_rushing_plays(
        rushing_plays: pd.DataFrame,
        player_positions: pd.DataFrame,
) -> pd.DataFrame:
    '''Add conversion, player position, and run gap information'''

    rushing_plays = rushing_plays.copy()

    rushing_plays['converted'] = (
        rushing_plays['first_down'].fillna(0).eq(1)
        |   rushing_plays['touchdown'].fillna(0).eq(1)
    )

    rushing_plays = rushing_plays.merge(
        player_positions,
        on='rusher_player_id',
        how = 'left',
    )

    rushing_plays['formatted_run_gap'] = rushing_plays.apply(
        format_run_gap,
        axis=1,
    )

    rushing_plays['run_type'] = rushing_plays.apply(
        classify_run_type,
        axis = 1
    )

    return rushing_plays

def analyze_third_down_runs(
        pbp: pd.DataFrame,
        team: str,
        player_positions: pd.DataFrame,
) -> pd.DataFrame:
    '''Inspect medium and long distance third down rushing plays'''

#Inspect individual rushing plays in late-down situations
    third_down_runs = pbp[
        (pbp['posteam'] == team)
        & (pbp['play_type'] == "run")
        & (pbp['down'] == 3)
        & (pbp['ydstogo'] >= 4)
    ].copy()

    third_down_runs['distance_group'] = pd.cut(
    third_down_runs['ydstogo'],
    bins = [3, 6, float('inf')],
    labels = ['medium', 'long'],
)

    third_down_runs = prepare_rushing_plays(third_down_runs, player_positions,)
    return third_down_runs.sort_values(
        ['distance_group', 'ydstogo', 'yards_gained'],
        ascending=[True, True, False],
    )

def analyze_fourth_down_runs(
        pbp: pd.DataFrame,
        team: str,
        player_positions: pd.DataFrame,
) -> pd.DataFrame:
    '''Inspect fourth-down rushing plays by distance group.'''

    fourth_down_runs = pbp[
        (pbp['posteam'] == team)
        & (pbp['play_type'] == "run")
        & (pbp['down'] == 4)
        & (pbp['ydstogo'] >= 1)
    ].copy()

    fourth_down_runs["distance_group"] = pd.cut(
        fourth_down_runs["ydstogo"],
        bins=[0, 3, 6, float("inf")],
        labels=["short", "medium", "long"],
        include_lowest=True,
    )

    fourth_down_runs = prepare_rushing_plays(fourth_down_runs, player_positions,)
    return fourth_down_runs.sort_values(
        ['distance_group', 'ydstogo', 'yards_gained'],
        ascending=[True, True, False],
    )

def classify_run_type (row: pd.Series) -> str:
    '''Classify a rushing play by a runner and scramble status'''

    if row['qb_scramble'] == 1:
        return 'qb_scramble' #nflverse already has qb_scramble classified

    if pd.isna(row['rusher_position']):
        return 'unclassified' 
    #if merge has not found any player position, it shall not classify
    #as non_qb_run by exclusion

    if (
        row['rusher_position'] == 'QB'
        and row['ydstogo'] == 1
    ):
        return 'qb_short_yardege_run'
    #QB + designed run + 1yrdtogo

    if row ['rusher_position'] == 'QB':
        return 'qb_designed_run'
    #designed run by the QB

    return 'non_qb_run'
    

