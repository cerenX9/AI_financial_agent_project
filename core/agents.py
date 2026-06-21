import os
from google import genai

class FinancialCrewAgents:
    def __init__(self):
        # LangChain'i aradan çıkarıp doğrudan Google'ın resmi istemcisini (Client) kuruyoruz
        api_key = os.getenv("GEMINI_API_KEY", "")
        self.client = genai.Client(api_key=api_key)

    def market_researcher_agent(self):
        return {
            "role": "Kıdemli Hisse ve Piyasa Araştırmacısı",
            "backstory": "İnternetteki haberleri tarayıp makro gelişmeleri özetler."
        }

    def financial_analyst_agent(self):
        return {
            "role": "Uzman Finansal Analist (CFA)",
            "backstory": "Hissenin finansal rasyolarını ve temel verilerini inceler."
        }

    def investment_advisor_agent(self):
        return {
            "role": "Kıdemli Yatırım Stratejisti",
            "backstory": "Araştırma ve analiz sonuçlarını birleştirip Türkçe rapor yazar."
        }