import pandas as pd

def analyze_late_downs_by_distance (pbp: pd.DataFrame, team: str) -> pd.DataFrame:
    '''Summarize third and fourth down performance by distance group.'''
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



