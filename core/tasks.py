from crewai import Task
from core.agents import FinancialCrewAgents

class FinancialCrewTasks:
    
    def research_task(self, agent, ticker: str) -> Task:
        return Task(
            description=f"""
                {ticker} hisse kodu ile belirtilen şirket hakkındaki en son haberleri, 
                piyasa trendlerini ve şirket hakkındaki genel duyarlılığı (olumlu/olumsuz hava) tarayıp analiz et. 
                Geleceğe yönelik potansiyel risk veya büyüme fırsatlarını belirle.
            """,
            expected_output="""
                Şirket hakkındaki en son 5 kritik gelişmeyi, piyasa algısını ve 
                makroekonomik gelişmeleri özetleyen detaylı bir pazar araştırma raporu.
            """,
            agent=agent
        )

    def analysis_task(self, agent, ticker: str) -> Task:
        return Task(
            description=f"""
                {ticker} hissesi için sağlanan finansal verileri çekme aracını kullan. 
                Şirketin F/K oranını, piyasa değerini, güncel fiyatını ve borç/özsermaye gibi rasyolarını incele. 
                Şirketin finansal olarak sağlıklı olup olmadığını ve ucuz mu pahalı mı olduğunu matematiksel olarak doğrula.
            """,
            expected_output="""
                Şirketin finansal rasyolarını, mali tablosunun özetini ve 
                finansal sağlık durumunu gösteren yapılandırılmış temel analiz raporu.
            """,
            agent=agent
        )

    def advice_task(self, agent, ticker: str) -> Task:
        return Task(
            description=f"""
                Araştırmacıdan gelen piyasa haberleri raporu ile Analistten gelen finansal rasyolar raporunu birleştir. 
                Yatırımcılar için risk-ödül dengesini gözeterek nihai bir strateji oluştur.
                Raporun sonuna kesinlikle net bir tavsiye (Güçlü Al / Al / Tut / Sat) ekle.
                TÜM RAPORU PROFESYONEL VE KURUMSAL BİR TÜRKÇE İLE YAZ.
            """,
            expected_output=f"""
                {ticker} hissesi için özel olarak hazırlanmış; Yönetici Özeti, Temel Analiz Bulguları, 
                Piyasa Riskleri ve Nihai Yatırım Tavsiyesi (Al/Sat/Tut) bölümlerini içeren, 
                tamamen Türkçe ve kurumsal dille yazılmış nihai portföy raporu.
            """,
            agent=agent
        )