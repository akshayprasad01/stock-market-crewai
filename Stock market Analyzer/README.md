# Stock Market Analyzer Agent

This Agent is written to analyze the stock market. Fire it up with any query related to stock market and it will answer you. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required libraries mentioned in the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Environment Variables to setup this agent

Set all the environment variables as mentioned below. Do not change any keys. copy paste the keys as it is and assign new values accordingly. Anything not in <> should not be changed.

```bash
OPENAI_API_KEY = <Your OPENAI_API_KEY >
GOOGLE_API_KEY = <Your Google API KEY >
SERPER_API_KEY = <Your Serper API key >
SEC_API_API_KEY = <Your SEC API Key >
XDG_DATA_HOME = xdg_data_home
MEM0_DIR = mem0_dir
EMBEDCHAIN_CONFIG_DIR = embedchain_dir
CREWAI_STORAGE_DIR = crewai_storage_dir
```

## Entry Point to Agent

> 1. File name : main.py
> 2. Function name : start_crew()

> Parameters for function
>    1. query: str (Write down you query in normal words)

> Parameters for function Example
>    1. query: Get me the top 5 performing companies in the indian stock market.

## Data used to Analyze company portfolios

The SEC filings data from the US and data from yahoo finance is being used. 
Using the data from yahoo finance, Moving averges, Relastive Strength Index, MACD, Bollinger Bands and Volumne Analysis are calculated.

These markers with the SEC Filings data are then fed to the LLM model to understand the trends better and get the analysis from the LLM.