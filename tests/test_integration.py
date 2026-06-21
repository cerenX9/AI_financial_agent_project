import os
import pytest
from core.agents import FinancialCrewAgents

def test_financial_agents_creation():
    # Test esnasında API anahtarı hatası almamak için geçici bir sahte anahtar tanımlıyoruz
    os.environ["GEMINI_API_KEY"] = "fake_api_key_for_testing"
    
    factory = FinancialCrewAgents()
    researcher = factory.market_researcher_agent()
    analyst = factory.financial_analyst_agent()
    
    assert researcher["role"] == "Kıdemli Hisse ve Piyasa Araştırmacısı"
    assert analyst["role"] == "Uzman Finansal Analist (CFA)"
    assert "backstory" in researcher