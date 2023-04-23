js:
function GetPlayUrl(playUrl) {
    let realPlay = {parse:0,url:playUrl};
    if (/mgtv|sohu/.test(playUrl)) {
        realPlay.headers = {'User-Agent':'Mozilla/5.0'};
    } else if (/bili/.test(playUrl)) {
        realPlay.headers  ={'User-Agent':'Mozilla/5.0','Referer':'https://www.bilibili.com'};
    } else if (/ixigua/.test(playUrl)) {
        realPlay.headers = {'User-Agent':'Mozilla/5.0','Referer':'https://www.ixigua.com'};
    }
    return realPlay
}
if (/\.m3u8|\.mp4/.test(input)) {
    input={parse:0,url:input};
} else {
    try {
let jxUrl = 'http://api.kunyu77.com/api.php/provide/parserUrl?url=';
var t = Math.floor(new Date().getTime() /1000).toString();
let jxExt = "&retryNum=0&pcode=010110002&version=2.1&devid=f9c9ce5bb5827a266829383718e6131a&package=com.sevenVideo.app.android&sys=android&sysver=12&brand=Xiaomi&model=Mi_10_Pro&sj="+t;
let url = jxUrl+input+jxExt;
let TK = "/api.php/provide/parserUrl"+"Xiaomif9c9ce5bb5827a266829383718e6131aMi_10_Procom.sevenVideo.app.android010110002"+0+t+"android12"+ encodeURIComponent(vipUrl) + "2.1"+t+"XSpeUFjJ";
let html = request(url,{headers:{Referer:jxUrl,'User-Agent':'okhttp/3.12.0','TK':md5(TK)}});
let urll = JSON.parse(html).data.url;
let playhtml = request(urll);
let playurl = JSON.parse(playhtml).url;
input = GetPlayUrl(playurl);
    }catch (e) {
        input = {parse:1,jx:1,url:input};
    }
}