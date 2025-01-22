$(document).ready(function () {
    $(".btn-primary").click(function () {
        let info = $(this).data('info');
        $('.modal-body').html(info);
        console.log(info);
    });
});