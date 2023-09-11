/**
 * setting.js
 * @author 巴拉巴拉
 * @date 2022-02-15
 * @version 8.8.8
 */
/*接口初始化*/
function player(config){
    if ((navigator.userAgent.indexOf("MSIE") >= 0) || (navigator.userAgent.indexOf("Trident") >= 0)) {
        alert("本播放器在IE浏览器和兼容模式下无法播放，请将浏览器设置为 极速模式！");
    }
    if(config.url.indexOf(".m3u8")>0||config.url.indexOf(".mp4")>0||config.url.indexOf(".flv")>0){
        MPlayer(config.url,config.title,config.vkey,config.next);
    }else{
        $.ajaxSettings.timeout='30000';
        // post php
        // $.post("api_config.php", {"url":config.url,"time":config.time,"key":config.key,"title":config.title},
        //     function(data) {
        //         if(data.code=="200"){
        //             MPlayer(data.url,config.title,config.vkey,config.next);
        //         }else{
        //             TheError();
        //         }
        //     },'json').error(function (xhr, status, info) {
        //     TheError();
        // });
    }
}
/*播放器初始化*/
function MPlayer(url,tittle,vkey,nexturl){
    $("#loading").remove();
    if(!nexturl){
        playcss(1);
    }else{
        playcss(2);
    }
    var playerConfig={
        container: '#mui-player', /*播放器ID*/
        themeColor: '#fa0000',   /*进度条颜色*/
        src:url,  /*视频播放地址*/
//        title: tittle,/*视频标题*/
        poster: '/web/player/mui/imges/background.jpg',/*背景图片*/
        autoplay: true,/*自动播放*/
        initFullFixed: true,/*是否全屏*/
        preload: 'auto',/*预加载*/
        autoOrientaion: true,/*自动切换方向*/
        dragSpotShape: 'circula',/*进度条样式 可选 circula | square*/
        lang: 'zh-cn',/*语言*/
        volume: '1',/*声音默认1 可选0.5*/
        playbackSpeed:[0.5, 0.75, 1, 1.25, 1.5, 2,2.5,3,3.5,4,4.5,5], // 播放速度
        videoAttribute:[
            {attrKey:'webkit-playsinline',attrValue:'webkit-playsinline'},
            {attrKey:'playsinline',attrValue:'playsinline'},
            {attrKey:'x5-video-player-type',attrValue:'h5-page'},
        ],
        plugins: [
            new MuiPlayerDesktopPlugin({
                leaveHiddenControls: true,
                fullScaling: 1,
            }),
            new MuiPlayerMobilePlugin({
                key:'01I01I01H01J01L01K01J01I01K01J01H01D01J01G01E',
                showMenuButton: true,
            })
        ]
    };
    if(url.indexOf(".m3u8")>0){
        playerConfig.parse= {
            type:'hls',
            loader:Hls,
            config: {
                debug:false,
            },
        };
    }else if(url.indexOf(".flv")>0){
        playerConfig.parse= {
            type:'flv',
            loader:flvjs,
            config: {
                cors:true,
            },
        };
    }
    if(!!nexturl){
        playerConfig.custom={
            footerControls:[{
                slot:'nextMedia',
                position:'left',
                tooltip:'下一集',
                oftenShow:true,
                click:function(e) {
                    top.location.href=nexturl;
                },
            }]
        };
    }
    var mp = new MuiPlayer(playerConfig);
    //记忆播放开始
    mp.on('ready',function(){
        var video = mp.video();
        var currentTime = localStorage.getItem(vkey);
        video.addEventListener("loadedmetadata",function(){
            this.currentTime = currentTime;
        });
        video.addEventListener("timeupdate",function(){
            var currentTime = Math.floor(video.currentTime);
            localStorage.setItem(vkey,currentTime);
        });
        video.addEventListener("ended",function(){
            localStorage.removeItem(vkey);
            if(!!nexturl){
                top.location.href=nexturl;
            }
        });
    //    弹出层提示
    });mp.on('ready',function() {
        //mp.showToast('手机端请手动点击播放');
        mp.showToast('提醒：请勿随意相信视频上网址,电话,二维码等！', 6000)
    });
    mp.on('error',function() {
        mp.showToast('视频加载失败，切换线路或刷新一次', 5000)
    });
    mp.on('seek-progress',function() {
        mp.showToast('加载中...')
    });
}
function playcss(num){
    if(num==1){
        $("body").append("<div id=\"mui-player\" class=\"content\"></div>");
    }else{
        $("body").append("<div id=\"mui-player\" class=\"content\"><template slot=\"nextMedia\"><svg t=\"1584686776454\" class=\"icon\" viewBox=\"0 0 1024 1024\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" p-id=\"1682\"><path d=\"M783.14692466 563.21664097L240.85307534 879.55472126c-39.1656664 24.10194914-90.38230866-6.02548665-90.38230865-51.21664226v-632.676158c0-45.19115433 51.21664097-75.31859011 90.38230865-51.21664226l542.29384932 316.33808029c39.1656664 21.08920518 39.1656664 81.34407804 0 102.43328194z\" p-id=\"1683\" fill=\"#ffffff\"></path><path d=\"M873.52923331 734.94302767c0 42.17841036-39.1656664 78.33133408-90.38230865 78.33133407s-90.38230866-36.15292371-90.38230735-78.33133407V289.05697233c0-42.17841036 39.1656664-78.33133408 90.38230735-78.33133407s90.38230866 36.15292371 90.38230865 78.33133407v445.88605534z\" p-id=\"1684\" fill=\"#ffffff\"></path></svg></template></div>");
    }
}
function TheError(){
    $("jxsb").append("<div id=\"error\"><h1>解析失败，请刷新重试或检查地址~</h1></div>");
    $("#loading").remove();
}