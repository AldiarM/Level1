#LEVEL1
#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update({'Python','CSS','Html'})
print(it_companies)
#4
it_companies.remove('Google')
print(it_companies)
#5
# remove() жойылған элемент жиынтықта болмаған кезде қатені көрсетеді
# discard() жойылған элемент жиынтықта болмаған кезде қатені көрсетпейді