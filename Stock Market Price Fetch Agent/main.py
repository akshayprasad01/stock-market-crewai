from dotenv import load_dotenv
load_dotenv()
import asyncio
from logger import logger
from crew_starter import StockMarketCrew

def get_company_info(company_name: str):
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
        company_stockdata = StockMarketCrew(companies=company_name)
        company_info = company_stockdata.run()
        logger.info(company_info)
        print(company_info)
        return company_info
    except Exception as e:
        logger.error(f"error in main get_company_info: {e}")


# get_company_info("MRF, Infosys")