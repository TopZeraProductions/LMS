$(document).ready(function(){

    $( "#btnSend" ).click(function() {
        vNome  = document.getElementById('txtNome').value;
        vCarga = document.getElementById('txtCarga').value;
        vCurso = document.getElementById('slcCurso').value;

        var data = {
            csrfmiddlewaretoken : "cXZbbxLehyr7Hvehy0DWpwsliaLQqyL3yw0VX2vcUekLDGlXIhfOO8NtnRhgohq7"
            , nome :   vNome
            , carga_horaria : vCarga
            , curso : vCurso
        }

        $.post(
            '/disciplina/cadastro/'
            , data,
            function(response, status){
                if(status == "success"){
                    alert('Cadastrado com sucesso');
                    window.location = "/disciplina/listagem/";

                }else{
                    alert('Alguma coisa deu errado');
                }
            }
        );
    });
});
