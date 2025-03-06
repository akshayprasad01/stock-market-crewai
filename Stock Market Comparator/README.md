# Stock Market Comparpator Agent

This Agent is written to compare different stocks in the stock  market. Fire it up with any query related to stock market and it will answer you. 

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
XDG_DATA_HOME = xdg_data_home
EMBEDCHAIN_CONFIG_DIR = embedchain_dir
CREWAI_STORAGE_DIR = crewai_storage_dir
```

## Entry Point to Agent

> 1. File name : main.py
> 2. Function name : kickOffCrew()

> Parameters for function
>    1. companies: str (Write down companies that you want to compare)

> Parameters for function Example
>    1. companies: Get me the top 5 performing companies in the indian stock market.