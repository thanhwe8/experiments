import numpy as np
import pandas as pd


from financepy.utils import *
from financepy.products.bonds import *

issue_dt = Date(10,12,2025)
maturity_dt = Date(10,12,2030)
coupon = 0.03
freq_type = FrequencyTypes.ANNUAL
dc_type = DayCountTypes.THIRTY_E_360
face = ONE_MILLION

bond = Bond(issue_dt, maturity_dt, coupon, freq_type, dc_type)
clean_price = 100.0

print(bond)

# Starting pricing
# Assuming we want to price on 2027
settle_dt = Date(21,7,2027)
bond.print_payments(settle_dt)
print(bond.current_yield(clean_price)*100.0)
bond.yield_to_maturity(settle_dt, clean_price, YTMCalcType.UK_DMO)*100.0

# Risk calculation using US Convention
yieldConvention = YTMCalcType.US_STREET
ytm = bond.yield_to_maturity(settle_dt, clean_price, yieldConvention)
print(ytm)
duration = bond.dollar_duration(settle_dt, ytm, yieldConvention)
modified_duration = bond.modified_duration(settle_dt, ytm, yieldConvention)
print("Dollar duration = ", duration)
print("Modified duration = ", modified_duration)

