# SchemeShift

NFL analytics project developed in Python to investigate how teams change
their offensive and defensive identities across situations and over time.


## Objective

The goal of Project Cover Zero is to build a data-driven framework for analyzing NFL team tendencies and identifying how their identities evolve throughout a season.

The project currently focuses on offensive analysis, including play-calling tendencies, down-and-distance behavior, conversion rates and rushing patterns. Defensive analysis will be incorporated after the offensive framework is sufficiently established.

## Current Development

Current analyses include:

- Run/pass distribution by down.
- Play-call percentage by down.
- First-down and touchdown conversion rates.
- Average yards gained.
- Average yards to go.
- Third- and fourth-down analysis by distance.
- Detailed inspection of late-down rushing plays.
- Basic offensive-line gap classification.

## Data

NFL data is accessed through the `nflreadpy` package and the nflverse ecosystem.

The project uses pandas as its primary data-analysis library.