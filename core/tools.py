import yfinance as yf

def fetch_stock_data(ticker: str) -> str:
    """Verilen hisse kodu için Yahoo Finance üzerinden temel finansal verileri çeker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        fk = info.get('trailingPE', 'N/A')
        fiyat = info.get('currentPrice', 'N/A')
        market_cap = info.get('marketCap', 'N/A')
        
        return f"Güncel Fiyat: {fiyat}, F/K Oranı: {fk}, Piyasa Değeri: {market_cap}"
    except Exception as e:
        return f"Veri çekme hatası: {str(e)}"