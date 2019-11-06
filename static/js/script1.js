function chartrun(pro, car, fat) {
  const ctx = document.getElementById('myChart').getContext('2d');
  const labels = ['Protein(cal)', 'Carbohydrate(cal)', 'Fat(cal)'];/* เพิ่มเป็นโปรตีน ไขมัน คาร์โบ */
  const colorHex = ['#4facfe', '#43e97b', '#fee140'];

  const myChart = new Chart(ctx, {
    type: 'pie',
    data: {
      datasets: [{
        data: [pro, car, fat], /* ปรับ% ปริมาณได้ */
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
}