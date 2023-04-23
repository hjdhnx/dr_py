let jxUrl = 'http://168.qxzm.cc/user/owe.php?app=10000&account=hjdhnx&password=hjdhnx&url=';
fetch_params.headers.Referer = jxUrl;
try {
    // realUrl = null;
    let html = request(jxUrl+vipUrl);
    log(html);
    realUrl = jsp.pjfh(html,'$..url');
    log('解析到真实播放地址:'+realUrl);
}catch (e) {
    log('解析发生错误:'+e.message);
    realUrl = vipUrl;
}