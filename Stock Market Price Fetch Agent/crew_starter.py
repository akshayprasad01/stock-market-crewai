from crewai import Crew
from agents import StockMarketAgents
from tasks import StockMarketTasks

class StockMarketCrew:
    def __init__(self, companies: str):
        self.companies = companies

    def run(self):
        # initialize Agents
        agents = StockMarketAgents()
        stock_dalal = agents.stock_dalal()

        #initialize tasks
        tasks = StockMarketTasks()
        scraper_task = tasks.scraper_task(agent=stock_dalal, companies=self.companies)

        stock_market_crew = Crew(
            agents=[stock_dalal],
            tasks=[scraper_task],
            verbose = False
        )

        result = stock_market_crew.kickoff()
        return result