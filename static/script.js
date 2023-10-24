// static/script.js
document.addEventListener('DOMContentLoaded', function () {
    const configForm = document.getElementById('config-form');
    const resultDiv = document.getElementById('result-div');
    const statusButton = document.getElementById('status-button');
    const healthStatus = document.getElementById('health-status');

    configForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const websiteURL = document.getElementById('website-url').value;
        const healthCheckPeriod = document.getElementById('health-check-period').value;

        fetch('/check_health', {
            method: 'POST',
            body: new URLSearchParams({ website_url: websiteURL, health_check_period: healthCheckPeriod }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }).then(() => {
            window.location.reload();
        });
    });

    function updateHealthStatus() {
        fetch('/get_health_status').then(response => response.json()).then(data => {
            if (data.status === '200') {
                statusButton.style.backgroundColor = 'green';
            } else {
                statusButton.style.backgroundColor = 'red';
            }
            healthStatus.textContent = data.status;
        });
    }

    statusButton.addEventListener('click', function () {
        updateHealthStatus();
    });

    setInterval(updateHealthStatus, {{ health_check_period }} * 1000);
});
