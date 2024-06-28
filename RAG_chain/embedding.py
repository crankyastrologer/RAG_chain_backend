import os

from langchain_community.embeddings.cloudflare_workersai import (CloudflareWorkersAIEmbeddings,)

embeddings = CloudflareWorkersAIEmbeddings(
    account_id=os.environ['ACCOUNT_ID'],
    api_token=os.environ['API_TOKEN'],
    model_name=os.environ['MODEL_NAME'],
)
