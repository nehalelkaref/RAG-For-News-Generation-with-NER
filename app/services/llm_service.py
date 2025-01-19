import os
from langchain_openai import ChatOpenAI
from app.services.tools import parse_aimessage, target_labels

LLM = os.environ.get('LLM_NAME')



model = ChatOpenAI(model=LLM, api_key=os.environ.get("OPENAI_API_KEY"), temperature=0)


def get_labels(search_query):
        prompt = f"Extract named entities from the sentence '{search_query}' The possible common Named Entities \
        types are exclusively: ({", ".join(target_labels)}). Return the output as a JSON that matches the following example: " 
        prompt += f"""Sentence: 'What is happening in Palestine and United States? Tell me news from abc-news' \
                Output: \n
               
                {{
                'GPE' : ['Palestine', 'United States'],
                'MEDIA_OUTLET': ['abc-news']
                }}
                
                """
        prompt+= ' \n Return only the extracted entities, do not provide additional information. if there are no entities to extract return {}'
        response= model.invoke(prompt)
        return parse_aimessage(response.content)


def generate_response(context, query, model=model):
        prompt = f"Answer the question given the below context. If you do not know the answer based on the given context respond with  'Nothing new about \
                this topic'. Reply with just the answer. \n\n "

        context_prompt = ''
        for c in context:
                context_prompt += c + '\n\n'
                
        prompt += f"\n\n Context:\n\n {context_prompt} + \n\n"
        prompt += f"\n\n Question: {query}"
        
        model.temperature=1
        return model.invoke(prompt)
