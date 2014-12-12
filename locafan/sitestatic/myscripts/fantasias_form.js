$(function(){
    // poe a mascara no campo: 'qtde_disponivel'
    if ($('#id_qtde_disponivel').get(0)) {
        qtde_disponivel = $('#id_qtde_disponivel').val();
        if (qtde_disponivel.search(/^\d$/) == 0) {
            qtde_disponivel = qtde_disponivel.replace(/^/, '0');
        } else if (qtde_disponivel == '') {
            qtde_disponivel = '01';
        }
        $('#id_qtde_disponivel').val(qtde_disponivel);
        $('#id_qtde_disponivel').mask('00', {placeholder: '00'});
    }
    // poe a mascara no campo: 'qtde_total'
    if ($('#id_qtde_total').get(0)) {
        qtde_total = $('#id_qtde_total').val();
        if (qtde_total.search(/^\d$/) == 0) {
            qtde_total = qtde_total.replace(/^/, '0');
        } else if (qtde_total == '') {
            qtde_total = '01';
        }
        $('#id_qtde_total').val(qtde_total);
        $('#id_qtde_total').mask('00', {placeholder: '00'});
    }
    // poe a mascara no campo: 'valor_fantasia'
    if ($('#id_valor_fantasia').get(0)) {
        valor_fantasia = $('#id_valor_fantasia').val();
        if (valor_fantasia.indexOf('.') != -1) {
            valor_fantasia = valor_fantasia.replace('.', ',');
        } else {
            if (valor_fantasia == '') {
                valor_fantasia = '300,00';
            } else {
                valor_fantasia = valor_fantasia.replace(/$/, ',00');
            }
        }
        // Coloca um zero no fim
        re = /(\,\d)$/;
        valor_fantasia=valor_fantasia.replace(re,"$1"+"0");
        // Coloca um zero antes da vírgula
        re = /^(\,\d{2})$/;
        valor_fantasia=valor_fantasia.replace(re,"0"+"$1");
        // Coloca um ponto antes dos 5 últimos dígitos
        re = /(\d)(\d{3})\,(\d{2})$/;
        valor_fantasia=valor_fantasia.replace(re,"$1.$2,$3");
        $('#id_valor_fantasia').val(valor_fantasia);
        $('#id_valor_fantasia').mask('0.000,00', {placeholder: '0.000,00', reverse: true});
    }
    // poe a mascara no campo: 'valor_locacao'
    if ($('#id_valor_locacao').get(0)) {
        valor_locacao = $('#id_valor_locacao').val();
        if (valor_locacao.indexOf('.') != -1) {
            valor_locacao = valor_locacao.replace('.', ',');
        } else {
            if (valor_locacao == '') {
                valor_locacao = '3,00';
            } else {
                valor_locacao = valor_locacao.replace(/$/, ',00');
            }
        }
        // Coloca um zero no fim
        re = /(\,\d)$/;
        valor_locacao=valor_locacao.replace(re,"$1"+"0");
        // Coloca um zero antes da vírgula
        re = /^(\,\d{2})$/;
        valor_locacao=valor_locacao.replace(re,"0"+"$1");
        // Coloca um ponto antes dos 5 últimos dígitos
        re = /(\d)(\d{3})\,(\d{2})$/;
        valor_locacao=valor_locacao.replace(re,"$1.$2,$3");
        $('#id_valor_locacao').val(valor_locacao);
        $('#id_valor_locacao').mask('0.000,00', {placeholder: '0.000,00', reverse: true});
    }
});

$(document).ready(function(){
    if ( $("#id_legend").text() == "Cadastrar Fantasia" || $("#id_legend").text() == "Buscar Fantasia pelo Tipo" ) {
        $("#id_tipo").chosen({
            disable_search: true,
            width: "75%"
        });
    } else if ($("#id_legend").text() == "Excluir Fantasia" || $("#id_legend").text() == "Editar Fantasia") {
        switch($('#id_tipo').val()) {
            case 'IM':
                $('#id_tipo').val('Infantil Masculino');
                break;
            case 'IF':
                $('#id_tipo').val('Infantil Feminino');
                break;
            case 'AM':
                $('#id_tipo').val('Adulto Masculino');
                break;
            case 'AF':
                $('#id_tipo').val('Adulto Feminino');
                break;
            case 'CS':
                $('#id_tipo').val('Casal');
                break;
        }
    }
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
        // unmask os campos com mascara que devem perder a mascara
        if ($('#id_qtde_disponivel').get(0)) {
            $('#id_qtde_disponivel').unmask();
        }
        if ($('#id_qtde_total').get(0)) {
            $('#id_qtde_total').unmask();
        }
        // tirar a mascara e coloca o caracter '.'
        // no lugar certo do campo 'valor_fantasia'
        if ($('#id_valor_fantasia').get(0)) {
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
            } else {
                $('#id_valor_fantasia').unmask();
            }
        }
        // tirar a mascara e coloca o caracter '.'
        // no lugar certo do campo 'valor_locacao'
        if ($('#id_valor_locacao').get(0)) {
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
            } else {
                $('#id_valor_locacao').unmask();
            }
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
