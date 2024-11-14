
async function carregarDadosDoGrafico() {

  const resposta = await fetch('/grafico-status');
  const dados = await resposta.json();


  const options = {
    series: [dados.aprovado, dados.reembolsado, dados.recusado],
    chart: {
    width: 380,
    type: 'pie',
    },
    labels: ['Aprovado', 'Reembolsado', 'Recusado'],
    colors: ['#28a745', '#ffc107', '#dc3545'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var chart = new ApexCharts(document.querySelector("#chart-status"), options);
  chart.render();

};

carregarDadosDoGrafico();
