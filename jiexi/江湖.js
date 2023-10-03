var flag = [];
function lazy() {
    let jxUrl = 'http://45.248.10.163:4433/json.php?wap=0&url=';
    fetch_params.headers.Referer = jxUrl;
    try {
        // realUrl = null;
        let html = request(jxUrl + input);
        // log(html);
        realUrl = jsp.pjfh(html, '$..url');
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl

}