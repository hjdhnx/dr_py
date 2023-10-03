var flag = [];
function lazy() {
    let jxUrl = 'http://api.kunyu77.com/api.php/provide/parserUrl?url=';
    var t = Math.floor(new Date().getTime() / 1000).toString();
    let jxExt = "&retryNum=0&pcode=010110002&version=2.1&devid=f9c9ce5bb5827a266829383718e6131a&package=com.sevenVideo.app.android&sys=android&sysver=12&brand=Xiaomi&model=Mi_10_Pro&sj=" + t;
    let url = jxUrl + input + jxExt;
    let TK = "/api.php/provide/parserUrl" + "Xiaomif9c9ce5bb5827a266829383718e6131aMi_10_Procom.sevenVideo.app.android010110002" + 0 + t + "android12" + encodeURIComponent(input) + "2.1" + t + "XSpeUFjJ";
    fetch_params.headers.Referer = jxUrl;
// fetch_params.headers['User-Agent'] = "Dalvik/2.1.0";
    fetch_params.headers['User-Agent'] = "okhttp/3.12.0";
    fetch_params.headers['TK'] = md5(TK);
    try {
        // realUrl = null;
        let html = request(url);
        log(html);
        realUrl = jsp.pjfh(html, '$..url');
        realUrl = 重定向(realUrl);
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}