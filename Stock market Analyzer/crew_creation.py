from textwrap import dedent
from crewai import Crew
from agents import FinancialAdvisorAgents
from tasks import FinancialAdvisorTasks

class FinancialAdvisorCrew:
    def __init__(self, query):
        self.query = query

    def run(self):
        agents = FinancialAdvisorAgents()
        tasks = FinancialAdvisorTasks()

        # Initialize Agents
        financial_advisor_expert = agents.financialAdvisorExpert()
        investment_strategist = agents.investmentStrategyExpert()
        sector_research_expert = agents.sectorResearchExpert()
        research_analyst_agent = agents.researchAnalystExpert()
        company_research_expert = agents.companyResearchExpert()
        
        # Initialize Tasks
        financial_analysis = tasks.financialAnalysis(
            agent = company_research_expert,
            query = self.query
        )

        filing_analysis = tasks.filingsAnalysis(
            agent = company_research_expert
        )

        research = tasks.research(
            agent = research_analyst_agent, 
            query = self.query
        )

        sector_research = tasks.sectorResearch(
            agent = sector_research_expert,
            query = self.query,
        )

        diversify_investments = tasks.diversifyInvestment(
            agent = investment_strategist,
        )

        recommend = tasks.recommend(
            agent = financial_advisor_expert,
            query = self.query
        )

        crew = Crew(
            agents=[
                financial_advisor_expert,
                investment_strategist,
                sector_research_expert,
                research_analyst_agent,
                company_research_expert
            ],
            tasks=[
                financial_analysis,
                filing_analysis,
                research,
                sector_research,
                diversify_investments,
                recommend
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result