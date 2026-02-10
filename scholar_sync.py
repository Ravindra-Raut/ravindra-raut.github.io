from scholarly import scholarly

author = scholarly.search_author('Ravindra Raut')
author = scholarly.fill(next(author))

for pub in author['publications']:
    scholarly.fill(pub)
    print(pub['bib']['title'], pub.get('num_citations', 0))

