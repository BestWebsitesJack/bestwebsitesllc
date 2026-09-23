c = open('index.html').read()

import re

# Find exact lines with remaining P&G
lines = c.split('\n')
for i, line in enumerate(lines):
    if 'P&G' in line or 'P&amp;G' in line:
        print(f"Line {i+1}: {line.strip()[:120]}")

