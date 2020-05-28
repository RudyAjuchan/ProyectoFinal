$(document).ready(function(){
    $('input[type=text]').addClass('form-control pl-5 mt-3');
    $('input[type=number]').addClass('form-control pl-5 mt-3');
    //inputs para clientes
    $('#id_Nombre').attr("placeholder","Ingrese el nombre del cliente");
    $('#id_Nombre').attr("require","require");
    $('#id_Apellido').attr("placeholder","Ingrese los apellidos");
    $('#id_Apellido').attr("require","require");
    $('#id_Direccion').attr("placeholder","Ingrese la dirección");
    $('#id_Direccion').attr("require","require");
    $('#id_Telefono').attr("placeholder","Ingrese el telefono");
    $('#id_Telefono').attr("require","require");
    $('#id_Nit').attr("placeholder","Ingrese el NIT");
    $('#id_Nit').attr("require","require");

    $('.form_zapatos #id_Estilo').attr("placeholder","Ingrese el estilo");
    $('.form_zapatos #id_Estilo').attr("require","require");
    $('.form_zapatos #id_Color').attr("placeholder","Ingrese el color");
    $('.form_zapatos #id_Color').attr("require","require");
    $('.form_zapatos #id_Talla').attr("placeholder","Ingrese la talla");
    $('.form_zapatos #id_Talla').attr("require","require");
    $('.form_zapatos #id_Marca').attr("placeholder","Ingrese la marca");
    $('.form_zapatos #id_Marca').attr("require","require");
    $('.form_zapatos #id_Proveedor').attr("placeholder","Ingrese el proveedor");
    $('.form_zapatos #id_Proveedor').attr("require","require");
    $('.form_zapatos #id_Precio').attr("placeholder","Ingrese el precio");
    $('.form_zapatos #id_Precio').attr("require","require");
    $('.form_zapatos #id_Stock').attr("placeholder","Ingrese la cantidad comprada");
    $('.form_zapatos #id_Stock').attr("require","require");
    $('.form_zapatos #id_Fecha_entrada').attr("placeholder","Ingrese la fecha");
    $('.form_zapatos #id_Fecha_entrada').attr("require","require");
    $('.form_zapatos #id_Fecha_entrada').attr("type","date");

    $('#id_Precio2').attr("placeholder","Precio de Zapato");
    $('#id_Precio2').attr("require","require");
    $('#id_Precio2').attr("readonly","readonly");
    $('#id_Cantidad').attr("placeholder","Ingrese la cantidad de zapatos");
    $('#id_Total').attr("placeholder","Total a pagar");
    $('#id_Total').attr("readonly","readonly");
    $('#id_Total').attr("require","require");
    $('#id_id_Zapato').attr("require","require");
    $('#id_id_Zapato2').attr("require","require");


    $('#alerta').modal('show');

    $('#id_id_Zapato2').click(function(){        
        var aux=document.getElementById('id_id_Zapato2').value;
        $('#id_Precio2').val(aux);
    });
    $('#id_Cantidad').keyup(function(){
        console.log("si pasa");
        var precio=$('#id_Precio2').val();
        var cantidad=$('#id_Cantidad').val();
        var total=precio*cantidad;
        console.log(precio,cantidad);
        $('#id_Total').val(total);
    });

    $('#id_total').removeClass("mt-3");
    $('#id_Fecha').removeClass("mt-3");
    $('#id_Fecha').attr('type','date');
});

function imprimir(){
    var restorepage = document.body.innerHTML;
    var printcontent = document.getElementById('content-imprimir').innerHTML;
    document.body.innerHTML=printcontent;
    window.print();
    document.body.innerHTML=restorepage;
}