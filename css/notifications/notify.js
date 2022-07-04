function notifyAdd(type,content,time=3000){

    let notify_red = '<div class="notify-red notifier"><p>' + content + '</p><span class="notify-countdown"></span></div>';

    let notify_green = '<div class="notify-green notifier"><p>' + content + '</p><span class="notify-countdown"></span></div>';

    let notify_yellow = '<div class="notify-yellow notifier"><p>' + content + '</p><span class="notify-countdown"></span></div>';

    if(type === "red"){
        $(".notify-container").append(notify_red)
    }else if(type === "green"){
        $(".notify-container").append(notify_green)
    }else if(type === "yellow"){
        $(".notify-container").append(notify_yellow)
    }

    $(".notify-countdown").animate(
        {"width" : "0"}, time,function(){
            $(this).parent().animate({"opacity":"0"},500,function(){
                $(this).remove()
            })
        })
}
