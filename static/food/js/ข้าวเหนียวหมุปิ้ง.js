let ctx = document.getElementById('myChart').getContext('2d');
let labels = ['Proteub🍖(cal)', 'Carb🌽(cal)', 'Fat🍟(cal)'];/* เพิ่มเป็นโปรตีน ไขมัน คาร์โบ */
let colorHex = ['#4facfe', '#43e97b', '#fee140', ];

let myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      data: [17.8,30.5,51.7,], /* ปรับ% ปริมาณได้ */
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
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 25,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '18'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})