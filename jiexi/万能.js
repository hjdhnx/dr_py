var flag = [];
function lazy() {
    let jxUrl = 'https://json.legendwhb.cn/llq/?url=';
    fetch_params.headers.Referer = jxUrl;
    try {
        let html = request(jxUrl + input);
        eval(html.match(/var config = {[\s\S]*?}/)[0] + "");
        let play = request("https://json.legendwhb.cn/llq/API.php", {
            headers: {
                "User-Agent": MOBILE_UA,
                "X-Requested-With": "XMLHttpRequest",
                "origin": "https://json.legendwhb.cn"
            }, body: "url=" + config.url + "&time=" + config.time + "&key=" + config.key, method: "POST"
        });
        realUrl = JSON.parse(play).url;
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}