from dotenv import load_dotenv
load_dotenv()
import asyncio
from crew_starter import FinancialCrew

def kickOffCrew(companies: str):
    asyncio.set_event_loop(asyncio.new_event_loop())
    # This is the main function that you will use to run your custom crew.
    print("## Welcome to Financial Planner Crew")
    print('-------------------------------')
    financial_crew = FinancialCrew(companies=companies)
    result = financial_crew.run()
    print("\n\n########################")
    print("## Here is you Financial Plan")
    print("########################\n")
    print(result)
    return result