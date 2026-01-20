import numpy as np
import financepy
from financepy.utils import *
from financepy.products.bonds import *



# Take an example to price US TREASURY BOND
issue_dt = Date(30,11,2022)

# settle_dt = Date(6,2,2023)  # Assuming the settle date is before ex dividend date
settle_dt = Date(26,5,2023)  # Assuimng the settle date is after ex dividend date
maturity_dt  = Date(30,11,2024)
coupon = 0.045

freq_type = FrequencyTypes.SEMI_ANNUAL
dc_type = DayCountTypes.ACT_ACT_ICMA
ex_div_days = 5
face = ONE_MILLION

bond = Bond(issue_dt, maturity_dt, coupon, freq_type, dc_type, ex_div_days)

clean_price = 100 + 4/32 + 1/64  # price was quoted as 100-04+
print(clean_price)

# Start replicating function
print(bond.cpn_dts) ## [30-NOV-2022, 31-MAY-2023, 30-NOV-2023, 31-MAY-2024, 30-NOV-2024]

# 1. Replicating _calc_pcd_ncd() function
print("1. Replicating _calc_pcd_ncd()")
num_flows = len(bond.cpn_dts)
print("num_flows is", num_flows)

for  i_flow in range(1, num_flows):
    print("Current flow is: " , i_flow)
    if bond.cpn_dts[i_flow] > settle_dt:
        print(bond.cpn_dts[i_flow-1])
        print(bond.cpn_dts[i_flow])
        break

print("2. Replicating accured interest")
bond._calc_pcd_ncd(settle_dt)
dc = DayCount(bond.dc_type)
cal = Calendar(bond.cal_type)
ex_div_dt = cal.add_business_days(bond.ncd, -1*bond.ex_div_days)
print(bond.ex_div_days)
print(ex_div_dt)


# C:\code\FinancePy\financepy\utils\day_count.py
(acc_factor, num, _) = dc.year_frac(bond.pcd, settle_dt, bond.ncd, bond.freq_type)
print(acc_factor)
print(num)
print(_)
print(bond.cpn)
print(bond.accrued_interest(settle_dt, face))
print(bond.payment_dts)
for dt in bond.payment_dts:
    print("this is dt", dt)



dirty_price = bond.dirty_price_from_ytm(settle_dt, 0.05,  YTMCalcType.US_TREASURY)
print(dirty_price)