$("form[name=signup_form]").submit(function (e) {
    let $form = $(this);
    var $error = $form.find(".error");
    let data = $form.serialize();

    $.ajax({
        url: "/user/signup/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            console.log(resp);
        },
        error: function (resp) {
            console.log(resp);
        }
    })

    e.preventDefault();
})