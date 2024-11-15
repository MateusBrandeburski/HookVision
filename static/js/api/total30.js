
async function total30() {
    const resposta = await fetch('/grafico-total30');
    const dados = await resposta.json();
    const elemento = document.getElementById('total30');

    elemento.textContent = `${dados.total}`;
}

total30();