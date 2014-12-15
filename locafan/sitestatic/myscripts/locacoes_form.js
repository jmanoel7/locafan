$(function(){
    $('#id_dt_locacao').mask('00/00/0000', {placeholder: 'dd/mm/aaaa'});
    $('#id_dt_devolucao').mask('00/00/0000', {placeholder: 'dd/mm/aaaa'});
    //if ($('#id_pg_realizado').get(0)) {
        // se necessario troca '.' por ',' no campo: 'pg_realizado'
        pg_realizado = $('#id_pg_realizado').val();
        if (pg_realizado.indexOf('.') != -1) {
            pg_realizado = pg_realizado.replace('.', ',');
        } else {
            if (pg_realizado == '') {
                pg_realizado = '0,00';
            } else {
                pg_realizado = pg_realizado.replace(/$/, ',00');
            }
        }
        // Coloca um zero no fim
        re = /(\,\d)$/;
        pg_realizado=pg_realizado.replace(re,"$1"+"0");
        // Coloca um zero antes da vírgula
        re = /^(\,\d{2})$/;
        pg_realizado=pg_realizado.replace(re,"0"+"$1");
        // Coloca um ponto antes dos 5 últimos dígitos
        re = /(\d)(\d{3})\,(\d{2})$/;
        pg_realizado=pg_realizado.replace(re,"$1.$2,$3");
        $('#id_pg_realizado').val(pg_realizado);
        $('#id_pg_realizado').mask('000.000,00', {placeholder: '000.000,00', reverse: true});
    //}
    //if ($('#id_pg_apagar').get(0)) {
        // se necessario troca '.' por ',' no campo: 'pg_apagar'
        pg_apagar = $('#id_pg_apagar').val();
        if (pg_apagar.indexOf('.') != -1) {
            pg_apagar = pg_apagar.replace('.', ',');
        } else {
            if (pg_apagar == '') {
                pg_apagar = '0,00';
            } else {
                pg_apagar = pg_apagar.replace(/$/, ',00');
            }
        }
        // Coloca um zero no fim
        re = /(\,\d)$/;
        pg_apagar=pg_apagar.replace(re,"$1"+"0");
        // Coloca um zero antes da vírgula
        re = /^(\,\d{2})$/;
        pg_apagar=pg_apagar.replace(re,"0"+"$1");
        // Coloca um ponto antes dos 5 últimos dígitos
        re = /(\d)(\d{3})\,(\d{2})$/;
        pg_apagar=pg_apagar.replace(re,"$1.$2,$3");
        $('#id_pg_apagar').val(pg_apagar);
        $('#id_pg_apagar').mask('000.000,00', {placeholder: '000.000,00', reverse: true});
    //}
    //if ($('#id_custo_total').get(0)) {
        // se necessario troca '.' por ',' no campo: 'custo_total'
        custo_total = $('#id_custo_total').val();
        if (custo_total.indexOf('.') != -1) {
            custo_total = custo_total.replace('.', ',');
        } else {
            if (custo_total == '') {
                custo_total = '0,00';
            } else {
                custo_total = custo_total.replace(/$/, ',00');
            }
        }
        // Coloca um zero no fim
        re = /(\,\d)$/;
        custo_total=custo_total.replace(re,"$1"+"0");
        // Coloca um zero antes da vírgula
        re = /^(\,\d{2})$/;
        custo_total=custo_total.replace(re,"0"+"$1");
        // Coloca um ponto antes dos 5 últimos dígitos
        re = /(\d)(\d{3})\,(\d{2})$/;
        custo_total=custo_total.replace(re,"$1.$2,$3");
        $('#id_custo_total').val(custo_total);
        $('#id_custo_total').mask('000.000,00', {placeholder: '000.000,00', reverse: true});
    //}
});

function mascara_valor(valor) {
    valor=String(valor);
    if (valor.indexOf('.') != -1) {
        valor=valor.replace('.',',');
    } else {
        if (valor == '') {
            valor='0,00';
        } else {
            valor=valor.replace(/$/, ',00');
        }
    }
    // Coloca um zero no fim
    re = /(\,\d)$/;
    valor=valor.replace(re,"$1"+"0");
    // Coloca um zero antes da vírgula
    re = /^(\,\d{2})$/;
    valor=valor.replace(re,"0"+"$1");
    // Coloca um ponto antes dos 5 últimos dígitos
    re = /(\d)(\d{3})\,(\d{2})$/;
    valor=valor.replace(re,"$1.$2,$3");
    // retorna valor
    return valor
}

$(document).ready(function(){
    if ( $("#id_legend").text().split(" ")[0] != "Excluir" ) {
        //$("#id_cliente option:first").text("");
        $("#id_cliente").chosen({
            allow_single_deselect: true,
            disable_search_threshold: 10,
            placeholder_text_single: 'Selecione um cliente ...',
            no_results_text: "Ops, nenhum cliente encontrado!",
            width: "450px"
        });
        $("#id_fantasias").chosen({
            disable_search_threshold: 10,
            placeholder_text_multiple: 'Selecione as fantasias ...',
            no_results_text: "Ops, nenhuma fantasia encontrada!",
            width: "450px"
        });
        $("#id_fantasias").chosen().change(function(){
            var opsel = $("#id_fantasias :selected").length;
            if (opsel > 0) {
                pixels = opsel * 25;
                $( "#p_id_fantasias" ).css( "height", pixels + "px" );
            } else {
                $( "#p_id_fantasias" ).css( "height", "25px" );
            }
            var total=0.0;
            for (var i=0; i<opsel; i++) {
                valor=$("#id_fantasias :selected").get(i).innerHTML.split(" ");
                valor=valor[valor.length-1];
                valor=valor.replace(',','.');
                valor=parseFloat(valor);
                total+=valor;
            }
            if (total < 0)
                total=0.0;
            pg_realizado=total/2;
            pg_realizado=mascara_valor(pg_realizado);
            $("#id_pg_realizado").val(pg_realizado);
            pg_apagar=total/2;
            pg_apagar=mascara_valor(pg_apagar);
            $("#id_pg_apagar").val(pg_apagar);
            total=mascara_valor(total);
            $("#id_custo_total").val(total);
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
        // se existir o campo pg_realizado, entao tira a mascara do campo 'pg_realizado'
        // e coloca o caracter '.' no lugar certo do campo 'pg_realizado'
        //if ($('#id_pg_realizado').get(0)) {
            if ($('#id_pg_realizado').val().indexOf(',') != -1) {
                $('#id_pg_realizado').unmask();
                var pg_realizado = $('#id_pg_realizado').val();
                var temp = pg_realizado.split("");
                temp[temp.length]   = temp[temp.length-1];
                temp[temp.length-2] = temp[temp.length-3];
                temp[temp.length-3] = ".";
                var i=0;
                pg_realizado="";
                for ( i=0; i < temp.length; i++) {
                    pg_realizado = pg_realizado + temp[i];
                }
                $('#id_pg_realizado').val(pg_realizado);
            } else
                $('#id_pg_realizado').unmask();
        //}
        // se existir o campo pg_apagar, entao tira a mascara do campo 'pg_apagar'
        // e coloca o caracter '.' no lugar certo do campo 'pg_apagar'
        //if ($('#id_pg_apagar').get(0)) {
            if ($('#id_pg_apagar').val().indexOf(',') != -1) {
                $('#id_pg_apagar').unmask();
                var pg_apagar = $('#id_pg_apagar').val();
                var temp = pg_apagar.split("");
                temp[temp.length]   = temp[temp.length-1];
                temp[temp.length-2] = temp[temp.length-3];
                temp[temp.length-3] = ".";
                var i=0;
                pg_apagar="";
                for ( i=0; i < temp.length; i++) {
                    pg_apagar = pg_apagar + temp[i];
                }
                $('#id_pg_apagar').val(pg_apagar);
            } else
                $('#id_pg_apagar').unmask();
        //}
        // se existir o campo custo_total, entao tira a mascara do campo 'custo_total'
        // e coloca o caracter '.' no lugar certo do campo 'custo_total'
        //if ($('#id_custo_total').get(0)) {
            if ($('#id_custo_total').val().indexOf(',') != -1) {
                $('#id_custo_total').unmask();
                var custo_total = $('#id_custo_total').val();
                var temp = custo_total.split("");
                temp[temp.length]   = temp[temp.length-1];
                temp[temp.length-2] = temp[temp.length-3];
                temp[temp.length-3] = ".";
                var i=0;
                custo_total="";
                for ( i=0; i < temp.length; i++) {
                    custo_total = custo_total + temp[i];
                }
                $('#id_custo_total').val(custo_total);
            } else
                $('#id_custo_total').unmask();
        //}
        $("#id_cliente").prop("disabled",false);
        $("#id_pg_apagar").prop("disabled",false);
        $("#id_pg_realizado").prop("disabled",false);
        $("#id_dt_devolucao").prop("disabled",false);
        $("#id_dt_locacao").prop("disabled",false);
        $("#id_custo_total").prop("disabled",false);
        $("#id_fantasias").prop("disabled",false);
        /* if ($("#id_fantasias :selected").length == 0) {
            $("#id_fantasias options:first").val(0);
            $("#id_fantasias options:first").prop("selected",true);
        }*/
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
