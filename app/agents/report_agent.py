from app.generators.analytical_generator import AnalyticalGenerator

generator = AnalyticalGenerator()

def report_agent(query, data, knowledge, reasoning):
    return generator.generate(
        query=query,
        data=data,
        knowledge=knowledge,
        reasoning=reasoning
    )
