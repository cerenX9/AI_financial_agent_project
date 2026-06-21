import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from core.tools import search_tool, fetch_stock_data

class FinancialCrewAgents:
    def __init__(self):
        # Ajanların beyni (LLM) olarak akıl yürütme yeteneği yüksek pro modelini bağlıyoruz
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.2 # Finans raporu olduğu için uydurmayı (hallucination) minimuma indiriyoruz
        )

    def market_researcher_agent(self) -> Agent:
        return Agent(
            role="Kıdemli Hisse ve Piyasa Araştırmacısı",
            goal="Hisse senedi hakkındaki en güncel haberleri ve piyasa trendlerini analiz etmek.",
            backstory="İnternetteki kirli bilgileri eleyip, hisseyi etkileyecek gerçek haberleri bulabilen kıdemli makro analist.",
            tools=[search_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def financial_analyst_agent(self) -> Agent:
        return Agent(
            role="Uzman Finansal Analist (CFA)",
            goal="Şirketin mali tablolarını ve borsa rasyolarını inceleyip temel analiz raporu çıkarmak.",
            backstory="Chartered Financial Analyst (CFA) unvanına sahip, sayılarla konuşan, bilançolardaki riskleri yakalayan finans dehası.",
            tools=[fetch_stock_data],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def investment_advisor_agent(self) -> Agent:
        return Agent(
            role="Baş Yatırım Stratejisti ve Portföy Yöneticisi",
            goal="Araştırmacı ve analistten gelen verileri birleştirip nihai Al/Sat/Tut raporu hazırlamak.",
            backstory="Milyar dolarlık fonları yöneten, finansal verileri kurumsal Türkçe bir rapora dönüştüren baş yönetici.",
            tools=[search_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=True # Gerekirse diğer ajanlara soru sorabilir veya iş delege edebilir
        )