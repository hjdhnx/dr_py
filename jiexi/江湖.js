// realUrl = 重定向('http://211.99.99.236:4567/jhjson/ceshi.php?url='+vipUrl);
// let jxUrl = 'http://211.99.99.236:4567/jhjson/ceshi.php?url=';
// let jxUrl = 'http://jx.vipmv.co/json.php?token=123457&url=';
let jxUrl = 'http://45.248.10.163:4433/json.php?wap=0&url=';
fetch_params.headers.Referer = jxUrl;
try {
    // realUrl = null;
    let html = request(jxUrl+vipUrl);
    // log(html);
    realUrl = jsp.pjfh(html,'$..url');
    log('解析到真实播放地址:'+realUrl);
}catch (e) {
    log('解析发生错误:'+e.message);
    realUrl = vipUrl;
}