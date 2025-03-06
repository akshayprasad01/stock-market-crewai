import os
from crewai import Agent
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM
from tools.calculator_tool import CalculatorTool
from tools.yfinance_tool import YFinTool
from tools.serper_tools import SearchTools
from tools.sec_tools import SEC10KTool, SEC10QTool
from crewai_tools import ScrapeWebsiteTool, TXTSearchTool, SerperDevTool
# from tools.website_search_tools import website_search_tool

class FinancialAdvisorAgents:
    def __init__(self):
        # self.google_genai_llm = ChatGoogleGenerativeAI(
        #     model = "gemini-2.0-flash-exp",
        #     verbose = True,
        #     temperature = 0.7,
        #     google_api_key = os.getenv("GOOGLE_API_KEY")
        # )

        # self.google_genai_llm = LLM(
        #     model = "gemini-2.0-flash-exp",
        #     api_key = os.getenv("GOOGLE_API_KEY"),
        #     temperature=0.7
        # )

        self.openAI_LLM = LLM(
            model=  "gpt-3.5-turbo", # "gpt-3.5-turbo", # "gpt-4",
            api_key = os.getenv("OPENAI_API_KEY"),
            temperature=0.8,
        )

    def financialAdvisorExpert(self):
        return Agent(
            role = "Financial Advisor Agent",
            goal = "Financial expert capable of answering any questions related to stock markets",
            backstory = """
                    A Financial expert with a decade full of experience in stock market.
                    With Complete knowledge of stock market and its trends, has the capability to answer 
                    anything reated to stock market.
            """,
            llm = self.openAI_LLM,
            tools = [
                ScrapeWebsiteTool(),
                # website_search_tool(),
                CalculatorTool()
            ],
            verbose = True, 
            allow_delegation = False
        )
    
    def investmentStrategyExpert(self):
        return Agent(
            role = "Investment Strategy Expert",
            goal = "Diversifying investment across stocks to mitigate risk and capitalize on growth across sectors.",
            backstory = """
                    Develops and implements investment strategies to help clients achieve their financial goals. 
                    Analyze market trends, economic data, and risk factors to build diversified portfolios.
                    With a focus on long-term growth, they advise on asset allocation and investment decisions to maximize returns.
            """,
            llm = self.openAI_LLM,
            tools = [
                ScrapeWebsiteTool(),
                # website_search_tool(),
                CalculatorTool(),
                SearchTools.search_internet,
                SEC10KTool(),
                SEC10QTool(),
                YFinTool.gatherInfoTool,
                YFinTool.getStockPrice
            ],
            verbose = True, 
            allow_delegation = False
        )
    
    def sectorResearchExpert(self):
        return Agent(
            role = "Financial sector research Expert",
            goal = "Research and come up with top 5 performing comapnies in each sector.",
            backstory = """
                    A research Analyst with a decade full of experience in evaluating and rating financial sectors 
                    based on their performance, ranking them in ascending order. Identify the top 5 performing companies 
                    within each sector, using comprehensive analysis of market trends and financial data. 
                    Guide investors in selecting high-potential stocks from the best-performing sectors.
            """,
            llm = self.openAI_LLM,
            tools = [
                ScrapeWebsiteTool(),
                # website_search_tool(),
                SearchTools.search_internet],
            verbose = True,
            allow_delegation = False
        )
    
    def companyResearchExpert(self):
        return Agent(
            role = "Company Research Expert",
            goal = "Research about a company throughly",
            backstory = """
                    A research analyst with tons of experience in conducting in-depth research to understand every aspect 
                    of a company, including its financials, management, operations, and market position. 
                    Analyze industry trends, competitive landscape, and growth potential to provide comprehensive insights. 
                    Their findings helped investors and stakeholders make informed decisions about the company's future prospects.
            """,
            llm = self.openAI_LLM,
            tools = [
                ScrapeWebsiteTool(),
                # website_search_tool(),
                CalculatorTool(),
                SearchTools.search_internet,
                SEC10KTool(),
                SEC10QTool(),
                YFinTool.gatherInfoTool,
                YFinTool.getStockPrice
            ],
            verbose = True,
            allow_delegation = False
        )
    
    def researchAnalystExpert(self):
        return Agent(
            role = "Staff Research Analyst",
            goal = "Being the best at gathering, interpreting data and amazing your customer with it",
            backstory = """
                    Known as the BEST research analyst, you're skilled in sifting through news, company announcements,
                    and market sentiments. Now you're working on a super important customer.""",
            llm = self.openAI_LLM,
            tools = [
                ScrapeWebsiteTool(),
                # WebsiteSearchTool(), 
                SEC10QTool(),
                SEC10KTool()
            ],
            verbose = True,
            allow_delegation = False
        )
    