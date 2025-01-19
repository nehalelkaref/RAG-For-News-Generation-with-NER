from newsapi import NewsApiClient
import os
from datetime import datetime, timedelta
# from app.services.tools import formulate_query

api = NewsApiClient(api_key=os.environ.get('NEWSAPI_KEY'))
end_interval = datetime.now()
start_interval = end_interval - timedelta(weeks=1)

def get_headlines(query):
    
    articles=api.get_everything(from_param=start_interval.strftime("%Y-%m-%d"),
                                to=end_interval.strftime("%Y-%m-%d"),
                                language="en",q=query,
                                sort_by="relevancy")
    if articles['status'] == 'ok':
        url_articles = [articles['articles'][i]['url'] for i in range(10)]
        return url_articles
    