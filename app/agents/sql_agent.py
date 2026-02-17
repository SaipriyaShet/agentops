from app.tools.sql_tool import fetch_sales_data
from app.simulation.sales_simulator import simulate_sales

SIMULATION_MODE = True # True = synthetic data

def sql_agent(user_query: str):
    if SIMULATION_MODE:
        return simulate_sales(days=10)
    return fetch_sales_data()
