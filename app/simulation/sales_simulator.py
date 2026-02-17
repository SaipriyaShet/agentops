import random
from datetime import datetime, timedelta


def simulate_sales(
    start_revenue=1000,
    days=7,
    volatility=0.15,
    drop_probability=0.2,
    spike_probability=0.15
):
    """
    Generates synthetic sales data to stress-test agents.
    """

    sales = []
    current = start_revenue
    date = datetime.utcnow()

    for i in range(days):
        change = random.uniform(-volatility, volatility)

        # Inject anomaly
        rand = random.random()
        if rand < drop_probability:
            change -= random.uniform(0.2, 0.4)
        elif rand < spike_probability:
            change += random.uniform(0.2, 0.4)

        current = max(100, int(current * (1 + change)))

        sales.append(
            (
                (date - timedelta(days=days - i)).strftime("%Y-%m-%d"),
                current
            )
        )

    return sales
