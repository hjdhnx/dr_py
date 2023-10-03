var flag = [];
function lazy(){
let jxUrl = 'https://vip.lianfaka.com/vip/?url=';
fetch_params.headers.Referer = 'https://www.dy6g.com';
// fetch_params.headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9s Plus Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36';
fetch_params.headers['User-Agent'] = MOBILE_UA;
try {
    let html = request(jxUrl+input);
    log(html);
    realUrl=html.match(/source src="(.*?)"/)[1];
    log('解析到真实播放地址:'+realUrl);
}catch (e) {
    log('解析发生错误:'+e.message);
    realUrl = input;
}

return realUrl
}