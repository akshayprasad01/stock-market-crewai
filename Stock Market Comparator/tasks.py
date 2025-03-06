from crewai import Task
from tools.data_preparation import GatherInfoTool
"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""

class FinancialAdvicetasks:

    def get_financial_data(self, agent, comapnies):
        return Task(
            description = f"""
                    **Task**: Get Financial Records from Yahoo Finance 
                    **Description**: Gather all the financial records from yahoo finance.

                    **Parameters**: 
                    - Companies: {comapnies}""",
            agent = agent,
            expected_output = "Financial records and Analysis",
            tools = [GatherInfoTool.gatherInfoTool]
        )
    
    def identify_best_company(self, agent, companies):
        return Task(
            description = f"""
                    **Task**: Choose a company to invest. 
                    **Description**: Analyse and identify a company to invest based on specific criteria
                    such as moving averages, RSI, MACD, Volumne analysis and also online market trend.
                    Your respose should be a detailed report on the chosen company.

                    **Parameters**: 
                    - Companies: {companies}""",
            agent = agent,
            expected_output = "A detailed report on the chosen company out of the goven companies."
        )
    
    def get_market_trends_online(self, agent, companies):
        return Task(
            description = f"""
                    **Task**: Get Sentiment analysis online for a comany. 
                    **Description**: Analyse and identify a company to invest based on specific criteria
                    such as moving averages, RSI, MACD, Volumne analysis and also online market trend.
                    Your respose should be a detailed report on the chosen company.

                    **Parameters**: 
                    - Companies: {companies}""",
            agent = agent,
            expected_output = ""
        )
    
    def report_generator(self, agent, companies):
        return Task(
            description = f"""
                    **Task**: Draft a comparison report of all the comapanies. 
                    **Description**: Analyse and identify a company to invest based on specific criteria
                    such as moving averages, RSI, MACD, Volumne analysis and also online market trend.
                    Your respose should be a detailed report on the chosen company.
                    Also, provide a comparison report and highlight pros and cons of each company.

                    **Parameters**: 
                    - Companies: {companies}""",
            agent = agent,
            expected_output = "A detailed comparison report of all the companies"
        )