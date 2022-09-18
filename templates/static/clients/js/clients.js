function add_carro(){
    let container = document.getElementById("form-carro")
    let html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div><div class='col-md'><input type='text' placeholder='placa' class='form-control' name='placa'></div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'> </div></div>"
    document.getElementById("form-carro").innerHTML += html
}

function exibir_form(tipo) {
    let add_cliente = document.getElementById('adicionar-cliente');
    let att_cliente = document.getElementById('att_cliente');
    if (tipo === '1') {
        att_cliente.style.display = 'none';
        add_cliente.style.display = 'block';
    }
    else if ( tipo === '2') {
        att_cliente.style.display = 'block';
        add_cliente.style.display = 'none';
    }
}

function dados_cliente() {
    let cliente = document.getElementById('cliente-select')
    let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    let id_cliente = cliente.value
    let data = new FormData();
    data.append('id_cliente', id_cliente)
    fetch("/clients/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: data
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        document.getElementById('form-att-cliente').style.display = 'block';
        let nome = document.getElementById('nome')
        nome.value = data['nome']
        let sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['sobrenome']
        let cpf = document.getElementById('cpf')
        cpf.value = data['cpf']
        let email = document.getElementById('email')
        email.value = data['email']
    })
}