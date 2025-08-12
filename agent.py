from typing import Annotated
from typing_extensions import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from dotenv import load_dotenv
from youtube import get_transcript
from prompt import  system_prompt
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv()


@tool
def get_yt_transcript(video_id: Annotated[str,"video id from the link"]) -> int:
   """Get the transcription from the youtube video url"""
   response = get_transcript(video_id)
   print("calling transcript with the video id ", video_id)
   return response


class State(TypedDict):
    messages: Annotated[list, add_messages]


class YoutubeAgent:
    def __init__(self):
        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

        # Initialize tool
        self.tools = [get_yt_transcript]

        # Bind tools to LLM
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.system_prompt = system_prompt
        self.conn = sqlite3.connect("checkpoints.sqlite", check_same_thread=False)
        self.memory = SqliteSaver(self.conn)


        # Build the LangGraph agent
        self.graph = self._build_graph()

    def _chatbot_node(self, state: State):
        """Main chatbot logic node."""
        return {"messages": [self.llm_with_tools.invoke(state["messages"])]}

    def _build_graph(self):
        """Constructs the LangGraph state machine."""
        graph_builder = StateGraph(State)

        # Add chatbot node
        graph_builder.add_node("chatbot", self._chatbot_node)

        # Add tools node
        tool_node = ToolNode(self.tools)
        graph_builder.add_node("tools", tool_node)

        # Add conditional edges
        graph_builder.add_conditional_edges("chatbot", tools_condition)
        graph_builder.add_edge("tools", "chatbot")
        graph_builder.add_edge(START, "chatbot")

        return graph_builder.compile(checkpointer=self.memory)

    def run(self, user_message: str, thread_id:str):
        """Runs the agent with a user message."""
        config = {"configurable": {"thread_id": thread_id}}

        state = {"messages": [{"role": "system", "content": self.system_prompt},
                              {"role": "user", "content": user_message}]}
        output =  self.graph.invoke(state,config)
        return output["messages"][-1].content




if __name__ == "__main__":
    agent = YoutubeAgent()
    # result = agent.run("https://www.youtube.com/watch?v=OGYfe6DmaSY&ab_channel=BenAI  i want the summary in 4 lines", "12342")
    result = agent.run("what was the motive of the video ? can you give in 2 points", "12342")
    print(result)
