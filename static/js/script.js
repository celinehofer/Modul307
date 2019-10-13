/*by chose of a radio button, the number fields of the other radio buttons get freeze */
$(document).ready(function(){
    $('#option1').prop('checked', true);
    radioButtons('option1');
});

function radioButtons(input_class){
    $('.rb').prop('disabled', true);
    $('.' + input_class).prop('disabled', false);
}

