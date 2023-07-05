from books import Books

title1 = Books("Danielle Steele,", "378,", "Mystery,", "2002,", "The Cottage.")
title2 = Books("Tony Anthony,", "256,", "Biography,", "2010,", "Taming the Tiger.")
title3 = Books("Wale Akinyemi,", "145,", "Biography,", "2007,", "The Billionaire Within.")
title4 = Books("Rachel Renee,", "389,", "Fiction,", "2015,", "Miss Know-it-all.")
title5 = Books("Shirley Hailstock,", "218,", "Romance,", "2009,", "A Father's Fortune.")

print(title1.author, title1.pages, title1.genre, title1.year, title1.title)
print(title2.author, title2.pages, title2.genre, title2.year, title2.title)
print(title3.author, title3.pages, title3.genre, title3.year, title3.title)
print(title4.author, title4.pages, title4.genre, title4.year, title4.title)
print(title5.author, title5.pages, title5.genre, title5.year, title5.title)