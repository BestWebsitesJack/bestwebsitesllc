c = open('index.html').read()

# Replace all P&G and Procter & Gamble references
replacements = [
    ("AI Product Manager at Procter &amp; Gamble", "AI Product Manager at a Fortune 500 company"),
    ("AI Product Manager at Procter & Gamble", "AI Product Manager at a Fortune 500 company"),
    ("Procter &amp; Gamble's highest individual recognition", "A Fortune 500's highest individual recognition"),
    ("Procter & Gamble's highest individual recognition", "A Fortune 500's highest individual recognition"),
    ("Procter &amp; Gamble", "a Fortune 500 company"),
    ("Procter & Gamble", "a Fortune 500 company"),
    ("P&amp;G CEO Award", "2025 Fortune 500 CEO Award"),
    ("P&G CEO Award", "2025 Fortune 500 CEO Award"),
    ("P&amp;G AI Product Manager", "Fortune 500 AI Product Manager"),
    ("P&G AI Product Manager", "Fortune 500 AI Product Manager"),
    ("P&amp;G's highest individual recognition", "A Fortune 500's highest individual recognition"),
    ("P&G's highest individual recognition", "A Fortune 500's highest individual recognition"),
    ("AI Product Manager at P&amp;G", "AI Product Manager at a Fortune 500 company"),
    ("AI Product Manager at P&G", "AI Product Manager at a Fortune 500 company"),
    ("from inside P&amp;G", "from inside a Fortune 500 company"),
    ("from inside P&G", "from inside a Fortune 500 company"),
    ("at P&amp;G", "at a Fortune 500 company"),
    ("P&amp;G &middot; Northwestern", "Fortune 500 &middot; Northwestern"),
    ("P&amp;G · Northwestern", "Fortune 500 · Northwestern"),
    ("P&G · Northwestern", "Fortune 500 · Northwestern"),
    ("inside P&amp;G", "inside a Fortune 500 company"),
    ("inside P&G", "inside a Fortune 500 company"),
    ("from P&amp;G", "from a Fortune 500 company"),
    ("from P&G", "from a Fortune 500 company"),
    ("2025 P&amp;G CEO Award", "2025 Fortune 500 CEO Award"),
    ("2025 P&G CEO Award", "2025 Fortune 500 CEO Award"),
]

for old, new in replacements:
    c = c.replace(old, new)

# Check for any remaining P&G references
import re
remaining = re.findall(r'[Pp]&(?:amp;)?[Gg]|[Pp]rocter|procter', c)
remaining = [r for r in remaining if 'schema' not in r]
print('Remaining P&G refs:', remaining if remaining else 'NONE - clean')

open('index.html','w').write(c)
print('Done -', len(c), 'bytes')
