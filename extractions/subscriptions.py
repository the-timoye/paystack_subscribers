from api import get_request
import json

import pandas as pd

pd.options.display.max_colwidth


def fetch_plans():
    try:
        plans = get_request('plan')
        df = pd.DataFrame(data=plans.json()['data'])

        plans_with_subscriptions = df[df["total_subscriptions"] > 0].explode(
            'subscriptions')

        plans_with_subscriptions = plans_with_subscriptions[
            [
                "id",
                'name',
                'subscriptions',
                'total_subscriptions',
                'total_subscriptions_revenue',
                'plan_code',
                'createdAt',
                'interval',
                'currency'
            ]
        ]

        plans_with_subscriptions['subscriptions'].to_json(
            'subs.json', orient='records')
        subscriptions = pd.read_json("subs.json")

        plans_with_subscriptions.pop('subscriptions')
        new_df = plans_with_subscriptions.set_index('id').join(
            subscriptions.set_index('plan'), lsuffix="_pln", rsuffix="_sub")

        new_df["no_of_payments"] = new_df['total_subscriptions_revenue'] // \
            new_df['amount']

        return new_df

    except Exception as e:
        print(e)


if __name__ == "__main__":
    fetch_plans()
