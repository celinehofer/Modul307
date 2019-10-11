$(".rb").change(function () {
    $(".rb").prop('checked', false);
    $(this).prop('checked', true);

    $(".rb").change(function () {
        $(".rb").not(this).prop('checked', false);
    });