from api import get_request
import asyncio
import pandas as pd

def fetch_plans():
        try:
            plans = get_request('/plan')
            df = pd.DataFrame(data=plans.json()['data'])
            # df = pd.read_json('plans.json')

            plans_with_subscriptions = df[df["total_subscriptions"] > 0].explode('subscriptions')

            plans_with_subscriptions = plans_with_subscriptions[
                [
                    'name',
                    'subscriptions',
                    'total_subscriptions', 
                    'total_subscriptions_revenue', 
                    'plan_code', 
                    'createdAt', 
                    'currency'
                ]
            ]

            return plans_with_subscriptions

        except Exception as e:
            print(e)
# if __name__ == "__main__":
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(fetch_plans())
#         loop.close()

