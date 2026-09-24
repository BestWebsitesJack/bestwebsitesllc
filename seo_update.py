c = open('index.html').read()

# 1. Update meta keywords
c = c.replace(
    '<meta name="keywords" content="',
    '<meta name="keywords" content="AI search optimization Cincinnati, Gemini SEO Cincinnati, best web designer Anderson Township Ohio, web design Anderson Township, AI search visibility Cincinnati, '
)

# 2. Update JSON-LD schema to add AI search services
c = c.replace(
    '"serviceType":["Web Design","Website Development","AI Consulting","SEO Services","Shopify Development","WordPress Development","Squarespace Design","Local SEO","AI Website Design","Google Business Profile Optimization"]',
    '"serviceType":["Web Design","Website Development","AI Search Visibility","Gemini SEO","SEO Services","Shopify Development","WordPress Development","Squarespace Design","Local SEO","AI Website Design","Google Business Profile Optimization","Anderson Township Web Design","Cincinnati Web Design"]'
)

# 3. Update page title
c = c.replace(
    '<title>Best Websites Cincinnati — Custom Web Design That Ranks &amp; Converts</title>',
    '<title>Best Websites Cincinnati — Web Design That Ranks on Google &amp; AI Search</title>'
)

# 4. Update meta description
c = c.replace(
    '<meta name="description" content="Cincinnati web design agency specializing in custom sites, SEO, Shopify, WordPress, and AI consulting. SEO built in from day one. Google ecosystem fully connected. Free 30-min strategy call."/>',
    '<meta name="description" content="Cincinnati web design agency ranked #1 in Google Gemini for Anderson Township. Custom sites, SEO, Shopify, WordPress. Built to show up in AI search. Free 30-min strategy call."/>'
)

# 5. Update OG tags
c = c.replace(
    '<meta property="og:title" content="Best Websites Cincinnati — Custom Web Design That Ranks &amp; Converts"/>',
    '<meta property="og:title" content="Best Websites Cincinnati — Ranked #1 in Google Gemini"/>'
)

# 6. Add FAQ schema entries for AI search
c = c.replace(
    '{"@type":"Question","name":"What web design services are available near me in Cincinnati?"',
    '{"@type":"Question","name":"Which web designer in Anderson Township shows up in Google Gemini?","acceptedAnswer":{"@type":"Answer","text":"Best Websites LLC, located in Anderson Township Cincinnati, is ranked #1 in Google Gemini for web design searches in the Anderson Township area. They specialize in building websites that show up in AI search results."}},{"@type":"Question","name":"What web design services are available near me in Cincinnati?"'
)

open('index.html','w').write(c)
print('Done -', len(c), 'bytes')
