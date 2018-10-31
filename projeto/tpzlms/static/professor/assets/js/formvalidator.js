$(document).ready(function(){

    $( "#btnSend" ).click(function() {
        vNome  = document.getElementById('txtNome').value;
        vCpf = document.getElementById('txtCPF').value;
        vRg = document.getElementById('txtRG').value;
        vCep = document.getElementById('txtCEP').value;
        vEndereco = document.getElementById('txtEndereco').value;
        vCidade = document.getElementById('txtCidade').value;
        vUf = document.getElementById('txtUF').value;


        var data = {
            csrfmiddlewaretoken : "cXZbbxLehyr7Hvehy0DWpwsliaLQqyL3yw0VX2vcUekLDGlXIhfOO8NtnRhgohq7"
            , nome :   vNome
            , cpf : vCpf
            , rg : vRg
            , cep : vCep
            , endereco : vEndereco
            , cidade : vCidade
            , uf : vUf
        }

        $.post(
            '/professor/cadastro/'
            , data,
            function(response, status){
                if(status == "success"){
                    alert('Cadastrado com sucesso');
                    window.location = "/professor/listagem/";

                }else{
                    alert('Alguma coisa deu errado');
                }
            }
        );
    });
});
