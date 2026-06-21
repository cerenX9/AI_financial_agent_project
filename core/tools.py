import yfinance as ticker_source
from crewai_tools import SerperDevTool
from langchain.tools import tool

# 1. ARAÇ: Google aramaları yapmak için Serper API aracı
search_tool = SerperDevTool()

# 2. ARAÇ: Yahoo Finance'ten hisse verisi çeken özel fonksiyonumuz
@tool("Fetch Financial Stock Data")
def fetch_stock_data(ticker: str) -> str:
    """
    Belirtilen hisse kodunun (Örn: AAPL, TSLA, THYAO.IS) güncel fiyat, 
    piyasa değeri, F/K oranı ve bilanço özetini getirir.
    """
    try:
        stock = ticker_source.Ticker(ticker)
        info = stock.info
        
        summary = f"""
        --- {ticker} HİSSE FİNANSAL ÖZETİ ---
        Şirket Adı: {info.get('longName', 'Bilinmiyor')}
        Sektör: {info.get('sector', 'Bilinmiyor')}
        Güncel Fiyat: {info.get('currentPrice', 'Bilinmiyor')} {info.get('currency', '')}
        Piyasa Değeri: {info.get('marketCap', 'Bilinmiyor')}
        F/K Oranı (PE Ratio): {info.get('trailingPE', 'Bilinmiyor')}
        Temettü Verimi: {info.get('dividendYield', 'Bilinmiyor')}
        52 Haftalık En Yüksek/En Düşük: {info.get('fiftyTwoWeekHigh', '')} / {info.get('fiftyTwoWeekLow', '')}
        """
        return summary
    except Exception as e:
        return f"Finansal veriler çekilirken hata oluştu: {str(e)}"