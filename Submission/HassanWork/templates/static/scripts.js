document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filter-form');
    const dataTableBody = document.getElementById('data-table').querySelector('tbody');

    filterForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const year = document.getElementById('year').value;
        const month = document.getElementById('month').value;

        fetch(`/data?year=${year}&month=${month}`)
            .then(response => response.json())
            .then(data => {
                // Clear existing table rows
                dataTableBody.innerHTML = '';

                // Insert new rows
                data.forEach(row => {
                    const tr = document.createElement('tr');
                    Object.values(row).forEach(value => {
                        const td = document.createElement('td');
                        td.textContent = value;
                        tr.appendChild(td);
                    });
                    dataTableBody.appendChild(tr);
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    });
});
