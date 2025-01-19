import ast
import regex as re
import json

target_labels = [
    "PERSON",
    "GPE",
    "LOC",
    "FAC",
    "ORG",
    "DATE",
    "EVENT",
    "WORK_OF_ART",
    "PRODUCT",
    "MONEY",
    "PERCENT",
    "QUANTITY",
    "CARDINAL",
    "NORP",
    "LANGUAGE",
    "CRIME",
    "DISASTER",
    "MEDIA_OUTLET",
    "SPORTS_EVENT",
    "TECH",
    "POLITICAL_EVENT"

]


def parse_aimessage(aimessage):
    # remove json marked syntax
    json_string = aimessage.strip("```json").strip("```")
    json_data = json.loads(json_string)

    return json_data


def formulate_query(entity_dict):
    
    keywords = ''

    if len(entity_dict.keys())>0:
        keys = entity_dict.keys()
        is_last=False
        for index, (_, keyword_list) in enumerate(entity_dict.items()):
            if index==len(entity_dict.keys())-1:
                is_last=True
            keywords += populate_keyword(kws_list=keyword_list, is_last=is_last)
    return keywords

        
def populate_keyword(kws_list, is_last):
    query = ''
    for i in range(len(kws_list)):
        query += kws_list[i]
        if i!=len(kws_list)-1:
            query+= ' AND '
    if not is_last:
        query += ' AND '
    return query


def split_text(articles_list, target_size=500):
    article_chunks = []
    chunks = []
    for article in articles_list:
        
        splits = article.split('.')

        chunk = ''
        for split in splits:

            split = split.replace('\n','')
            split = split.replace('\t','')
            if (len(chunk) + len(split) < target_size):
                
                chunk += split + '. '

            else:
                if chunk!= '':
                    chunk += '. '
                    chunks.append(chunk)
                    chunk = ''
            if (split == splits[-1]) and (chunk!=''):
                chunk += split + '. '
                chunks.append(chunk.strip('\n'))
        article_chunks.append(chunks)
    

    return chunks
                

