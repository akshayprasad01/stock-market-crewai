from crewai import Crew
from agents import StockMarketAnalyser
from tasks import FinancialAdvicetasks

class FinancialCrew:
    def __init__(self, companies):
        self.companies = companies

    def run(self):
        agents = StockMarketAnalyser()
        tasks = FinancialAdvicetasks()

        data_collection_expert = agents.data_collection_expert()
        research_expert = agents.research_expert()
        company_selection_expert = agents.company_selection_expert()
        expert_financial_analyst = agents.expert_financial_analyst()


        #tasks
        get_financial_data = tasks.get_financial_data(
            agent=data_collection_expert,
            comapnies=self.companies
        )

        identify_best_company = tasks.identify_best_company(
            agent=company_selection_expert,
            companies=self.companies
        )

        get_market_trends_online = tasks.get_market_trends_online(
            agent = research_expert,
            companies=self.companies
        )

        report_generator = tasks.report_generator(
            agent=expert_financial_analyst,
            companies=self.companies
        )

        crew = Crew(
            agents=[data_collection_expert,
                    research_expert,
                    company_selection_expert,
                    expert_financial_analyst],
            tasks=[get_financial_data,
                   get_market_trends_online,
                   identify_best_company,
                   report_generator],
            verbose=True,
            # cache=False
        )

        result = crew.kickoff()
        return result