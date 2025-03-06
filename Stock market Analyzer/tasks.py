import os
from crewai import Task

class FinancialAdvisorTasks:
    tasks_config = 'config/tasks.yaml'
    def financialAnalysis(self, agent, query):
        return Task(
            description = f"""
                        Unserstand the query "{query}" given to you by the user.
                        Conduct a thorough analysis of company's  stock financial health and market performance.
                        This includes examining key financial metrics such as P/E ratio, EPS growth, revenue trends, 
                        and debt-to-equity ratio. Also, analyze the stock's performance in comparison 
                        to its industry peers and overall market trends.
                        """,
            expected_output = """
                        The final report must expand on the summary provided but now 
                        including a clear assessment of the stock's financial standing, its strengths and weaknesses, 
                        and how it fares against its competitors in the current market scenario.
                        Make sure to use the most recent data possible.
                        """,
            agent = agent,
        )
    
    def filingsAnalysis(self, agent):
        return Task(
            description = """
                        Analyze the latest 10-Q and 10-K filings from EDGAR for the stock in question. 
                        Focus on key sections like Management's Discussion and analysis, financial statements, insider trading activity, 
                        and any disclosed risks. Extract relevant data and insights that could influence
                        the stock's future performance.""",
            expected_output = """
                        Final answer must be an expanded report that now also highlights significant findings
                        from these filings including any red flags or positive indicators for your customer.
                        """,
            agent = agent,
        )
    
    def research(self, agent, query):
        return Task(
            description = f"""
                        Collect and summarize recent news articles, press
                        releases, and market analyses related to the {query}.
                        Pay special attention to any significant events, market sentiments, and analysts' opinions. 
                        Also include upcoming events like earnings and others.
                        """,
            expected_output = """
                        A report that includes a comprehensive summary of the latest news, 
                        any notable shifts in market sentiment, and potential impacts on the stock. 
                        Also make sure to return the stock ticker.
                        Make sure to use the most recent data as possible.""",
            agent = agent,
            context = [self.filingsAnalysis()]
        )
    
    def sectorResearch(self, agent, query):
        return Task(
            description = f"""
                        Collect and summarize recent news articles, press
                        releases, and market analyses related to each sector of the stock market metioned in the {query}.
                        Pay special attention to any significant events, market sentiments, and analysts' opinions. 
                        Also include upcoming events like earnings and others.
                        """,
            expected_output = """
                        A report that includes a comprehensive summary of the latest news, 
                        any notable shifts in market sentiment related to that sector, and potential impacts on all its stocks.
                        Make sure to use the most recent data as possible.
                        """,
            agent = agent,
            context = [self.filingsAnalysis()]
        )
    
    def diversifyInvestment(self, agent):
        return Task(
            description = """
                        consider diversifying your investment across these stocks to mitigate 
                        risk and capitalize on growth across sectors.""",
            expected_output = """
                        Your final answer MUST be table containing diversification of funds in different stocks of different sectors.
                        if should also contain a detailed report on why each of the sector or company has been alocated funds.
                        """,
            context = [self.sectorResearch()],
            agent = agent
        )
    
    def recommend(self, agent, query):
        return Task(
            description = f"""
                        You reveived a query "{query}" from the user.
                        Now, Review and synthesize the analyses provided by the
                        Financial Analyst and the Research Analyst.
                        Combine these insights to form a comprehensive
                        investment recommendation. You MUST Consider all aspects, including financial
                        health, market sentiment, and qualitative data from
                        EDGAR filings. 
                        
                        Make sure to include a section that shows insider 
                        trading activity, and upcoming events like earnings.
                        """,
            expected_output = """
                        Your final answer MUST be a recommendation for your customer. It should be a full super detailed report, providing a 
                        clear investment stance and strategy with supporting evidence.
                        Make it pretty and well formatted for your customer.
                        """,
            agent = agent,
            context = [self.diversifyInvestment()],
        )