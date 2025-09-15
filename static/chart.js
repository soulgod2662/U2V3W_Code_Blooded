document.addEventListener("DOMContentLoaded", function () {
    const matchedCount = parseInt(document.getElementById("matchedCount").textContent);
    const missingCount = parseInt(document.getElementById("missingCount").textContent);

    const ctx = document.getElementById('skillChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Matched Skills', 'Missing Skills'],
            datasets: [{
                data: [matchedCount, missingCount],
                backgroundColor: ['#28a745', '#dc3545']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
});