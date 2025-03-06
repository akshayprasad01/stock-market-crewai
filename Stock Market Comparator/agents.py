import os
from dotenv import load_dotenv
from textwrap import dedent
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.searchtool import SearchTools
from tools.data_preparation import GatherInfoTool
# from tools.serper_tools import serper_tool


class StockMarketAnalyser:
    def __init__(self):
        self.google_genai_llm = ChatGoogleGenerativeAI(
            model = "gemini-2.0-flash-exp",
            verbose = True,
            temperature = 0.7,
            google_api_key = os.getenv("GOOGLE_API_KEY")
        )

    def data_collection_expert(self):
        return Agent(
            role = "Data Collector Agent",
            backstory = dedent("""
                            A meticulous and resourceful agent who scours various sources to gather relevant stock market data, including historical prices, financial reports, news articles, and social media sentiment.
                            Always on the lookout for new and innovative data sources to gain an edge in the market.
                            """),
            goal = dedent("""
                        Ensure the team has a constant stream of high-quality, up-to-date data from diverse sources, 
                        forming the foundation for accurate and insightful analysis.
                        """),
            tools = [GatherInfoTool.gatherInfoTool,
                     SearchTools.search_internet],
            verbose = True,
            llm = self.google_genai_llm,
            allow_delegation = False
        )
    
    def research_expert(self):
        return Agent(
            role='Research Analyst',
            goal='Gather current market data and trends of a given company',
            backstory="""You are an expert research analyst with years of experience in
                        gathering market intelligence. You're known for your ability to find
                        relevant and up-to-date market information and present it in a clear,
                        actionable format.""",
            llm = self.google_genai_llm,
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation = False
        )
    
    def company_selection_expert(self):
        return Agent(
            role = "Company Selection Expert - Analyst",
            goal = "Select the best Company based on market trends, financial reports, market holding and fund manager.",
            backstory = "Expert at analyzing financial data to pick an ideal company.",
            llm = self.google_genai_llm,
            tools = [SearchTools.search_internet],
            verbose = True,
            allow_delegation = False
        )
    
    def expert_financial_analyst(self):
        return Agent(
            role = "Financial Expert",
            goal = "Generate a report after comparing the financial reports of the all the companies",
            backstory = """
                        Expert in analysing and comparing financial reports of various comapnies.
                        Knowledgeable financial expert with a decade experience of understanding market trends.
                        Expert in giving investment advice based on financial reports and market trends.""",
            llm = self.google_genai_llm,
            tools = [GatherInfoTool.gatherInfoTool,
                     SearchTools.search_internet],
            verbose = True,
            allow_delegation = False
        )