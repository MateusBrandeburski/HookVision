

var options = {
    series: [44, 55, 41],
    chart: {
    type: 'donut',
  },
  responsive: [{
    breakpoint: 480,
    options: {
      chart: {
        width: 20
      },
      legend: {
        position: 'bottom'
      }
    }
  }]
  };

var chart = new ApexCharts(document.querySelector("#graficoPagamentos"), options);
chart.render();