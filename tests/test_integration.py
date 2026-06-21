import os
import pytest
from core.agents import FinancialCrewAgents
from core.tasks import FinancialCrewTasks

def test_agents_and_tasks_initialization():
    """Ajanların ve görevlerin hafızada doğru nesne tipleriyle (Object Types) oluştuğunu doğrular."""
    # Test esnasında API key hatası almamak için sahte bir çevre değişkeni tanımlıyoruz
    os.environ["GEMINI_API_KEY"] = "fake_test_key_123"
    
    agents_factory = FinancialCrewAgents()
    tasks_factory = FinancialCrewTasks()
    
    # 1. Ajanların oluşum kontrolü
    researcher = agents_factory.market_researcher_agent()
    analyst = agents_factory.financial_analyst_agent()
    
    assert researcher.role == "Kıdemli Hisse ve Piyasa Araştırmacısı"
    assert analyst.role == "Uzman Finansal Analist (CFA)"
    
    # 2. Görevlerin (Tasks) ajanlarla doğru eşleştiğinin kontrolü
    task1 = tasks_factory.research_task(researcher, "TSLA")
    
    assert task1.agent == researcher
    assert "TSLA" in task1.description