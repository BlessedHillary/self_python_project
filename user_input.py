# this program is for accepting user input.

name = input(str("What is your name?: "))

try:
    age = int(input(('How old are you?: ')))
except ValueError as e:
        print('enter a number')
        print(e)

country = input(str('Where are you from?: '))
while country == " ":
    print(input(str('You must enter here are you from?: ')))

gender = input(str('What\'s your gender?: '))

print('hello ' + name + ' you are ' + str(age) +  ' years old from ' + country + ' And your are a ' + gender)

