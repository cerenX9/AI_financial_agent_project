import pytest
from core.tools import fetch_stock_data

def test_fetch_stock_data():
    # Apple (AAPL) hissesi için veri çekmeyi test ediyoruz
    data = fetch_stock_data("AAPL")
    
    assert data is not None
    assert "Güncel Fiyat" in data
    assert "F/K Oranı" in data