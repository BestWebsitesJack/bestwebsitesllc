c = open('index.html').read()

c = c.replace(
    'AI Product Manager · P&amp;G',
    'AI Product Manager · Fortune 500'
)

# Fix line 598 - need to see full line
lines = c.split('\n')
for i, line in enumerate(lines):
    if 'P&G' in line or 'P&amp;G' in line:
        print(f"Still remaining line {i+1}: {line.strip()[:150]}")

print('Done' if 'P&amp;G' not in c and 'P&G' not in c else 'Still has references')
open('index.html','w').write(c)
