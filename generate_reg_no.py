import random

letters ='ABCDEFGHJKLMNOPRSTUWXYZ'
chars = "0123456789ABCDEFGHJKLMNPRSTUWXZ"
numbers = "0123456789"


error_list = ['APA','ARG','ASS','BAJ','BSS','CUC','CUK','DUM','ETA',
            'ETT','FAG','FAN','FEG','FEL','FEM','FES','FET','FNL',
            'FUC','FUK','FUL','GAM','GAY','GEJ','GEY','GHB','GUD',
            'GYN','HAT','HBT','HKH','HOR','HOT','KGB','KKK','KUC',
            'KUF','KUG','KUK','KYK','LAM','LAT','LEM','LOJ','LSD',
            'LUS','MAD','MAO','MEN','MES','MLB','MUS','NAZ','NRP',
            'NSF','NYP','OND','OOO','ORM','PAJ','PKK','PLO','PMS',
            'PUB','RAP','RAS','ROM','RPS','RUS','SEG','SEX','SJU',
            'SOS','SPY','SUG','SUP','SUR','TBC','TOA','TOK','TRE',
            'TYP','UFO','USA','WAM','WAR','WWW','XTC','XTZ','XXL',
            'XXX','ZEX','ZOG','ZPY','ZUG','ZUP'	'ZOO']
part2_reg_nr = ""
part1_reg_nr = ""
flag = True
while flag:
    for i in range(3):
        part1_reg_nr += random.choice(letters)

    for i in range(2):
        part2_reg_nr +=  random.choice(numbers)

    for i in range(1):
        part2_reg_nr += random.choice(chars)

    
    if part1_reg_nr not in error_list:
        flag = False


reg_nr = part1_reg_nr+" "+part2_reg_nr
print(reg_nr)



