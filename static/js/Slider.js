$(document).ready(function () {
    $("#slider").slider({
        animate: true,
        value: 1,
        min: 0,
        max: 500,
        step: 1,
        slide: function (event, ui) {
            update(1, ui.value); //changed
        }
    });

    $("#slider2").slider({
        animate: true,
        value: 0,
        min: 0,
        max: 500,
        step: 1,
        slide: function (event, ui) {
            update(2, ui.value); //changed
        }
    });
    $("#slider3").slider({
        animate: true,
        value: 0,
        min: 0,
        max: 500,
        step: 1,
        slide: function (event, ui) {
            update(3, ui.value); //changed
        }
    });

    //Added, set initial value.เพิ่มการตั้งค่าเริ่มต้น

    $("#amount").val(0);

    $("#duration").val(0);

    $("#fat").val(0);

    $("#amount-label").text(0);

    $("#duration-label").text(0);

    $("#fat-label").text(0);

    $("#total-label'").text(0);



    update(0, 0);
});

//changed. now with parameter
function update(slider, val) {
    //changed. Now, directly take value from ui.value. if not set (initial, will use current value.)

    var total = slider == 0 ? val : $("#total").val();
    var $amount = slider == 1 ? val : $("#amount").val();
    var $duration = slider == 2 ? val : $("#duration").val();
    var $fat = slider == 3 ? val : $("#fat").val();
   
    /* commented

    $amount = $( "#slider" ).slider( "value" );
    $duration = $( "#slider2" ).slider( "value" );
     */

    //$total = newFunction() + ($amount + $duration + $fat);
    $total = parseInt($amount) + parseInt($duration) + parseInt($fat);
    //   console.log($total);

    $("#amount").val($amount);
    $("#amount-label").text($amount);


    $("#duration").val($duration);
    $("#duration-label").text($duration);


    $("#fat").val($fat);
    $("#fat-label").text($fat);


    $("#total").val($total);
    $("#total-label").text($total);

    $('#slider a').html('<label><span class="glyphicon glyphicon-chevron-left"></span> ' + $amount + ' <span class="glyphicon glyphicon-chevron-right"></span></label>');
    $('#slider2 a').html('<label><span class="glyphicon glyphicon-chevron-left"></span> ' + $duration + ' <span class="glyphicon glyphicon-chevron-right"></span></label>');
    $('#slider3 a').html('<label><span class="glyphicon glyphicon-chevron-left"></span> ' + $fat + ' <span class="glyphicon glyphicon-chevron-right"></span></label>');
}

function newFunction() {
    return " ";
}





