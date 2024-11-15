let search = '';
let limit = 10;
let offset = 0;

const textoBusca = document.getElementById('textoBusca');

let debounceTimer;
function fetchPaginatedData() {
    fetch(`/table-autocomplite?search=${encodeURIComponent(search)}&limit=${limit}&offset=${offset}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            renderTable(data);  
            togglePrevButton();
        })
        .catch(error => {
            console.error("Erro ao buscar dados:", error);
        });
}

// Lida com a digitação do usuário, realizando busca com debounce
textoBusca.addEventListener('input', (event) => {
    search = event.target.value.trim();

    // Só faz a requisição se o texto for maior ou igual a 2 caracteres
    if (search.length >= 2) {
        clearTimeout(debounceTimer);  // Limpa o timer anterior, caso o usuário continue digitando
        debounceTimer = setTimeout(() => {
            fetchPaginatedData();  // Chama a função após um atraso (debounce)
        }, 300);  // Atraso de 300ms
    }
});

// Navegação para a próxima página
function nextPage() {
    offset += limit;
    fetchPaginatedData();
}


function prevPage() {
    if (offset >= limit) {  // Impede que o offset seja negativo
        offset -= limit;
        fetchPaginatedData();
    }
}

// Controla a habilitação do botão "Anterior"
function togglePrevButton() {
    const prevButton = document.querySelector("#prev-button");
    prevButton.disabled = (offset === 0);  // Desabilita o botão se o offset for 0
}


function renderTable(data) {
    const tableBody = document.querySelector("#table-body");
    tableBody.innerHTML = "";  // Limpa os dados anteriores
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


document.querySelector("#next-button").addEventListener("click", nextPage);
document.querySelector("#prev-button").addEventListener("click", prevPage);
fetchPaginatedData();
