import newspaper


#Returns the urls of the articles in the news sites
def scrape(news_sites=[]):

    urlmap = {}
    for site in news_sites:
        news = newspaper.build(site)
        urlmap[site] = []
        for article in news:
            urlmap[site] = article.url


    return urlmap

