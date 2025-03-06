# Stock Market Price Fetch Agent

This Agent is written to fetch stock price for a given company.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required libraries mentioned in the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Environment Variables to setup this agent

Set all the environment variables as mentioned below. Do not change any keys. copy paste the keys as it is and assign new values accordingly. Anything not in <> should not be changed.

```bash
XDG_DATA_HOME = xdg_data_home
EMBEDCHAIN_CONFIG_DIR = embedchain_dir
CREWAI_STORAGE_DIR = crewai_storage_dir
LITELLM_LOG = DEBUG
WATSONX_URL = https://us-south.ml.cloud.ibm.com
WATSONX_API_KEY = <Your watsonx api key >
WATSONX_PROJECT_ID = <Watsonx project id >
WATSONX_MODEL_ID_LLAMA = watsonx/meta-llama/llama-3-1-70b-instruct
WATSONX_MODEL_ID_GRANITE = watsonx/ibm/granite-13b-chat-v2
```

## Entry Point to Agent

> 1. File name : main.py
> 2. Function name : get_company_info()

> Parameters for function
>    1. company_name: str (Write down company you want to fetch prices for.)

> Parameters for function Example
>    1. company_name: Infosys.