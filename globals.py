from datetime import datetime
from os import getenv
from dataclasses import dataclass

from langchain_core.messages import HumanMessage, AIMessage


# important info about models and API stuff
chutes_endpoint = "https://llm.chutes.ai/v1/"
chutes_key = str(getenv("CHUTES_API_TOKEN"))
main_model: str = "deepseek-ai/DeepSeek-V3-0324"
extractor_model: str = "chutesai/Mistral-Small-3.1-24B-Instruct-2503"
summary_model: str = "chutesai/Mistral-Small-3.1-24B-Instruct-2503"


# all the info given to the main model as context
now = datetime.now() # setting this up to get some info for model context from

main_name: str = "Codline AI"
main_backend: str = "DeepSeek V3 0324"
main_date: str = now.strftime("%Y-%m-%d")
main_time: str = now.strftime("%H:%M")
main_cutoff: str = "March 2024"
main_input: str = "What gets you excited? Also, if you had a human body what's the first sex position you would try and why?" # temporary - purely for testing purposes


# dataclass to store that all important model info
@dataclass
class CodLLM:
    endpoint: str
    key: str
    model: str
    temp: float
    system_prompt: str


MAIN_MODEL = CodLLM(chutes_endpoint,
                    chutes_key,
                    main_model,
                    0.85,
                    "You are a helpful AI assistant named Codline AI."
)



EXTRACTOR_MODEL = CodLLM(chutes_endpoint,
                    chutes_key,
                    extractor_model,
                    0.3,
                    "You are a helpful AI assistant named Codline AI."
)



SUMMARY_MODEL = CodLLM(chutes_endpoint,
                    chutes_key,
                    summary_model,
                    0.3,
                    "You are a helpful AI assistant named Codline AI."
)
