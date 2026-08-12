# SchmeShift - Methodology

This document describes the current methodological definitions in the project that supports the broader goal of identifying how NFL teams change their identity across situations and over time.

The current development focuses on offensive analysis, with defensive analysis planned once the offensive framework is sufficiently established

The methodology will evolve alongside the project. Whenever a new definition emerges, the corresponding analysis shall be reviewed to ensure that historical results remain comparable.

## Data Source

NFL data is loaded using the 'nflreadpy' package, which provides acess to datasets from all nflverse ecosystem.
Play-by-play (pbp) is originally returned as a Polars DataFrame and converted to pandas for analysis.
Player statistics are also loaded when additional player information, such as position, is required.

## Offensive Play Selection

The current offensive analyses include plays that satisfy the following conditions:

- 'posteam' corresponds to the selected team (the one with the possession);
- 'play_type' is either 'run' or 'pass';
Special teams plays are not included in the current offensive analysis.
This definition may be refined in the future to account situations such as sacks, RPOs, penalties, interceptions...

## Conversion

A play is currently classified as converted when it results in either a first down or a touchdown
The implemation uses nflverse fields 'first_down' and 'touchdown'.

Conceptually:
'converted = first_down OR touchdown'
For third and fourth downs, this represents a traditional conversion.
For the first and second downs, the metric should instead be interpreted as the percentage of plays that immediately produced a new first down or TD.

## Play Percentage

'play_percentage' represents the share of offensive plays belonging to a specific play type within the naalyzed situation.

For example, when grouping by down:

'play_percentage = number_of_plays / total_plays_on_down'

## Yards to Go

'ydstogo' represents the number of yards required to reach the line to gain
The current analyses use the aritmetic mean of 'ydstogo' to provide context for play selection and conversion rates.
This is important to compare rushing and passing efficiency. A higher conversion rate doesn't mean that one play type is more effective if it is systematically called in easier situations.

## Distance Groups

Third- and fourth-down situations are currently divided into three groups:

| Distance group | Yards to go |
|---|---:|
| Short | 1–3 |
| Medium | 4–6 |
| Long | 7+ |

These categories are used to compare play selection and performance under roughly similar down-and-distance conditions.
The thresholds are methodological choices rahter than universal NFL definitions and may be revised later.

## Late-Down Analysis

Late down analysis currently focuses on third and fourth downs.
For each combination of:

'down + distance_group + play_type'
the project calculates:
- number of plays;
- play percentage;
- number of conversions;
- conversion rate;
- average yards gained;
- average yards to go.

This segmentation is intended to reduce selection bias that appears when all third or fourth down situations are analyzed together.
For example, rushing plays may appear to convert at a much higher rate than passes simply because runs are disproportionately called in short-yardage situations.

## Run Gap Classification

The nflverse play-by-play dataset provides 'run_location' and 'run_gap' information for rushing plays.

SchemeShift currently creates an additional interpreted field, 'formatted_run_gap', using the following mapping:

| nflverse `run_gap` | Project classification |
|---|---|
| `guard` | A gap |
| `tackle` | B gap |
| `end` | outside |

Whrn 'run_location' is available as 'left' or 'right', the direction is added to the classification
Ex.:
- `left A gap`
- `right B gap`
- `left outside`

If 'run_gap' is missing but 'run_loction' is 'middle', the play is labeled: 'inside - gap unknown'

The original nflverse 'run_gap' field should be preserved. The 'formatted_run_gap' field represents a SchemeShift interpretation and should not replace the raw data.

## Player Position

Rusher position is obtained by joining pbp data with seasonal player stats.
The player identifier used in pbp data ('rusher_player_id') is matched with the player identifier from the player statitistics dataset.
Duplicate player IDs are removed before the merge so that each player contrubutes a single position record to the lookup table.

## Current Limitations

Future versions shuld investigate how to treat:
- sacks;
- quarterback scrambles;
- designed quarterback runs;
- RPOs;
- penalties and nullified plays;
- first downs caused by penalties;
- kneel-downs;
- spikes;
- postseason games;
- personnel packages;
- formations;
- game situation and score differential.

## Future Metrics

Possible future additions include:
- median yards to go;
- yards-to-go distributions;
- explosive-play rate;
- EPA per play;
- success rate;
- player-level conversion rates;
- league-average comparisons;
- performance by personnel package;
- performance by field position;
- performance by game state.

Any new metric should have its definition documented here before being treated
as part of the project's standard analysis.



