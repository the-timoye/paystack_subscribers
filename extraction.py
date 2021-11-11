from api import get_request
import json

import pandas as pd

pd.options.display.max_colwidth

def fetch_plans():
        try:
            plans = get_request('/plan')
            df = pd.DataFrame(data=plans.json()['data'])

            plans_with_subscriptions = df[df["total_subscriptions"] > 0].explode('subscriptions')
            plans_with_subs = plans_with_subscriptions[
                [
                    "id",
                    'name',
                    'subscriptions',
                    'total_subscriptions', 
                    'total_subscriptions_revenue', 
                    'plan_code', 
                    'createdAt', 
                    'currency'
                ]
            ]

            plans_with_subs['subscriptions'].to_json('subs.json', orient='records')
            sd = pd.read_json("subs.json")
            
            plans_with_subs.pop('subscriptions')
            new_df = plans_with_subs.set_index('id').join(sd.set_index('plan'), lsuffix="_pln", rsuffix="_sub")       

            return new_df

        except Exception as e:
            print(e)
if __name__ == "__main__":
    fetch_plans()
