#Find the Difference in Age between Oldest and Youngest Family Members
def difference_in_ages(ages):
    ma_n = 0
    me_n = 200
    for a in ages:
        if a > ma_n:
            ma_n = a
        if a < me_n:
            me_n = a      
    return(me_n, ma_n, ma_n - me_n) 
