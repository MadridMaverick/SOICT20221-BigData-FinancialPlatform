'''
ham tinh RSI
dung de tinh muc do gia co phieu co cao qua hay thap qua khong

input la 1 chuoi gia stock
output 1 chuoi co do dai tuong tu la chi so rsi %
VD: df['RSI'] = computeRSI(df['close'])
'''

def computeRSI (data, time_window = 14):
    diff = data.diff(1).dropna()        # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]
    
    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]
    
    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

"""
Ham nay giup cho lam muot do thi 
tinh chi so EMA
input la 1 cot gia tri cua ma co phieu
output cot gia tri cua ma co phieu day nhung muot hon

vd: df['EMA'] = calEMA(df['close'])
"""
def computeEMA(data, com = 0.5):
    ema = data.ewm(com= com).mean()
    return ema