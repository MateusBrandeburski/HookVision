from classes.database.database import Pagamentos
from sqlalchemy import func

class Graficos:
    
    @staticmethod
    def grafico_status():
        reembolsado = Pagamentos.query.filter_by(status="reembolsado").count()
        aprovado = Pagamentos.query.filter_by(status="aprovado").count()
        recusado = Pagamentos.query.filter_by(status="recusado").count()
        
        resultado = {
            "reembolsado": reembolsado,
            "aprovado": aprovado,
            "recusado": recusado
        }
        return resultado
    
    @staticmethod
    def grafico_total():
        result = Pagamentos.query.with_entities(
            func.date(func.to_timestamp(Pagamentos.data, 'DD/MM/YYYY HH24:MI')).label('data'),
            func.count(Pagamentos.id).label('quantidade_transacoes')
        ).group_by(func.date(func.to_timestamp(Pagamentos.data, 'DD/MM/YYYY HH24:MI'))).all() 
        
        resultado = []
        
        for row in result:
            data_formatada = row.data.strftime('%Y-%m-%d') 
            resultado.append({
                "data": data_formatada,
                "total": row.quantidade_transacoes
            })
        
        return resultado
        
        
    
    

    