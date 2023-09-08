str = 'X-DSPAM-Confidence:0.8475'
str = 'X-DSPAM-Confidence: 0.8475'
print(str)
colon= str.find(':')
print(colon)
value = str[colon+2:]
final = float(value)
print(final)

