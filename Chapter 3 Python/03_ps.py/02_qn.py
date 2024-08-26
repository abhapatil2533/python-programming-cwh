NAME = input("NAME: ")
DATE= input("DATE: ")

letter = ''' Dear <|NAME|>
                you are selected!
                <|DATE|>'''


letter = letter.replace("<|NAME|>", NAME)
letter = letter.replace("<|DATE|>", DATE)
print(letter)