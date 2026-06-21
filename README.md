# 🤖 Agentic AI: Otonom Finansal Analist ve Yatırım Ajanı

Bu proje, geleneksel LangChain veya CrewAI gibi ağır ve bağımlılık yaratan aracı kütüphaneleri ortadan kaldırarak, doğrudan **Google GenAI resmi SDK'sı** (`google-genai`) ve `gemini-2.5-flash` modeliyle inşa edilmiş **katmanlı bir otonom ajan (Agentic AI) mimarisidir.** Kullanıcıdan alınan bir hisse senedi kodu (örn: `AAPL`, `NVDA`, `THYAO.IS`) üzerinden tamamen otonom bir şekilde finansal verileri çeker, analiz eder ve kurumsal düzeyde Türkçe yatırım stratejisi raporları hazırlar.

---

## 🚀 Öne Çıkan Özellikler

* **Resmi Google GenAI Entegrasyonu:** `gemini-2.5-flash` modeliyle ultra hızlı, kararlı ve düşük maliyetli API çağrıları.
* **Otonom Çoklu Ajan Akışı (Chain of Thought):** Bilgi toplayan araştırmacı ajan ve bu bilgileri sentezleyip rapora dönüştüren stratejist ajan yapısı.
* **Canlı Finansal Veri Verimliliği:** `yfinance` (Yahoo Finance) entegrasyonu ile anlık fiyat, F/K oranı ve piyasa değeri entegrasyonu.
* **Modern ve Dinamik Arayüz:** Kullanıcı dostu, API anahtarı güvenliği sağlayan şık bir **Streamlit** paneli.
* **Robust Test Altyapısı:** Projenin her bileşeni `pytest` ile birim (unit) ve entegrasyon testlerinden başarıyla geçmektedir.

---

## 📐 Proje Mimarisi (Katmanlı Yapı)

Proje, temiz kod (clean code) prensiplerine uygun olarak modüler bir mimaride tasarlanmıştır:

```text
AI_financial_agent_project/
│
├── core/
│   ├── __init__.py
│   ├── agents.py       # Google GenAI istemcisi ve ajan rolleri
│   ├── tasks.py        # Ajanların otonom görev tanımları
│   └── tools.py        # Finansal veri çekme araçları (yfinance)
│
├── tests/
│   ├── test_integration.py  # Entegrasyon ve API akış testleri
│   └── test_unit.py         # Veri çekme fonksiyonu birim testleri
│
├── app.py              # Streamlit Web Arayüzü
├── requirements.txt    # Bağımlılık listesi
└── .gitignore          # Güvenlik (API Key ve .venv gizleme)