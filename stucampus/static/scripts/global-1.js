
window.onload = function(){
    $(".sidebar").css("display","none");
    setTimeout(function(){
        $(".fixed-logo").css("transform","scale(1)");
    },500);
    w = document.body.clientWidth;
    if(w<=767){
        fontsize= w/750*30 ;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    } 
    else if(w>=768&&w<=1600){
        fontsize = w/1366*30;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    } 
    else if(w>=1600){
        fontsize = 1600/1366*30;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    }
    now = 0;
    banner1 = $("#banner1");
    banner2 = $("#banner2");
    banner3 = $("#banner3");
    banner4 = $("#banner4");
    bannerwidth = parseInt(banner1.css("width"))/fontsize;
    rounds={
        '0' : $(".round1"),
        '1' : $(".round2"),
        '2' : $(".round3"),
        '3' : $(".round4"),
    }
    bannerRun();
    navcome(6);
    bind();
};
    banner1 = $("#banner1");
    banner2 = $("#banner2");
    banner3 = $("#banner3");
    banner4 = $("#banner4");
window.onresize = function(){
    bannerwidth = parseInt(banner1.css("width"))/fontsize;
    w = document.body.clientWidth;
    if(w<=767){
        fontsize= w/750*30 ;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;") ;
        bannerselect(now);
    }
    else if(w>=768){
        fontsize = w/1366*30;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    }
    bannerselect(now);
}
function bannertouchstart(event){
    touch = event.touches[0];
    firstPos = {
        x : Number(touch.pageX),
        y : Number(touch.pageY)
    };
    event.preventDefault();
}
function bannertouchend(event){
    touch = event.changedTouches[0];
    lastPos = {
        x : Number(touch.pageX),
        y : Number(touch.pageY)
    };
    if(lastPos["x"]>firstPos["x"]){
        time = 0;
        if(now==0){
            bannerselect(3);
        }
        else{
            bannerselect(now-1);
        }
    }
    else if(lastPos["x"]<firstPos["x"]){
        time = 0;
        if(now==3){
            bannerselect(0);
        }
        else{
            bannerselect(now+1);
        }
    }
}
function bind(){
    for(i=1;i<=4;i++){
        $("#banner"+i)[0].addEventListener("touchstart",bannertouchstart);
        $("#banner"+i)[0].addEventListener("touchend",bannertouchend);
    }
}

var time = 0;
function bannerRun(){
    setInterval(function(){ time += 1; },1);
    setInterval(function(){
        if(time>=2000){
            rounds[now].removeClass("active");
            now = now + 1;
            if(now>=4){
                now = 0;
            }
            rounds[now].addClass("active");
            banner1.css("z-index",1);
            banner2.css("z-index",1);
            banner3.css("z-index",1);
            banner4.css("z-index",1);
            bannerselect(now);
            if(now==2){
                banner1.css("z-index",-1);
                banner1.css("left",bannerwidth*2+"rem");
            }
            else if(now==3){
                banner2.css("z-index",-1);
                banner2.css("left",bannerwidth+"rem");
            }
            else if(now==0){
                banner3.css("z-index",-1);
                banner3.css("left","0rem");
            }
            else if(now==1){
                banner4.css("z-index",-1);
                banner4.css("left",-bannerwidth+"rem");
            }
            else{
                banner1.css("left","0rem");
                banner2.css("left","0rem");
                banner3.css("left","0rem");
                banner4.css("left","0rem");
                now=0;
            }
            time = 0;
        }
    },3);
}
function bannerselect(bannerid){
    if(bannerid==0){
        banner1.css("left",-bannerid*bannerwidth+"rem");
        banner2.css("left",-bannerid*bannerwidth+"rem");
        banner3.css("left",-bannerid*bannerwidth+"rem");
        banner4.css("left",-4*bannerwidth+"rem");
    }
    else if(bannerid==1){
        banner1.css("left",-bannerid*bannerwidth+"rem");
        banner2.css("left",-bannerid*bannerwidth+"rem");
        banner3.css("left",-bannerid*bannerwidth+"rem");
        banner4.css("left",-bannerid*bannerwidth+"rem");
    }
    else if(bannerid==2){
        banner1.css("left",2*bannerwidth+"rem");
        banner2.css("left",-bannerid*bannerwidth+"rem");
        banner3.css("left",-bannerid*bannerwidth+"rem");
        banner4.css("left",-bannerid*bannerwidth+"rem");
    }
    else if(bannerid==3){
        banner1.css("left",bannerwidth+"rem");
        banner2.css("left",bannerwidth+"rem");
        banner3.css("left",-bannerid*bannerwidth+"rem");
        banner4.css("left",-bannerid*bannerwidth+"rem");
    }
    time = 0;
    rounds[now].removeClass("active");
    now = bannerid;
    rounds[now].addClass("active");
    return false;
}

sidebaropen = function(){
    $(".sidebar").css("display","block");
    setTimeout(function(){
        $(".sidebar").addClass("sidebarout");
        $(".call-back").css("display","block");
    },100);
    return false;
}
sidebarclose = function(){
    $(".sidebar").removeClass("sidebarout");
    $(".call-back").css("display","none");
    setTimeout(function(){
        $(".sidebar").css("display","none");
    },500);
    return false;
}

function navcome(navid){
    nownav = $(".now");
    if(navid==6){
        nownav.css("left",0+"rem");
        return false;
    }
    for(i=0;i<5;i++){
        $("#nav"+i).removeClass("nav-active");
    }
    if(navid==0){
        nownav.css("left",navid*4.0+"rem");
        $("#nav"+navid).addClass("nav-active");
        setTimeout(function(){
            window.location.href = "http://stu.szu.edu.cn/";
        },500);
    }
    else if(navid==1){
        nownav.css("left",navid*4.0+"rem");
        $("#nav"+navid).addClass("nav-active");
        setTimeout(function(){
            window.location.href = "http://stu.szu.edu.cn/lecture/";
        },500);
    }
    else if(navid==2){
        nownav.css("left",navid*4.0+"rem");
        $("#nav"+navid).addClass("nav-active");
        setTimeout(function(){
            window.location.href = "http://stu.szu.edu.cn/activity/";
        },500);
    }
    else if(navid==3){
        nownav.css("left",navid*4.0+"rem");
        $("#nav"+navid).addClass("nav-active");
        setTimeout(function(){
            window.location.href = "http://stu.szu.edu.cn/articles/photography/";
        },500);
    }
    else if(navid==4){
        nownav.css("left",navid*4.0+"rem");
        $("#nav"+navid).addClass("nav-active");
        setTimeout(function(){
            window.location.href = "http://stu.szu.edu.cn:8080/";
        },500);
    }
}
var logoclicktime = 0;
function hiddenthings(){
    logoclicktime += 1;
    if(logoclicktime<=5){
        $('html, body').animate({
            scrollTop: '0px'
        }, 800);
    }
    if(logoclicktime==6){
        $(".fixed-logo").css("transform","scale(4)");
        $(".fixed-logo").css("opacity","0");
        setTimeout(function(){
            window.location.href = "http://stu.szu.edu.cn/manage/index";
        },500);
    }
};