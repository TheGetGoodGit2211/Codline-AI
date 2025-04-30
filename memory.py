from langchain_core.messages import BaseMessage, SystemMessage, AIMessage, HumanMessage
from langchain_openai import OpenAI

from globals import EXTRACTOR_MODEL, SUMMARY_MODEL

from typing import Deque, Tuple, List
from collections import deque

class CodBufferMemory:
    def __init__(self, max_turns: int = 15):
        self._buffer: Deque[Tuple[HumanMessage, AIMessage]] = deque(maxlen=max_turns)

    def add_turn(self, human: HumanMessage, ai: AIMessage):
        self._buffer.append((human, ai))

    def get_turns(self) -> Deque[Tuple[HumanMessage, AIMessage]]:
        return self._buffer

    def to_langchain_messages(self) -> List[BaseMessage]:
        messages = []
        for human, ai in self.get_turns():
            messages.append(human)
            messages.append(ai)
        return messages


class CodSummaryMemory:
    def __init__(self, bufmem: CodBufferMemory):
        point_extractor = OpenAI(base_url=EXTRACTOR_MODEL.endpoint,
                                 api_key=EXTRACTOR_MODEL.key,
                                 model=EXTRACTOR_MODEL.model,
                                 temperature=EXTRACTOR_MODEL.temp)

        point_extractor = OpenAI(base_url=SUMMARY_MODEL.endpoint,
                                 api_key=SUMMARY_MODEL.key,
                                 model=SUMMARY_MODEL.model,
                                 temperature=SUMMARY_MODEL.temp)
