function add_carro(){
    let container = document.getElementById("form-carro")
    let html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div><div class='col-md'><input type='text' placeholder='placa' class='form-control' name='placa'></div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'> </div></div>"
    document.getElementById("form-carro").innerHTML += html
}