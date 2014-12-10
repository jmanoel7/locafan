/*
function mascara(o,f){
    v_obj=o;
    v_fun=f;
    setTimeout("exec_mascara()",1);
}

function exec_mascara(){
    v_obj.value=v_fun(v_obj.value);
}

function mascara_nome(v){
    // Retira tudo o que nao eh letra do campo nome
    re = /[^A-Za-zÁÀÄÃÂÉÈËẼÊÍÌÏĨÎÓÒÖÕÔÚÙÜŨÛÝỲŸỸŶẂẀẄŴÇáàäãâéèëẽêíìïĩîóòöõôúùüũûýỳÿỹŷẃẁẅŵç ]/g;
    v=v.replace(re,"");
    return v;
}

function trim_js(str){
    //Remove todos os espacos em branco do inicio
    re = /^ +/;
    str=str.replace(re,"");
    //Remove todos os espacos em branco do fim
    re = / +$/;
    str=str.replace(re,"");
    //Troca um ou mais espacos por um espaco
    re = / +/g;
    str=str.replace(re," ");
    return str;
}
*/
$(function(){
    $('#id_qtde_disponivel').mask('00', {placeholder: '00'});
    $('#id_qtde_total').mask('00', {placeholder: '00'});
    $('#id_valor_fantasia').mask('000.000,00', {placeholder: '000.000,00', reverse: true});
    $('#id_valor_locacao').mask('000.000,00', {placeholder: '000.000,00', reverse: true});
});

$(document).ready(function(){
    if ( $("#id_legend").text() != "Excluir Fantasia" ) {
        $("#id_tipo").chosen({
            disable_search: true,
            width: "89%"
        });
    }
    $("#p_input").tooltip();
    $("#dialog").dialog({
        autoOpen: false,
        width: 400,
        buttons: [
            {
                text: "Ok",
                click: function(){
                    $("form").submit();
                    $(this).dialog("close");
                }
            },
            {
                text: "Cancelar",
                click: function(){
                    $(this).dialog("close");
                }
            }
        ]
    });
    $("form").submit(function(){
        // unmask os campos com mascara que devem perder a mascara
        $('#id_qtde_disponivel').unmask();
        $('#id_qtde_total').unmask();
        // tirar a mascara e coloca o caracter '.'
        // no lugar certo do campo 'valor_fantasia'
        if ($('#id_valor_fantasia').val().indexOf(',') != -1) {
            $('#id_valor_fantasia').unmask();
            var valor_fantasia = $('#id_valor_fantasia').val();
            var temp = valor_fantasia.split("");
            temp[temp.length]   = temp[temp.length-1];
            temp[temp.length-2] = temp[temp.length-3];
            temp[temp.length-3] = ".";
            var i=0;
            valor_fantasia="";
            for ( i=0; i < temp.length; i++) {
                valor_fantasia = valor_fantasia + temp[i];
            }
            $('#id_valor_fantasia').val(valor_fantasia);
        } else
            $('#id_valor_fantasia').unmask();
        // tirar a mascara e coloca o caracter '.'
        // no lugar certo do campo 'valor_locacao'
        if ($('#id_valor_locacao').val().indexOf(',') != -1) {
            $('#id_valor_locacao').unmask();
            var valor_locacao = $('#id_valor_locacao').val();
            var temp = valor_locacao.split("");
            temp[temp.length]   = temp[temp.length-1];
            temp[temp.length-2] = temp[temp.length-3];
            temp[temp.length-3] = ".";
            var i=0;
            valor_locacao="";
            for ( i=0; i < temp.length; i++) {
                valor_locacao = valor_locacao + temp[i];
            }
            $('#id_valor_locacao').val(valor_locacao);
        } else
            $('#id_valor_locacao').unmask();
    });
    $("#id_submit_form").click(function(event){
	  $("#dialog").dialog("open");
      event.preventDefault();
    });
    // Hover states on the static widgets
    $( "#id_submit_form" ).hover(
        function() {
            $( this ).addClass( "ui-state-hover" );
        }
    );
});
