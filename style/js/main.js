var animaionTime = 700;
$.each($('.fadein'), function (i, e) {
    $(this).fadeIn(animaionTime);
});

let imgBack = new BackgroundReplace({ attribute: 'background' });
imgBack.start();