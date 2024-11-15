from classes.database.database import Pagamentos
from sqlalchemy import func, extract
from datetime import timedelta, datetime

class Tabela:
    
    @staticmethod
    def tabela_paginada(limit, offset):
        pagamentos = (
            Pagamentos.query
            .limit(limit)
            .offset(offset)
            .all()
        )

        dados = [{
                "nome": pagamento.nome,
                "email": pagamento.email,
                "status": pagamento.status,
                "status_no_sistema": pagamento.status_no_sistema,
                "valor": pagamento.valor,
                "forma_pagamento": pagamento.forma_pagamento,
                "parcelas": pagamento.parcelas,
                "data": pagamento.data
                  } for pagamento in pagamentos]
        
        return dados
        
    
    @staticmethod
    def total_base():
        pass
    
    
    @staticmethod
    def search_auto_complite(ilike):
        pass
    
    
    @staticmethod
    def total_ultimos_30_dias():
        pass
    