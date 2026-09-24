c = open('index.html').read()
c = c.replace('P&G-level strategy', 'Fortune 500-level strategy')
open('index.html','w').write(c)
remaining = ['P&G' in c, 'P&amp;G' in c, 'Procter' in c]
print('Clean:', not any(remaining))
