from tools.yfin_tools import MyYahooFinTool
import os
from crewai import Agent, LLM

class StockMarketAgents:
    def __init__(self):
        self.watson_llm = LLM(
            model=os.getenv("WATSONX_MODEL_ID_LLAMA"),
            base_url=os.getenv("WATSONX_URL"),
            project_id=os.getenv("WATSONX_PROJECT_ID"),
            max_tokens=2000,
            temperature=0.7,
            api_key=os.getenv("WATSONX_API_KEY"),
            verbose = False
        )

    def stock_dalal(self):
        return Agent(
            role = "Expert Company Data Finder",
            backstory = """Expert in finding the stock Prioce of company""",
            goal = "To find the latest stock price of a company",
            tools = [MyYahooFinTool()],
            verbose=False,
            llm = self.watson_llm
        )