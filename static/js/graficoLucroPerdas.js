async function carregarDadosGraficoLucroPerdas() {
    const resposta = await fetch('/grafico-lucro-perdas'); // Supondo que você tenha uma rota que retorne esses dados
    const dados = await resposta.json();

    // Função para formatar os valores com separador de milhar e "K"
    const formatarValor = (valor) => {
        return valor.toLocaleString('pt-BR').replace(',', '.') + 'K';  // Usa o pt-BR para separador de milhar com ponto
    };

    const aprovado = formatarValor(dados.aprovado);
    const reembolsado = formatarValor(dados.reembolsado);
    const recusado = formatarValor(dados.recusado);

    var options = {
        series: [{
            data: [dados.aprovado, dados.reembolsado, dados.recusado], // Dados originais sem formatação para o gráfico
        }],
        chart: {
            type: 'bar',
            height: 380,
            toolbar: {
                show: false // Desabilita o menu de opções
            }
        },
        plotOptions: {
            bar: {
                distributed: true,
                horizontal: false, // Altera para gráfico vertical
                dataLabels: {
                    position: 'center', // Posição das etiquetas de dados no centro das barras
                },
            }
        },
        colors: ['#28a745', '#ffc107', '#dc3545'],
        dataLabels: {
            enabled: true,
            textAnchor: 'middle',
            style: {
                colors: ['#000']
            },
            formatter: function (val) {
                return val.toLocaleString('pt-BR').replace(',', '.') + 'K'; // Formata os valores com separador de milhar e sufixo "K"
            },
            offsetY: -10, // Ajusta a posição vertical das etiquetas
            dropShadow: {
                enabled: false
            }
        },
        stroke: {
            width: 1,
            colors: ['#fff']
        },
        xaxis: {
            categories: ['Aprovado', 'Reembolsado' ,'Recusado'], // Mantém as categorias no eixo x
        },
        yaxis: {
            labels: {
                show: true // Habilita a exibição dos rótulos no eixo y
            }
        },
        title: {
            text: 'Faturamento e Perdas',
            align: 'center',
            floating: true
        },
        subtitle: {
            text: '',
            align: 'center',
        },
        tooltip: {
            theme: 'dark',
            x: {
                show: true
            },
            y: {
                title: {
                    formatter: function () {
                        return ''
                    }
                }
            }
        },
        legend: {
            show: false // Desabilita a legenda para evitar duplicação dos rótulos
        }
    };

    var chart = new ApexCharts(document.querySelector("#chartLucroPerdas"), options);
    chart.render();
}

carregarDadosGraficoLucroPerdas();
