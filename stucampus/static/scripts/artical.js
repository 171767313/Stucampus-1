window.onscroll = function(){
	var scrollTop = document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;
	if(scrollTop>=biaogan){
		$(".artical-header").addClass("up");
		$(".blur").css("display","none");
		$(".artical-title").addClass("artical-title-up");
		$(".artical-main").addClass("main-up");
	}
	else if(scrollTop<=biaogan){
		$(".artical-header").removeClass("up");
		$(".blur").css("display","block");
		$(".artical-title").removeClass("artical-title-up");
		$(".artical-main").removeClass("main-up");
	}
}
function backhome(){
    window.location.href="/index.html";
}
var logoclicktime = 0;
$(function(){
    setTimeout(function(){
        $(".fixed-logo").css("transform","scale(1)");
        $(".btn").css("transform","scale(1)");
    },500);
    $("#backTop").click(function() {
        $('html, body').animate({
            scrollTop: '0px'
        }, 800);
        $(".fixed-logo").click();
    });
    w = document.body.clientWidth;
    if(w<=767){
        fontsize= w/750*30 ;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    } 
    else if(w>=768&&w<=1600){
        fontsize= w/1366*30 ;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;") ;
    }
    else if(w>=1600){
        fontsize = 1600/1366*30;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    }
    navcome(6);
});
function showtools(){
    logoclicktime += 1;
    if(logoclicktime%2 != 0){
        $("#backTop").css("bottom","5.86667rem");
        $("#share").css("bottom","9.6rem");
        $("#discuss").css("bottom","13.33333rem");
        $("#like").css("bottom","17.06667rem");
    }
    else if(logoclicktime%2 == 0){
        $("#backTop").css("bottom","1.6rem");
        $("#share").css("bottom","1.6rem");
        $("#discuss").css("bottom","1.6rem");
        $("#like").css("bottom","1.6rem");
    }
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