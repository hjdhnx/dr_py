// let jxUrl = 'https://h5.freejson.xyz/player/analysis.php?v=';
// fetch_params.headers.Referer = jxUrl;
// try {
//     // realUrl = null;
//     let html = request(jxUrl+input);
//     log(html);
//     //realUrl = jsp.pjfh(html,'$..url');
//     realUrl=html.match(/var urls = "(.*?)"/)[1];
//     log('解析到真实播放地址:'+realUrl);
// }catch (e) {
//     log('解析发生错误:'+e.message);
//     realUrl = input;
// }
// 虾米免嗅
var flag = [];
function lazy() {
    let jxUrl = 'https://jx.xmflv.com/?url=';
    fetch_params.headers.Referer = jxUrl;
    eval(getCryptoJS());

    function encrypt(_0x5cf953) {
        var _0x5efb07 = CryptoJS.enc.Utf8.parse(vkey);
        var _0x45c0ea = CryptoJS.enc.Utf8.parse('ash3omcjsoajh1ur');
        var _0x268682 = CryptoJS.AES.encrypt(_0x5cf953, _0x5efb07, {
            'iv': _0x45c0ea,
            'mode': CryptoJS.mode.CBC,
            'padding': CryptoJS.pad.ZeroPadding
        });
        return _0x268682.toString();
    }

    function jsdecrypt(_0x1a43fe) {
        var _0x10ab4d = CryptoJS.enc.Utf8.parse(vkey);
        var _0x291247 = CryptoJS.enc.Utf8.parse('contentDocuments');
        var _0x5abb12 = CryptoJS.AES.decrypt(_0x1a43fe, _0x10ab4d, {
            'iv': _0x291247,
            'mode': CryptoJS.mode.CBC,
            'padding': CryptoJS.pad.ZeroPadding
        }).toString(CryptoJS.enc.Utf8);
        return _0x5abb12.toString();
    }

    try {
        let html = request(jxUrl + input);
        let time = html.match(/var time = '(.*?)'/)[1];
        let ua = html.match(/var ua = '(.*?)'/)[1];
        let vkey = html.match(/var vkey = '(.*?)'/)[1];
// log(encrypt(vkey));
        let phtml = request("https://jx.xmflv.com/favicon.ico", {
            headers: {
                "origin": "https://jx.xmflv.com"
            },
            body: "url=" + input + "&time=" + time + "&ua=" + ua + "&vkey=" + encrypt(vkey),
            method: "post"
        });
// log(phtml);
        realUrl = jsdecrypt(JSON.parse(phtml).url);
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}