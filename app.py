import os
import streamlit as st
from crewai import Crew, Process
from core.agents import FinancialCrewAgents
from core.tasks import FinancialCrewTasks

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Agentic AI: Finansal Analizör", page_icon="📉", layout="wide")

st.title("🤖 Agentic AI: Otonom Finansal Analizör ve Yatırım Ajanı")
st.caption("CrewAI ve Gemini Pro ile Güçlendirilmiş Çoklu Yapay Zeka Mürettebatı")

# Sidebar - Güvenli API Anahtarı ve Input Yönetimi
with st.sidebar:
    st.header("🔑 Güvenlik & Konfigürasyon")
    
    # Kullanıcıdan API key'leri alıyoruz (Eğer sistemde yüklü değilse)
    gemini_key = st.text_input("Google Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    serper_key = st.text_input("Serper (Google Search) API Key", type="password", value=os.getenv("SERPER_API_KEY", ""))
    
    st.markdown("---")
    st.markdown("### 💡 Nasıl Çalışır?")
    st.write("1. **Araştırmacı Ajan** internete çıkıp haberleri tarar.")
    st.write("2. **Analist Ajan** Yahoo Finance'ten bilançoyu inceler.")
    st.write("3. **Stratejist Ajan** verileri birleştirip Türkçe rapor üretir.")

# API Key Kontrolü ve Çevre Değişkenlerine Enjekte Edilmesi
if gemini_key and serper_key:
    os.environ["GEMINI_API_KEY"] = gemini_key
    os.environ["SERPER_API_KEY"] = serper_key
    
    st.success("API Anahtarları Başarıyla Tanımlandı! Sistem Analize Hazır. ✅")
    
    # Kullanıcı Giriş Alanı
    st.subheader("📊 Analiz Edilecek Hisse Senedi")
    ticker = st.text_input("Hisse Kodunu Giriniz (Örn: Apple için AAPL, Tesla için TSLA, Türk Hava Yolları için THYAO.IS):", "").upper()
    
    if st.button("Otonom Analizi Başlat 🚀", use_container_width=True):
        if ticker:
            with st.spinner(f"🤖 Yapay zeka mürettebatı {ticker} hissesi için toplandı... Analiz ediliyor, lütfen bekleyiniz (Bu işlem 1-2 dakika sürebilir)..."):
                
                try:
                    # 1. Ajan ve Görev Nesnelerini Örnekleme (Instantiation)
                    agents = FinancialCrewAgents()
                    tasks = FinancialCrewTasks()
                    
                    researcher = agents.market_researcher_agent()
                    analyst = agents.financial_analyst_agent()
                    advisor = agents.investment_advisor_agent()
                    
                    task1 = tasks.research_task(researcher, ticker)
                    task2 = tasks.analysis_task(analyst, ticker)
                    task3 = tasks.advice_task(advisor, ticker)
                    
                    # 2. Mürettebatı (Crew) Hiyerarşik / Sıralı Süreçle Ayağa Kaldırma
                    financial_crew = Crew(
                        agents=[researcher, analyst, advisor],
                        tasks=[task1, task2, task3],
                        process=Process.sequential, # Görevler sırayla birbirini besleyerek akacak
                        verbose=True
                    )
                    
                    # 3. Süreci Başlatma (Kickoff)
                    result = financial_crew.kickoff()
                    
                    # 4. Sonuçları Ekrana Yazdırma
                    st.success("✨ Analiz Başarıyla Tamamlandı!")
                    
                    st.markdown("## 📋 Nihai Yatırım Stratejisi Raporu")
                    st.markdown(result)
                    
                except Exception as e:
                    st.error(f"Analiz sırasında bir hata oluştu: {str(e)}")
        else:
            st.warning("Lütfen geçerli bir hisse senedi kodu giriniz.")
else:
    st.info("⚠️ Uygulamayı başlatmak için lütfen sol taraftaki panelden Gemini ve Serper API anahtarlarınızı giriniz.")