from app.generators.base import BaseGenerator

class AnalyticalGenerator(BaseGenerator):

    def generate(self, query, data, knowledge, reasoning):
        revenues = [row[1] for row in data]

        trend = "stable"
        if len(revenues) >= 2:
            if revenues[-1] < revenues[-2]:
                trend = "decline"
            elif revenues[-1] > revenues[-2]:
                trend = "growth"

        return f"""
Business Insight Report

User Question:
{query}

Revenue Trend:
{trend}

Revenue Values:
{revenues}

Knowledge Context:
{knowledge}

Reasoning Trace:
{reasoning}

Conclusion:
The trend likely reflects changes in customer activity or conversion behavior.
""".strip()
