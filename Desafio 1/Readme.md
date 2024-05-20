# Formulário 

Este é um exemplo de um formulário HTML que utiliza um "repeater" para adicionar dinamicamente campos de participantes. O formulário permite que os usuários insiram seus emails e percentuais de participação.

## Estrutura do Formulário

O formulário consiste em:

1. Um campo de email.
2. Um campo de percentual.
3. Um botão para adicionar mais participantes (repetir o campo).
4. Um botão para enviar o formulário.

## Funcionalidades

- **Adicionar Participante**: Clique no botão "+ Adicionar Participante" para criar um novo campo de participante.
- **Remover Participante**: Cada campo de participante possui um botão "X" que permite removê-lo.
- **Validações**:
    - O formato do email é validado usando uma expressão regular.
    - A soma dos percentuais é verificada para garantir que seja igual a 100%.

## CSS (styles.css)

O arquivo `styles.css` contém estilos para o formulário, como a formatação do contêiner e dos campos.

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    background-color: #f5f5f5;
}

.container {
    width: 80%;
    max-width: 600px;
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.repeater-item {
    margin-bottom: 10px;
}
```

# JavaScript (index.html)
O código JavaScript no arquivo index.html adiciona a funcionalidade de adicionar e remover participantes dinamicamente.

```JavaScript
// index.html

// Obtém a referência ao formulário
const repeaterForm = document.getElementById('repeaterForm');

// Obtém a referência ao contêiner de repetição
const repeaterContainer = document.getElementById('repeaterContainer');

// Função para adicionar um novo item de participante
function addItem() {
    const newItem = document.createElement('div');
    newItem.className = 'repeater-item';
    newItem.innerHTML = `
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <label for="percentual">Percentual:</label>
        <input type="text" name="percentual">
        <span>%</span>
        <button type="button" onclick="removeItem(this)">X</button>
    `;
    repeaterContainer.appendChild(newItem);
}

// Função para remover um item de participante
function removeItem(button) {
    button.parentElement.remove();
}

// Event listener para o envio do formulário
repeaterForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const emails = Array.from(document.querySelectorAll('input[name="email"]'));
    const participations = Array.from(document.querySelectorAll('input[name="percentual"]'));

    const data = {
        "email": emails.map(email => email.value),
        "percentual": participations.map(part => parseFloat(part.value))
    };

    // Implemente suas validações aqui
});
