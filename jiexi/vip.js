var flag = [];
function lazy() {
    let jxUrl = 'https://80k.tv/jxplayer.php?v=';
    fetch_params.headers.Referer = 'https://1080p.tv';
    fetch_params.headers['User-Agent'] = MOBILE_UA;
    try {
        let html = request(jxUrl + input);
        log(html);
        realUrl = html.match(/src="(h.*?)"/)[1];
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}