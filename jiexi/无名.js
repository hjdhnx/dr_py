// let jxUrl = 'http://api.ckflv.cn/?url=';
var flag = [];
function lazy() {
    log(env);
    let jxUrl = 'https://k.json.icu/home/api?type=ys&uid=12406929&key=adgouwyCGIRSTUV046&url=';
    fetch_params.headers.Referer = jxUrl;
    try {
        // realUrl = null;
        let html = request(jxUrl + input);
        log(html);
        realUrl = jsp.pjfh(html, '$..url');
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}