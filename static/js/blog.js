$(window).on('scroll', function () {
    // 判断显示还是隐藏按钮
    if ($(this).scrollTop() >= $(this).height()) {
        $('#top').fadeIn('slow');
    } else {
        $('#top').fadeOut('slow');
    }
});
$("#top").click(function () {
    $("html,body").animate({scrollTop: 0}, 500);
});

// Message显示3秒后消失
$("#msg_alert").delay(2000).fadeOut();


// $("#comment_submit").click(function () {
//     let error_text = $("#comment_error_text");
//     error_text.text("");
//     const ek_content = CKEDITOR.instances['id_detail'].document.getBody().getText().trim();
//     if (ek_content ==="") {
//         error_text.text("评论内容不能为空");
//         return false;
//     }
//
//     CKEDITOR.instances['id_detail'].updateElement();
//
//     $.ajax({
//         type: "POST",
//         url: '/comment/add_comment/',
//         data: $("#comment_form").serializer,
//         async: true,
//         // cache: false,
//         success: function (data, textStatus, jqXHR) {
//             console.log(data);
//             console.log(textStatus);
//             console.log(jqXHR);
//             if (data["status"] === "success"){
//                 location.reload();
//             } else {
//                 error_text.text(data["error_message"]);
//             }
//
//         },
//         error: function (xhr, textStatus) {
//             console.log("错误");
//             console.log(xhr);
//             console.log(textStatus);
//         }
//
//     })
// });