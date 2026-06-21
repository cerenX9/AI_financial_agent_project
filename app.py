import os
import streamlit as st
import yfinance as yf
from core.agents import FinancialCrewAgents

st.set_page_config(page_title="Agentic AI: Finansal Analizör", page_icon="📉", layout="wide")

st.title("🤖 Agentic AI: Otonom Finansal Analizör ve Yatırım Ajanı")
st.caption("Doğrudan Gemini Pro Altyapısı ile Güçlendirilmiş Otonom Sistem")

with st.sidebar:
    st.header("🔑 Güvenlik & Konfigürasyon")
    gemini_key = st.text_input("Google Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    st.markdown("---")
    st.markdown("### 💡 Sistem Nasıl Çalışıyor?")
    st.write("Sanal ajanlar sırayla birbirini besleyerek otonom analiz üretir.")

if gemini_key:
    os.environ["GEMINI_API_KEY"] = gemini_key
    st.success("Gemini API Anahtarı Tanımlandı! ✅")
    
    st.subheader("📊 Analiz Edilecek Hisse Senedi")
    ticker = st.text_input("Hisse Kodunu Giriniz (Örn: AAPL, TSLA, THYAO.IS):", "").upper()
    
    if st.button("Otonom Analizi Başlat 🚀", use_container_width=True):
        if ticker:
            with st.spinner(f"🤖 Yapay zeka ajanları {ticker} için çalışıyor..."):
                try:
                    # Yahoo Finance verisini doğrudan çekiyoruz (Hatasız ve hızlı)
                    stock = yf.Ticker(ticker)
                    info = stock.info
                    
                    fk = info.get('trailingPE', 'N/A')
                    fiyat = info.get('currentPrice', 'N/A')
                    market_cap = info.get('marketCap', 'N/A')
                    
                    finansal_veri_ozeti = f"Güncel Fiyat: {fiyat}, F/K Oranı: {fk}, Piyasa Değeri: {market_cap}"
                    
                    # Ajanları ve LLM'i çağırıyoruz
                    factory = FinancialCrewAgents()
                    
                    # Otonom Akış (Chain) Başlıyor
                    # 1. Aşama: Araştırmacı Ajan Bilgi Topluyor
                    prompt_research = f"{ticker} hissesi hakkında güncel piyasa trendlerini ve finansal durumu analiz et. Şu temel verileri kullan: {finansal_veri_ozeti}"
                    response_research = factory.llm.invoke(prompt_research).content
                    
                    # 2. Aşama: Stratejist Ajan Raporu Türkçeleştirip Sonuca Bağlıyor
                    final_prompt = f"""
                    Aşağıdaki analiz verilerini al ve kurumsal bir Türkçe ile nihai bir yatırım raporu hazırla.
                    Raporun sonuna net bir tavsiye (Al/Sat/Tut) ekle.
                    
                    Veriler:
                    {response_research}
                    """
                    nihai_rapor = factory.llm.invoke(final_prompt).content
                    
                    st.success("✨ Analiz Başarıyla Tamamlandı!")
                    st.markdown("## 📋 Nihai Yatırım Stratejisi Raporu")
                    st.markdown(nihai_rapor)
                    
                except Exception as e:
                    st.error(f"Analiz sırasında bir hata oluştu: {str(e)}")
else:
    st.info("⚠️ Uygulamayı başlatmak için lütfen sol taraftaki panelden Gemini API anahtarınızı giriniz.")