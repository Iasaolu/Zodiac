#Program by IKPONWONSA ASAOLU 
# DEC 4TH 2019

#function to determine zodiac sign based on month and day
def astrology_machine(month_born, day_born):
    if month_born.lower() == 'january': 
        if (day_born < 20):
            zodiacSign = 'Capricorn'  
        else:
            zodiacSign =  'Aquarius'
          
    elif month_born.lower()  == 'february': 
        if (day_born < 19):
            zodiacSign = 'Aquarius'  
        else:
            zodiacSign = 'Pisces'
          
    elif month_born.lower() == 'march': 
        if (day_born< 21):
            zodiacSign = 'Pisces'
        else: 
            zodiacSign = 'Aries'
          
    elif month_born.lower() == 'april': 
        if (day_born < 20):
            zodiacSign = 'Aries'  
        else:
            zodiacSign = 'Taurus'
          
    elif month_born.lower() == 'may': 
        if (day_born < 21):
            zodiacSign = 'Taurus'  
        else: 
            zodiacSign = 'Gemini'
          
    elif month_born.lower() == 'june': 
        if (day_born < 21) :
            zodiacSign = 'Gemini' 
        else:
            zodiacSign = 'Cancer'
          
    elif month_born.lower() == 'july': 
        if (day_born < 23):
            zodiacSign = 'Cancer'  
        else:
            zodiacSign= 'Leo'
          
    elif month_born.lower() == 'august':        
        if (day_born < 23) :
            zodiacSign = 'Leo' 
        else: 
            zodiacSign = 'Virgo'
          
    elif month_born.lower()  == 'september': 
        if (day_born < 23):
            zodiacSign = 'Virgo'  
        else:
            zodiacSign = 'Libra'
          
    elif month_born.lower() == 'october': 
        if (day_born < 23):
            zodiacSign = 'Libra'  
        else:
            zodiacSign = 'Scorpio'
          
    elif month_born.lower() == 'november': 
        if (day_born < 22) :
            zodiacSign = 'Scorpio' 
        else:
            zodiacSign = 'Sagittarius'

    elif month_born.lower() == 'december': 
        if (day_born < 22): 
            zodiacSign = 'Sagittarius' 
        else: 
            zodiacSign = 'Capricorn'
          
    return zodiacSign

#function to determine the generation user was born in based on year input
def generation_machine(year_born):
    if year_born >= 1900 and year_born <= 1924:
        generation = 'The G.I Generation'
    
    elif year_born >= 1925 and year_born <= 1945:
        generation = "The Silent Generation"
    
    elif year_born >= 1946 and year_born <= 1964:
        generation = "Baby Boomers"

    elif year_born >= 1965 and year_born <= 1979:
        generation = "Generation X"

    elif year_born >= 1980 and year_born <= 2000:
        generation = "Generation Y"

    elif year_born>=2000 and year_born <= 2019:
        generation = "Generation Z"
    
    return generation

#main function for program
def game_time():
    print("Hello there, I am going to determine your age, generation and scorpio sign based on the information you are going to give me!")

    #get user's name
    user_name = input("What is your name? ")

    #get user's date of birth
    monthOfBirth = input("What month were you born in? ")
    months_in_years = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    
    # loops over month, day and year inputs to make sure they are supported by this program
    while monthOfBirth.lower() not in months_in_years:
        print ("Month does not exist!")
        monthOfBirth = input("Please type in your month of birth again? ") 
    else:
        dayOfBirth = int(input("What day were you born? "))
        while dayOfBirth > 31 or dayOfBirth <= 0:
            print ("Day of month does not exist!")
            dayOfBirth = int(input("Please type in your month of birth again? "))
        else:
            yearOfBirth = int(input("What year were you born in? "))
            while yearOfBirth >= 2020 or yearOfBirth <= 1899:
                print ("That year of birth is not supported by this program")
                yearOfBirth = int(input("What year were you born in? "))
            else:
                age = 2019 - yearOfBirth 
                return "Hey "+ user_name + ", you are " + str(age) +  " years old, a " + astrology_machine(monthOfBirth,dayOfBirth) +" and part of "+generation_machine(yearOfBirth)+ "."



print(game_time())
