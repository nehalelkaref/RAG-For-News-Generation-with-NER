from . import bp
from flask import jsonify, request
from app.services.llm_service import get_labels,generate_response
from app.services.news_service import get_headlines
from app.services.scraping_service import scrape_url
from app.services.pinecone_service import embed_articles
from app.services.tools import formulate_query

@bp.route('/get-search-kws', methods=['POST'])
def get_search_kws():
    query = request.get_json()['search_query']
    labels = get_labels(query)
    search_query = formulate_query(labels)
    urls = get_headlines(search_query)
    articles = scrape_url(urls)
    context = embed_articles(articles, query=query)
    answer = generate_response(context,query)

    return {"answer":answer.content}


