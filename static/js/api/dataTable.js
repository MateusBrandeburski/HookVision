let limit = 10; // Valor padrão
let offset = 0; // Inicialmente começa em 0

// Função para buscar os dados paginados
function fetchPaginatedData() {
    fetch(`/table?limit=${limit}&offset=${offset}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // Exibe os dados no console (ou pode ser usado para renderizar na página)
            renderTable(data); // Função para exibir os dados na tabela (se necessário)
        })
        .catch(error => {
            console.error("Erro ao buscar dados:", error);
        });
}

// Função para avançar para a próxima página
function nextPage() {
    offset += limit; // Incrementa o offset pelo valor do limit
    fetchPaginatedData(); // Busca os dados da nova página
}

// Função para voltar à página anterior
function prevPage() {
    if (offset >= limit) { // Impede que o offset seja negativo
        offset -= limit; // Decrementa o offset pelo valor do limit
        fetchPaginatedData(); // Busca os dados da página anterior
    }
}

// Função para renderizar os dados em uma tabela (opcional)
function renderTable(data) {
    const tableBody = document.querySelector("#table-body"); // Alvo da tabela no HTML
    tableBody.innerHTML = ""; // Limpa os dados anteriores
    data.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.nome}</td>
            <td>${item.email}</td>
            <td>${item.status}</td>
            <td>${item.status_no_sistema}</td>
            <td>${item.valor}</td>
            <td>${item.forma_pagamento}</td>
            <td>${item.parcelas}</td>
            <td>${item.data}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Adiciona os eventos aos botões "Próximo" e "Anterior"
document.querySelector("#next-button").addEventListener("click", nextPage);
document.querySelector("#prev-button").addEventListener("click", prevPage);

// Busca inicial ao carregar a página
fetchPaginatedData();
