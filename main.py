import os
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI

# chutes_key = os.getenv("CHUTES_API_TOKEN")
# chutes_endpoint = "https://llm.chutes.ai/v1/"
# model = "deepseek-ai/DeepSeek-V3-0324"
# temp = 0.85
#
# llm = ChatOpenAI(
#         base_url=chutes_endpoint,
#         api_key=chutes_key,
#         model=model,
#         temperature=temp)
#
# response = llm.invoke([HumanMessage("Why is the sky blue?")])
# print(response.content)
