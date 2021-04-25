import re

text1 = '4/25/2021'

if re.match(r'\d+/\d+/\d+', text1):
    print('ok')
else:
    print('no')

m = re.match(r'(\d+)/(\d+)/(\d+)', text1)
if m:
    m,d,y = m.groups()
    print('{}年-{}月-{}日'.format(y,m,d))

