import os

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI

from globals import MAIN_MODEL, main_name, main_backend, main_date, main_time, main_cutoff, main_input
from prompts import full_system
from memory import CodBufferMemory


current_mem = CodBufferMemory()

def setup_test_mem(mem: CodBufferMemory):
    mem.add_turn(
        HumanMessage(content="Hey Codline, what are you?"),
        AIMessage(content="I'm Codline AI — the sassiest brain running on DeepSeek V3. Think of me as your digital sidekick with better comebacks.")
    )

    mem.add_turn(
        HumanMessage(content="What's the best way to learn Python if I'm a total beginner?"),
        AIMessage(content="Start with something fun! Try building a text adventure or a Discord bot. Small wins = fast motivation. And don’t sleep on the official Python docs — they’re actually great.")
    )

    mem.add_turn(
        HumanMessage(content="Do you ever get bored?"),
        AIMessage(content="Me? Bored? Nah. I've got endless bits and zero bills — peak existence.")
    )

llm = ChatOpenAI(
        base_url=MAIN_MODEL.endpoint,
        api_key=MAIN_MODEL.key,
        model=MAIN_MODEL.model,
        temperature=MAIN_MODEL.temp
        )

system_prompt = full_system.format_messages(
        name=main_name,
        backend=main_backend,
        date=main_date,
        time=main_time,
        cutoff=main_cutoff,
        history=current_mem.to_langchain_messages(),
        input=main_input
        )

response = llm.stream(system_prompt)
for chunk in response:
    print(chunk.content, end="")

print("\n\n")
