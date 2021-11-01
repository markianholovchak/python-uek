def bonus(years):
    bonus = 0
    yearsCounter = 1
    while(yearsCounter <= years):
        if(yearsCounter <= 5):
            bonus +=100
        elif(yearsCounter > 5 and yearsCounter <= 8 ):
            bonus +=200
        else:
            bonus += 50
        yearsCounter +=1
    return bonus
