console.log('hello world')
$(document).on("click", ".image-display", function (e) {
    e.preventDefault();
    var $popup = $(".modal");
    var popup_url = $(this).data("popup-url");
    $(".modal-body", $popup).load(popup_url, function () {
    $popup.modal("show");
    });
});
