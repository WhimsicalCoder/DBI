<!DOCTYPE html>
<html>
<head>
    <title>Campaign Tool</title>
    <style>
        /* Add some basic styling */
        body {
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Campaign Tool</h1>
        <label for="campaignName">Campaign Name:</label>
        <input type="text" id="campaignName" placeholder="Campaign Name">

        <label for="totalBudget">Total Budget ($):</label>
        <input type="number" id="totalBudget" placeholder="Total Budget">

        <label for="bookedImpressions">Booked Impressions:</label>
        <input type="number" id="bookedImpressions" placeholder="Booked Impressions">

        <label for="startDate">Start Date:</label>
        <input type="date" id="startDate">

        <label for="endDate">End Date:</label>
        <input type="date" id="endDate">

        <button id="calculateCPM">Calculate CPM</button>

        <div id="result"></div>
    </div>

    <script>
        document.getElementById('calculateCPM').addEventListener('click', function() {
            const campaignName = document.getElementById('campaignName').value;
            const totalBudget = parseFloat(document.getElementById('totalBudget').value);
            const bookedImpressions = parseFloat(document.getElementById('bookedImpressions').value);
            const startDate = new Date(document.getElementById('startDate').value);
            const endDate = new Date(document.getElementById('endDate').value);

            if (!campaignName || isNaN(totalBudget) || isNaN(bookedImpressions) || isNaN(startDate) || isNaN(endDate)) {
                alert('Please fill in all the fields with valid data.');
                return;
            }

            const cpm = (totalBudget / bookedImpressions) * 1000;

            const resultContainer = document.getElementById('result');
            resultContainer.innerHTML = `
                <p>Campaign Name: ${campaignName}</p>
                <p>Cost Per Mille (CPM): $${cpm.toFixed(2)}</p>
            `;
        });
    </script>
</body>
</html>
