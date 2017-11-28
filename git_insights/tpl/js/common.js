window.onload = function(){
    // $(".commit_num").mouseover(function(){
    //     $(this).css("color",'red');
    //     $(this).next().css("display",'block');
    // });
    // $(".commit_num").mouseout(function(){
    //     $(this).css("color",'blue');
    //     $(this).next().css("display",'none');
    // });
    $("[data-toggle='popover']").popover();

    $(".commit_id").popover({ trigger: "manual" , html: true, animation:false})
    .on("mouseenter", function () {
        var _this = this;
        $(this).popover("show");
        $(".popover").on("mouseleave", function () {
            $(_this).popover('hide');
        });
    }).on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide");
            }
        }, 100);
    });


};

