import pytest
from core.tools import fetch_stock_data

def test_fetch_stock_data_with_valid_ticker():
    """Valid (geçerli) bir hisse kodu girildiğinde aracın düzgün veri getirdiğini test eder."""
    # Apple hissesi (AAPL) ile aracı test ediyoruz
    result = fetch_stock_data._run(ticker="AAPL")
    
    assert "AAPL HİSSE FİNANSAL ÖZETİ" in result
    assert "Şirket Adı" in result
    assert "Güncel Fiyat" in result
    assert "F/K Oranı" in result

def test_fetch_stock_data_with_invalid_ticker():
    """Geçersiz bir hisse kodu girildiğinde sistemin çökmediğini, hata mesajı döndürdüğünü test eder."""
    # Rastgele geçersiz bir kod veriyoruz
    result = fetch_stock_data._run(ticker="INVALIDXYZ123")
    
    # yfinance geçersiz kodlarda boş veri döner veya hata mesajı tetikler, sistemin ayakta kaldığını doğrulamalıyız
    assert "HİSSE FİNANSAL ÖZETİ" in result or "hata" in result.lower()