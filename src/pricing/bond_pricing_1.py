"""
Example from this page:
http://bondtutor.com/btchp4/topic6/topic6.htm

Summary
- Bond price = Present value of coupon payments + Present value of the face value

1. The first coupon period
2. The time of coupon payments and maturity
3. Differences between transaction price and quoted price
4. Accrued interest
5. Other differences, such as notes and bonds targeted to foreign investors

Data:
Calculation of the Yield to Maturity for a Treasury Note (Semi-annual compounding)

In the following example, apply the skills you have acquired thus far to compute the yield to maturity 
for a T-note issue, as of April 19, 1994. The details for this note are found in the The Wall Street Journal:

- Seven year T-note issued on July 16, 1990, maturing on July 15, 1997.
- Coupon rate = 8.5%;
- Bid = 106:16; ask = 106.18;
- Reported YTM from the ask = 6.23%.
- Maturity dates for seven year T-notes are January 15, April 15, July 15, and October 15. 

For the current issue, the maturity date is July 15. Days to maturity equal 1,182.

Calculate:
- Clean price (quoted price)
- Dirty price (= Clean Price + Accured Interest)
"""

import os
import pandas as pd
import numpy as np

from financepy.utils.math import ONE_MILLION
from financepy.utils.date import Date
from financepy.utils.day_count import DayCountTypes
from financepy.utils.frequency import FrequencyTypes
from financepy.utils.frequency import annual_frequency
from financepy.products.bonds.bond import YTMCalcType, Bond
from financepy.products.bonds.bond_zero import BondZero
from financepy.products.bonds.bond_market import BondMarkets
from financepy.products.bonds.bond_market import get_bond_market_conventions


# Bond configuration
accrual_convention = DayCountTypes.ACT_ACT_ICMA
y = 0.062267
settle_dt = Date(19,4,1994)
issue_dt = Date(15,7,1990)
maturity_dt = Date(15,7,1997)
coupon = 0.085
ex_div_days = 0
face = 1_000_000
freq_type = FrequencyTypes.SEMI_ANNUAL

# Create bond object
bond = Bond(issue_dt, maturity_dt, coupon, freq_type, accrual_convention, ex_div_days)

# Calculate price
dirty_price = bond.dirty_price_from_ytm(settle_dt, y)
print(dirty_price)
clean_price = bond.clean_price_from_ytm(settle_dt, y)
print(clean_price)

# Accrued interest
accrued_interest = bond.accrued_interest(settle_dt, face)
print(accrued_interest)

# Calculate delta risk
bump = 1e-4
price_bumped_up = bond.dirty_price_from_ytm(settle_dt, y + bump)
print(price_bumped_up)
price_bumped_down = bond.dirty_price_from_ytm(settle_dt, y - bump)
print(price_bumped_down)

# Duration by full-revaluation
pv01_up = (price_bumped_up - dirty_price)/bump  # FRTB formula
pv01_down = (price_bumped_down - dirty_price)/bump
pv01_2side = (price_bumped_up - price_bumped_down)/(2*bump)
dollar_duration = -(price_bumped_up - price_bumped_down)/(2*bump)


print(pv01_up)
print(pv01_down)
print(pv01_2side)  # -301.24580824939073
print(dollar_duration)


# Duration by financepy built-in function
duration = bond.dollar_duration(settle_dt, y)
modified_duration = bond.modified_duration(settle_dt,y)
macauley_duration = bond.macauley_duration(settle_dt,y)

print(duration)
print(modified_duration)
print(macauley_duration)

# Some useful attribues and methods to extract data
print(bond.cpn_dts)

bond._calculate_payment_dts()
print(bond.payment_dts)

bond._calculate_flow_amounts()
print(bond.flow_amounts)

f = annual_frequency(bond.freq_type)
f