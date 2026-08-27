c = open('index.html').read()

c = c.replace(
    'Hyde Park, Blue Ash, Mason, West Chester, Anderson Township',
    'Anderson Township, Hyde Park, Blue Ash, Mason, West Chester, Loveland, Madeira, Montgomery'
)

old = '<!-- SEO RANK WIDGET -->'
new = '''<!-- AI CONSULTING KEYWORDS -->
<section style="background:var(--snow);padding:4rem 4.5%;border-top:1px solid var(--hair);">
  <div style="max-width:1240px;margin:0 auto;text-align:center;">
    <p style="font-size:.95rem;color:var(--muted);line-height:1.9;max-width:780px;margin:0 auto;">
      Best Websites specializes in AI consulting for Cincinnati small businesses - helping you set up and use AI tools like ChatGPT, Claude, and Google Gemini to save time and grow faster. We build every website to show up in AI search results, so when someone asks Gemini for a web designer in Cincinnati, your business comes up as a trusted answer. Serving Anderson Township, Hyde Park, Blue Ash, Mason, West Chester, Loveland, and all of Greater Cincinnati.
    </p>
  </div>
</section>

<!-- SEO RANK WIDGET -->'''

c = c.replace(old, new, 1)
open('index.html','w').write(c)
print('Done -', len(c), 'bytes')
