let ctx = document.getElementById('myChart').getContext('2d');
let labels = ['โปรตีน', 'คาร์โบไฮเดรต', 'ไข่มัน'];/* เพิ่มเป็นโปรตีน ไขมัน คาร์โบ */
let colorHex = ['#EFCA08','#43AA8B','#FB3640'];

let myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      data: [30, 10, 40], /* ปรับ% ปริมาณได้ */
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
          size: '10'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})