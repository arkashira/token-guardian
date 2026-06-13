from token_guardian import TokenGuardian, AIUsage
import pytest

def test_predict_cost_benefit_exceeds_runway():
    ai_usage = [AIUsage(usage=100, cost=500, date='2022-01-01'), AIUsage(usage=200, cost=600, date='2022-01-02')]
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    assert token_guardian.predict_cost_benefit() == "AI usage exceeds projected runway"

def test_predict_cost_benefit_within_runway():
    ai_usage = [AIUsage(usage=100, cost=200, date='2022-01-01'), AIUsage(usage=200, cost=300, date='2022-01-02')]
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    assert token_guardian.predict_cost_benefit() == "AI usage is within projected runway"

def test_provide_predictive_insights_increasing():
    ai_usage = [AIUsage(usage=100, cost=200, date='2022-01-01'), AIUsage(usage=200, cost=300, date='2022-01-02')]
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    assert token_guardian.provide_predictive_insights() == "AI usage is increasing"

def test_provide_predictive_insights_decreasing():
    ai_usage = [AIUsage(usage=200, cost=300, date='2022-01-01'), AIUsage(usage=100, cost=200, date='2022-01-02')]
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    assert token_guardian.provide_predictive_insights() == "AI usage is decreasing"

def test_suggest_cost_saving_measures_exceeds_runway():
    ai_usage = [AIUsage(usage=100, cost=500, date='2022-01-01'), AIUsage(usage=200, cost=600, date='2022-01-02')]
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    assert token_guardian.suggest_cost_saving_measures() == "Consider reducing AI usage or optimizing AI usage strategy"

def test_suggest_cost_saving_measures_within_runway():
    ai_usage = [AIUsage(usage=100, cost=200, date='2022-01-01'), AIUsage(usage=200, cost=300, date='2022-01-02')]
    token_guardian = TokenGuardian(runway=1000, ai_usage=ai_usage)
    assert token_guardian.suggest_cost_saving_measures() == "No cost-saving measures suggested"
