import json
from watson_developer_cloud import AlchemyLanguageV1

def Extract_Sentiment(api_key="your_api", url="http://www.nytimes.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay"):
    alchemy_language = AlchemyLanguageV1(api_key = api_key)
    print(json.dumps(
      alchemy_language.combined(
        url=url,
        extract='title,authots,keywords',
        sentiment=1,

        max_items=1),
      indent=2))
Extract_Sentiment(url = "http://www.nytimes.com/2016/09/18/realestate/so-you-think-your-place-is-small.html?hp&action=click&pgtype=Homepage&clickSource=image&module=photo-spot-region&region=top-news&WT.nav=top-news&mtrref=www.nytimes.com&gwh=689DBA02B8BA5664CCFD84935A2030C3&gwt=pay")