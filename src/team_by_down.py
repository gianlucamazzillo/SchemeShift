import pandas as pd

def analyze_team_by_down(pbp: pd.DataFrame, team: str,) -> pd.DataFrame:
    '''Summarize offensive play calling and production by down and play type for a given team.'''
    team_plays = pbp[
        (pbp["posteam"] == team)
        & (pbp["play_type"].isin(["run", "pass"]))
        & (pbp["down"].isin([1, 2, 3, 4]))
    ].copy()

    team_plays['converted'] = (
        team_plays['first_down'].fillna(0).eq(1)
        |   team_plays['touchdown'].fillna(0).eq(1)
    )

    summary = (
        team_plays
        .groupby(['down', 'play_type'], as_index = False)
        .agg(
            number_of_plays = ('play_type', 'size'),
            conversions = ('converted', 'sum'),
            conversion_rate = ('converted', 'mean'),
            average_ydstogo = ('ydstogo', 'mean'),
            median_ydstogo = ('ydstogo', 'median'),
            average_yards=('yards_gained', 'mean'),
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
    summary["median_ydstogo"] = summary["median_ydstogo"].round(2)

    return summary[
        [
            'down',
            'play_type',
            'number_of_plays',
            "play_percentage",
            'conversion_rate',
            'conversions',
            'average_yards',
            'median_ydstogo',
            'average_ydstogo',
        ]
    ].sort_values(['down', 'play_type'])