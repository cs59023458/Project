let ctx = document.getElementById('myChart').getContext('2d');
let labels = ['Protein(cal)', 'Carbohydrate(cal)', 'Fat(cal)'];/* เพิ่มเป็นโปรตีน ไขมัน คาร์โบ */
let colorHex = ['#ff0844', '#21d4fd', '#fee140', ];
let myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      data: [23.9, 46.3, 29.9,], /* ปรับ% ปริมาณได้ */
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: -10,
        borderWidth: 0,
        borderColor: '#fff',
        borderRadius: 25,
      
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '30'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})