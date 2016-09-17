import newspaper


#Returns the urls of the articles in the news sites
def scrape(news_sites=[]):

    urlmap = {}
    for site in news_sites:
        news = newspaper.build(site)
        urlmap[site] = []
        for article in news.articles:
            urlmap[site].append(article.url)



    return urlmap

sites  = ["http://www.usatoday.com/","http://www.dailymail.co.uk/home/index.html","https://www.yahoo.com/news/?ref=gs","https://www.theguardian.com/world","http://en.canoe.com/home.html","http://edition.cnn.com/WORLD/","http://www.asahi.com/ajw/","http://www.theage.com.au/","http://www.journalgazette.net/","http://washingtonpost.com/","http://www.nytimes.com/","http://foxnews.com/","http://bbc.com/","http://www.111breakingnews.com/?f"]
print(scrape(sites))