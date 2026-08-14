import pandas as pd

def analyze_ydstogo_distribution(pbp: pd.DataFrame, team: str) -> pd.DataFrame:
    '''Summarize yards to go distribution by down and play type'''

    team_plays = pbp[
        (pbp['posteam'] == team)
        & (pbp['play_type'].isin(['run', 'pass']))
        & (pbp['down'].isin([1, 2, 3, 4]))
        & (pbp['ydstogo']>0)
    ].copy()

    distribution = (
        team_plays.groupby(['down', 'play_type', 'ydstogo'], as_index=False,
                           ).agg(
                               number_of_plays = ('ydstogo', 'size')
                           )
    )

    distribution ['plays_in_group'] = (
        distribution.groupby(
            ['down', 'play_type']
        )['number_of_plays'].transform('sum')
    )
    distribution['play_percentage'] = (
        distribution['number_of_plays'] / distribution['plays_in_group']*100
    ).round(1)

    distribution['down'] = (
        distribution['down'].astype(int)
    )

    return (
        distribution[
            [
                'down',
                'play_type',
                'ydstogo',
                'number_of_plays',
                'play_percentage',
            ]
        ].sort_values(['down', 'play_type', 'ydstogo'])
    )

def analyze_ydstogo_summary( pbp: pd.DataFrame, team: str,) -> pd.DataFrame:
    '''Summarize the typical yards to go situation by down and play type'''

    team_plays = pbp[
        (pbp['posteam'] == team)
        & (pbp['play_type'].isin(['run', 'pass']))
        & (pbp['down'].isin([1, 2, 3, 4]))
        & (pbp['ydstogo']>0)
    ].copy()

    summary = (
        team_plays.groupby(
            ['down', 'play_type'],
        as_index=False
        ).agg(
            median_ydstogo = ('ydstogo', 'median'),
            most_common_ydstogo=(
                'ydstogo',
                lambda x: x.mode().iloc[0],
            ),
            occurrences =(
                'ydstogo',
                lambda x: x.value_counts().iloc[0],
            ),
            number_of_plays = ('ydstogo', 'size'),
            )
        )

    summary['percentage'] = (
        summary['occurrences']/ summary['number_of_plays'] * 100
    ).round(1)
    summary['median_ydstogo'] = (
        summary['median_ydstogo'].round(2)
    )
    summary['down'] = (
        summary['down'].astype(int)
    )
    summary['most_common_ydstogo'] = (
        summary['most_common_ydstogo'].astype(int)
    )

    return (
        summary[
            [
                "down",
                "play_type",
                "median_ydstogo",
                "most_common_ydstogo",
                "occurrences",
                "percentage",
            ]
        ].sort_values(['down', 'play_type'])
    )

