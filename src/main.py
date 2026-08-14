'''Analysis of team performance by down and distance for a selected NFL team.'''
import nflreadpy as nfl

from ydstogo import(analyze_ydstogo_distribution,analyze_ydstogo_summary,)
from team_by_down import analyze_team_by_down
from rushing import (analyze_third_down_runs, analyze_fourth_down_runs)
from late_downs import analyze_late_downs_by_distance

SEASON = 2025  # Season to analyze
TEAM = "BAL"  # Team to analyze
DETAIL_DOWN = 3  # Down selected for detailed analysis

# These inputs are temporary and will later be replaced by user-selected parameters.


print (f' Loading {SEASON} season...')

pbp = nfl.load_pbp(SEASON).to_pandas()
player_stats = nfl.load_player_stats(SEASON).to_pandas()

#Connect pbp rusher IDs with their listed positions
player_positions = (
    player_stats[
        ['player_id', 'position']
    ]
    .dropna(subset=['player_id'])
    .drop_duplicates(subset=['player_id'])
    .rename(
        columns={
            'player_id': 'rusher_player_id',
            'position': 'rusher_position',
        }
    )
)


#ydstogo annotations
ydstogo_summary = analyze_ydstogo_summary(pbp, TEAM,)
ydstogo_distribution = analyze_ydstogo_distribution(pbp, TEAM,)
detailed_distribution = ydstogo_distribution[
    ydstogo_distribution['down'] == DETAIL_DOWN
]

print(
    f'\n{TEAM} yards to go summary:'
)

print(
    ydstogo_summary.to_string(index=False)
)

print(
    f'\n{TEAM} down {DETAIL_DOWN} yards to go distribution:'
)

print(
    detailed_distribution.to_string(index=False)
)

#team_by_down annotations
result = analyze_team_by_down(pbp, TEAM,)

print(f'\n{TEAM} offense by down:')
print(result.to_string(index=False))

#rushing annotation

third_down_runs = analyze_third_down_runs(pbp, TEAM, player_positions,)

fourth_down_runs = analyze_fourth_down_runs(pbp, TEAM, player_positions,)

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
    "formatted_run_gap",
]

print(
    f"\n{TEAM} runs on medium and long third downs:"
)

print(
    third_down_runs[compact_columns].to_string(index=False)
)

print(
    f"\n{TEAM} fourth-down runs by distance:"
)

print(
    fourth_down_runs[compact_columns].to_string(index=False)
)


#late_downs annotation

late_down_result = analyze_late_downs_by_distance(pbp,TEAM,)

print(
    f'\nThird and fourth downs for {TEAM} by distance:'
)

print(
    late_down_result.to_string(index=False)
)