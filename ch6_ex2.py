text = "X-DSPAM-Confidence:    0.8475"
length=len(text)
pos_1=text.find(' ')
number=text[pos_1:length]
number=number.strip()
number=float(number)
print number