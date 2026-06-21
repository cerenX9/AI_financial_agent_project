import os
from langchain_google_genai import ChatGoogleGenerativeAI

class FinancialCrewAgents:
    def __init__(self):
        # Model ismini Google'ın tam ve güncel formatına (models/gemini-1.5-pro) çevirdik
        self.llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-pro",
            google_api_key=os.getenv("GEMINI_API_KEY", ""),
            temperature=0.2
        )

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