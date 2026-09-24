#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = ['Thirty', 'Days', 'Of', 'Python']
result = ' ' .join(string)
print(result)

company = "Coding For All"
print(company)
print(len(company))

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(company[0:6])