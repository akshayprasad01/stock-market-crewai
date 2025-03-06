from crewai import Task

class StockMarketTasks:
    
    def scraper_task(self, agent, companies):
        return Task(
            description = f"""
                    **Task**: Get Financial Records from Yahoo Finance 
                    **Description**: Gather all the financial records from yahoo finance.

                    **Parameters**: 
                    - Companies: {companies}""",
            agent=agent,
            expected_output="Summary of the data obtained from yfinance."
        )