# kelly-lab

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Educational **Kelly criterion** toolkit: fraction sizing, growth rate, and Monte Carlo bankroll paths.

> Not financial advice. Educational only. Kelly assumes known edge and i.i.d. bets — real markets break both.

## Install

```bash
pip install -e ".[dev]"
```

## Usage

```bash
# Full Kelly for a binary bet: win prob p, decimal odds b (net odds = odds-1)
kelly-lab fraction --p 0.55 --odds 2.0

# Half Kelly (more common in practice)
kelly-lab fraction --p 0.55 --odds 2.0 --fraction 0.5

# Simulate bankroll growth over N independent bets
kelly-lab sim --p 0.55 --odds 2.0 --bankroll 1000 --n 500 --fraction 0.5 --seed 42
```

## API

```python
from kelly_lab import kelly_fraction, expected_log_growth, simulate_bankroll

f = kelly_fraction(p=0.55, b=1.0)  # b = decimal_odds - 1
g = expected_log_growth(p=0.55, b=1.0, f=f)
path = simulate_bankroll(p=0.55, b=1.0, f=0.5 * f, bankroll=1000, n=200, seed=0)
```

## Why this exists

Portfolio piece for DS students bridging probability, EV, and risk of ruin — pairs well with `brier-lab` and tip ledgers.
