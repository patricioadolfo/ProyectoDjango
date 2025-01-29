$(document).ready(function () {
    $(".btn-primary").click(function () {
        let info = $(this).data('info');
        $('.maps').html(info);
        console.log(info);
    });
});