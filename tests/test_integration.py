import os
import pytest
from core.agents import FinancialCrewAgents

def test_financial_agents_creation():
    os.environ["GEMINI_API_KEY"] = "fake_api_key_for_testing"
    factory = FinancialCrewAgents()
    
    # Yeni yapıda istemcinin (client) başarıyla kurulduğunu doğruluyoruz
    assert factory.client is not None