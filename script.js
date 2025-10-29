function loadMateri(algoritma) {
    const contentArea = document.getElementById('content-area');
    contentArea.innerHTML = '<h2>Memuat...</h2>'; 

    fetch(`/api/materi/${algoritma}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Gagal memuat data dari backend.');
            }
            return response.json();
        })
        .then(data => {
            let htmlContent = '<h3><span style="color: #007BFF;">♦</span> ' + data.judul + '</h3>'; // Icon diamond
            
            htmlContent += '<h4>Pengertian:</h4>';
            htmlContent += `<p>${data.pengertian}</p>`;

            htmlContent += '<h4>Kelebihan:</h4><ul>';
            data.kelebihan.forEach(item => {
                htmlContent += `<li>${item}</li>`;
            });
            htmlContent += '</ul>';

            htmlContent += '<h4>Kekurangan:</h4><ul>';
            data.kekurangan.forEach(item => {
                htmlContent += `<li>${item}</li>`;
            });
            htmlContent += '</ul>';

            contentArea.innerHTML = htmlContent;

            updateActiveButton(algoritma);
        })
        .catch(error => {
            console.error('Error:', error);
            contentArea.innerHTML = `<h2>Error</h2><p>Gagal memuat data algoritma.</p>`;
        });
}

function updateActiveButton(activeAlgoritma) {
    const buttons = document.querySelectorAll('.alg-button');
    buttons.forEach(button => {
        button.classList.remove('active-alg');
        if (button.textContent.toLowerCase().includes(activeAlgoritma.replace('fuzzy', 'fuzzy'))) {
            button.classList.add('active-alg');
        }
    });
}
