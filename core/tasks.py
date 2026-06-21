class FinancialCrewTasks:
    def research_task(self, agent_info, ticker, stock_data):
        return f"""
        Rolün: {agent_info['role']}
        Görevin: {ticker} hissesini şu verilere göre analiz et: {stock_data}
        """

    def recommendation_task(self, agent_info, research_result):
        return f"""
        Rolün: {agent_info['role']}
        Görevin: Şu analiz sonuçlarını birleştirerek kurumsal bir Türkçe yatırım raporu hazırla:
        {research_result}
        """