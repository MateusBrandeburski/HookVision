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
    def search_auto_complite(search_term, limit, offset):
        search_term = f"%{search_term.lower()}%"
        
        result = Pagamentos.query.filter(
            func.lower(Pagamentos.nome).ilike(search_term) |
            func.lower(Pagamentos.email).ilike(search_term) |
            func.lower(Pagamentos.status).ilike(search_term) |
            func.lower(Pagamentos.status_no_sistema).ilike(search_term) |
            func.lower(Pagamentos.forma_pagamento).ilike(search_term) |
            func.lower(Pagamentos.parcelas).ilike(search_term) |
            func.lower(Pagamentos.data).ilike(search_term)
        ).execution_options(no_use_bindparams=True).limit(limit).offset(offset).all()

        dados = [{
            "nome": r.nome,
            "email": r.email,
            "status": r.status,
            "status_no_sistema": r.status_no_sistema,
            "valor": r.valor,
            "forma_pagamento": r.forma_pagamento,
            "parcelas": r.parcelas,
            "data": r.data
        } for r in result]

        return dados
    
    
    @staticmethod
    def total_ultimos_30_dias():
        pass
    