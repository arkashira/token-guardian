import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class AIUsage:
    usage: float
    cost: float
    date: str

class TokenGuardian:
    def __init__(self, runway: float, ai_usage: list[AIUsage]):
        self.runway = runway
        self.ai_usage = ai_usage

    def predict_cost_benefit(self):
        total_cost = sum(usage.cost for usage in self.ai_usage)
        if total_cost > self.runway:
            return "AI usage exceeds projected runway"
        else:
            return "AI usage is within projected runway"

    def provide_predictive_insights(self):
        usage_trend = [usage.usage for usage in self.ai_usage]
        if len(usage_trend) > 1:
            trend = usage_trend[-1] - usage_trend[-2]
            if trend > 0:
                return "AI usage is increasing"
            elif trend < 0:
                return "AI usage is decreasing"
            else:
                return "AI usage is stable"
        else:
            return "Not enough data to provide insights"

    def suggest_cost_saving_measures(self):
        if sum(usage.cost for usage in self.ai_usage) > self.runway:
            return "Consider reducing AI usage or optimizing AI usage strategy"
        else:
            return "No cost-saving measures suggested"

def load_ai_usage_from_json(file_path: str) -> list[AIUsage]:
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [AIUsage(usage=usage['usage'], cost=usage['cost'], date=usage['date']) for usage in data]

def main():
    ai_usage = load_ai_usage_from_json('ai_usage.json')
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    print(token_guardian.predict_cost_benefit())
    print(token_guardian.provide_predictive_insights())
    print(token_guardian.suggest_cost_saving_measures())

if __name__ == "__main__":
    main()
