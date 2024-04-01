// Função para abrir o modal
function openModal(modalName) {
    var modal = document.getElementById(modalName);
    modal.style.display = "block";
    if (modalName == 'signupModal'){
        document.getElementById("closeLoginModal").click()
    }
}

// Função para fechar o modal
function closeModal(modalName) {
    var modal = document.getElementById(modalName);
    modal.style.display = "none";
}

// Fechar o modal ao clicar fora dele
window.onclick = function(event) {
    var modal = document.getElementById("loginModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }

    var modal = document.getElementById("signupModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

//Login
document.getElementById("idLoginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    
    // Obtém os dados do formulário de login
    var formData = new FormData(document.getElementById("idLoginForm"));
    
    // Envia uma solicitação AJAX para o backend para realizar o login
    fetch("{% url 'login' %}", {
        method: "POST",
        body: formData,
        headers: {
        "X-CSRFToken": "{{ csrf_token }}" // Adicione isso se estiver usando CSRF protection
        }
    })
    .then(response => {
        if (response.ok) {
        // Login bem-sucedido, execute a ação desejada (por exemplo, atualizar a página)
        location.reload();
        } else {
        // Login falhou, exiba uma mensagem de erro ao usuário
        alert("Login falhou. Verifique suas credenciais.");
        }
    })
    .catch(error => {
        console.error("Erro ao enviar solicitação de login:", error);
    });
});

//Cadastro
document.getElementById("idsignupForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    
    // Obtém os dados do formulário de login
    var formData = new FormData(document.getElementById("idsignupForm"));
    
    // Envia uma solicitação AJAX para o backend para realizar o login
    fetch("{% url 'signup' %}", {
        method: "POST",
        body: formData,
        headers: {
        "X-CSRFToken": "{{ csrf_token }}" // Adicione isso se estiver usando CSRF protection
        }
    })
    .then(response => {
        if (response.ok) {
        // Login bem-sucedido, execute a ação desejada (por exemplo, atualizar a página)
        location.reload();
        } else {
        // Login falhou, exiba uma mensagem de erro ao usuário
        alert("Login falhou. Verifique suas credenciais.");
        }
    })
    .catch(error => {
        console.error("Erro ao enviar solicitação de login:", error);
    });
});

