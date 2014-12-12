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
    $('#id_cpf').mask('000.000.000-00', {placeholder: '___.___.___-__'});
    $('#id_cep').mask('00000-000', {placeholder: '_____-___'});
    $('#id_tel_fixo').mask('(00) 0000-0000', {placeholder: '(__) ____-____'});
    $('#id_tel_cel').mask('(00) 0000-0000', {placeholder: '(__) ____-____'});
    $('#id_tel_trab').mask('(00) 0000-0000', {placeholder: '(__) ____-____'});
    if ($('#id_multa').get(0)) {
        // se necessario troca '.' por ',' no campo: 'multa'
        multa = $('#id_multa').val();
        if (multa.indexOf('.') != -1) {
            multa = multa.replace('.', ',');
        } else {
            if (multa == '') {
                multa = '0,00';
            } else {
                multa = multa.replace(/$/, ',00');
            }
        }
        // Coloca um zero no fim
        re = /(\,\d)$/;
        multa=multa.replace(re,"$1"+"0");
        // Coloca um zero antes da vírgula
        re = /^(\,\d{2})$/;
        multa=multa.replace(re,"0"+"$1");
        // Coloca um ponto antes dos 5 últimos dígitos
        re = /(\d)(\d{3})\,(\d{2})$/;
        multa=multa.replace(re,"$1.$2,$3");
        $('#id_multa').val(multa);
        $('#id_multa').mask('0.000,00', {placeholder: '0.000,00', reverse: true});
    }
});

$(document).ready(function(){
    if ( $("#id_legend").text() != "Excluir Cliente" ) {
        $("#id_sexo").chosen({
            disable_search: true,
            width: "89%"
        });
        $("#id_uf").chosen({
            no_results_text: "Ops, Estado n&atilde;o encontrado!",
            width: "89%"
        });
    }
    $(".zip-field").blur(function(){
        var arr;
        // validates CEP
        var regex = /^([0-9]{5})[-. ]?([0-9]{3})$/;
        if (regex.test($(".zip-field").val()))
        {
            $.get('/cep/'+$(".zip-field").val()+'/', function(data,status)
            {
                eval("var arr = "+data);
                $("#"+address.street).val(arr.street);
                $("#"+address.district).val(arr.district);
                $("#"+address.city).val(arr.city);
                $("#"+address.state).val(arr.state);
                $("#"+address.state).trigger("chosen:updated");
            });
        }
    });
    $("#p_input").tooltip();
    $("#dialog").dialog({
        autoOpen: false,
        width: 400,
        buttons: [
            {
                text: "Ok",
                click: function(){
                    $("#id_form").submit();
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
    $("#id_form").submit(function(){
        // executa mais um trim no campo nome
        if ($('#id_nome').get(0)) {
            var nome = $('#id_nome').val();
            $('#id_nome').val(trim_js(nome));
        }
        // unmask os campos com mascara que devem perder a mascara
        $('#id_cpf').unmask();
        $('#id_cep').unmask();
        $('#id_tel_fixo').unmask();
        $('#id_tel_cel').unmask();
        $('#id_tel_trab').unmask();
        // se existir o campo multa, entao tira a mascara do campo 'multa'
        // e coloca o caracter '.' no lugar certo do campo 'multa'
        if ($('#id_multa').get(0)) {
            if ($('#id_multa').val().indexOf(',') != -1) {
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
            } else
                $('#id_multa').unmask();
        }
    });
    $("#a_buscar").click(function(){
        $("#id_form").submit();
    });
    $("#a_submit_form").click(function(event){
        $("#dialog").dialog("open");
        event.preventDefault();
    });
    // Hover states on the static widgets
    $( "#a_submit_form, #a_voltar, #a_buscar" ).hover(
        function() {
            $( this ).addClass( "ui-state-hover" );
        },
        function() {
            $( this ).removeClass( "ui-state-hover" );
        }
    );
});
