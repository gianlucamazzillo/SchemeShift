"""Main entry point for Project Cover Zero analysis."""

import argparse
import nflreadpy as nfl

from late_downs import analyze_late_downs_by_distance
from rushing import (
    analyze_fourth_down_runs,
    analyze_third_down_runs,
)
from team_by_down import analyze_team_by_down
from ydstogo import (
    analyze_ydstogo_distribution,
    analyze_ydstogo_summary,
)


parser = argparse.ArgumentParser()

#Blueprint for receiving arguments in the terminal
#This shall substitute the SEASON; TEAM and DETAIL_DOWN in the future
parser.add_argument(
    "analysis",
    choices=[
        "ydstogo",
        "team-by-down",
        "rushing",
        "late-downs",
    ],
)

args = parser.parse_args()


SEASON = 2025 #Season to analyze
TEAM = "BUF" #Team to analyze
DETAIL_DOWN = 3 #Down selected for detailed analysis of yards to go distribution

# These inputs are temporary and will later be replaced by user-selected parameters.


print(f"Loading {SEASON} season...")

pbp = nfl.load_pbp(SEASON).to_pandas()


if args.analysis == "ydstogo":

    ydstogo_summary = analyze_ydstogo_summary(
        pbp,
        TEAM,
    )

    ydstogo_distribution = analyze_ydstogo_distribution(
        pbp,
        TEAM,
    )

    detailed_distribution = ydstogo_distribution[
        ydstogo_distribution["down"] == DETAIL_DOWN
    ]

    print(
        f"\n{TEAM} yards to go summary:"
    )

    print(
        ydstogo_summary.to_string(index=False)
    )

    print(
        f"\n{TEAM} down {DETAIL_DOWN} yards to go distribution:"
    )

    print(
        detailed_distribution.to_string(index=False)
    )


elif args.analysis == "team-by-down":

    result = analyze_team_by_down(
        pbp,
        TEAM,
    )

    print(
        f"\n{TEAM} offense by down:"
    )

    print(
        result.to_string(index=False)
    )


elif args.analysis == "rushing":

    kneel_test = pbp[
        (pbp["posteam"] == TEAM)
        & (pbp["play_type"] == 1)
    ].copy()

    print(
        kneel_test[
            [
            "week",
            "down",
            "ydstogo",
            "play_type",
            "rusher_player_name",
            "yards_gained",
            "qb_kneel",
            "desc",
        ]
        ].to_string(index=False)
    )

    player_stats = nfl.load_player_stats(SEASON).to_pandas()

    player_positions = (
        player_stats[
            [
                "player_id",
                "position",
            ]
        ]
        .dropna(subset=["player_id"])
        .drop_duplicates(subset=["player_id"])
        .rename(
            columns={
                "player_id": "rusher_player_id",
                "position": "rusher_position",
            }
        )
    )

    third_down_runs = analyze_third_down_runs(
        pbp,
        TEAM,
        player_positions,
    )

    fourth_down_runs = analyze_fourth_down_runs(
        pbp,
        TEAM,
        player_positions,
    )

    compact_columns = [
        "week",
        "defteam",
        "distance_group",
        "ydstogo",
        "yards_gained",
        "converted",
        "rusher_player_name",
        "rusher_position",
        "qb_scramble",
        "run_type",
        "formatted_run_gap",
    ]

    print(
        f"\n{TEAM} runs on medium and long third downs:"
    )

    print(
        third_down_runs[
            compact_columns
        ].to_string(index=False)
    )

    print(
        f"\n{TEAM} fourth-down runs by distance:"
    )

    print(
        fourth_down_runs[
            compact_columns
        ].to_string(index=False)
    )


elif args.analysis == "late-downs":

    late_down_result = analyze_late_downs_by_distance(
        pbp,
        TEAM,
    )

    print(
        f"\nThird and fourth downs for {TEAM} by distance:"
    )

    print(
        late_down_result.to_string(index=False)
    )