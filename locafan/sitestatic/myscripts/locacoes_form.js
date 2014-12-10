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

$(function(){
    $('#id_dt_nascimento').mask('00/00/0000', {placeholder: 'dd/mm/aaaa'});
    //$('#id_dt_nascimento').mask('00/00/0000');
    $('#id_cpf').mask('000.000.000-00', {placeholder: '___.___.___-__'});
    $('#id_cep').mask('00000-000', {placeholder: '_____-___'});
    $('#id_tel_fixo').mask('(00) 0000-0000', {placeholder: '(__) ____-____'});
    $('#id_tel_cel').mask('(00) 0000-0000', {placeholder: '(__) ____-____'});
    $('#id_tel_trab').mask('(00) 0000-0000', {placeholder: '(__) ____-____'});
    if ($('#id_multa').get(0))
        $('#id_multa').mask('000000,00', {placeholder: '0000,00', reverse: true});
});
*/

$(document).ready(function(){
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
        // executa mais um trim no campo nome
        //var nome = $('#id_nome').val();
        //$('#id_nome').val(trim_js(nome));
        /* unmask os campos com mascara que devem perder a mascara
        $('#id_cpf').unmask();
        $('#id_cep').unmask();
        $('#id_tel_fixo').unmask();
        $('#id_tel_cel').unmask();
        $('#id_tel_trab').unmask();*/
        // tira a mascara do campo multa e coloca o caracter '.' no lugar certo de seu valor
        /*if ($('#id_multa').get(0)) {
            $('#id_multa').unmask();
            var multa = $('#id_multa').val();
            var temp = multa.split("");
            temp[temp.length]   = temp[temp.length-1];
            temp[temp.length-2] = temp[temp.length-3];
            temp[temp.length-3] = ".";
            var i=0;
            multa="";
            for ( i=0; i < temp.length; i++) {
                multa = multa + temp[i];
            }
            $('#id_multa').val(multa);
        }*/
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
