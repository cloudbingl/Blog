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


