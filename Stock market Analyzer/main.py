import os
from dotenv import load_dotenv
load_dotenv()
import tracemalloc
tracemalloc.start()
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)
from textwrap import dedent
from crew_creation import FinancialAdvisorCrew

def start_crew(query: str):
    financial_crew = FinancialAdvisorCrew(query=query)
    result = financial_crew.run()

    return result

if __name__ == "__main__":
    print("Welcome to Financial Planner!!")
    print('-------------------------------')
    query = input(
        dedent("""
      Fire me up with any query related to Stock Market!!
    """))

    financial_crew = FinancialAdvisorCrew(query=query)
    result = financial_crew.run()
    print("\n\n########################")
    print("## Here is you Financial Plan")
    print("########################\n")
    print(result)