window.onresize = function(){
    w = document.body.clientWidth;
    if(w<=767){
        fontsize= w/750*30 ;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;") ;
    }
    else if(w>=768&&w<=1600){
        fontsize= w/1366*30 ;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;") ;
    }
    else if(w>=1600){
        fontsize = 1600/1366*30;
        document.getElementsByTagName("html")[0].setAttribute("style", "font-size:"+fontsize+"px;")
    }
}