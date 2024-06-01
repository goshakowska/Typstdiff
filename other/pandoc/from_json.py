import json
import pandoc
from pandoc.types import Para, Strikeout, Underline

#  pandoc -t json -f typst changes.typ -o changes.json

doc = pandoc.read(file="changes.json")
print(doc)

paragraph_new = doc[1][2]
print(paragraph_new)

paragraph_new_content = doc[1][2][0]
print(paragraph_new_content)

paragraph_new_underline = Para([Underline(paragraph_new_content)])

doc[1][2] = paragraph_new_underline

paragraph_old = doc[1][3]
print(paragraph_old)

paragraph_old_content = doc[1][3][0]
print(paragraph_old_content)

paragraph_old_strikeout = Para([Strikeout(paragraph_old_content)])

print(paragraph_old_strikeout)
doc[1][3] = paragraph_old_strikeout


json_again = pandoc.write(doc, file="changes_converted.json")

# pandoc -f json -t typst changes_converted.json -o changes_converted.typ

# typst compile changes.typ changes.pdf
# typst compile changes_converted.typ changes_converted.pdf
