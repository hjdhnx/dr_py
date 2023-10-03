// 星驰免嗅
var flag = [];
function lazy() {
    let jxUrl = 'https://vip.swuii.top/player/analysis.php?v=';
    fetch_params.headers.Referer = jxUrl;
    try {
        let html = request(jxUrl + input);
        eval(html.match(/var config = {[\s\S]*?}/)[0]);
        url = config.url;
        _0x4909f4 = url;
        let _0xc6d095 = '';
        log(url);
        eval(getCryptoJS());
        var _0x4909f4 = atob(_0x4909f4);
        log(_0x4909f4);
// log(_0x4909f4.length);
        var _0x3e9518 = _0x4909f4.length;
// log(_0x4909f4);
        var _0x2c3abf = [];
        var _0x1c7cc5 = [];
        var _0xfc0e29 = "202205051426239465";
        var _0x1a1b75 = _0xfc0e29.length;
        var _0x320253 = {
            "EmMtr": function (_0xcb360, _0x190522) {
                return _0xcb360 < _0x190522;
            }, "INrFk": function (_0x118889, _0x267e98) {
                return _0x118889 % _0x267e98;
            }, "YJmqv": function (_0x31bf52, _0x2fd6b6) {
                return _0x31bf52 % _0x2fd6b6;
            }, "IVJrP": function (_0x43c04f, _0x1fa873) {
                return _0x43c04f % _0x1fa873;
            }, "aTggn": function (_0x13bd41, _0x2f040c) {
                return _0x13bd41 + _0x2f040c;
            }, "txtvd": function (_0x450d4d, _0x107d6d) {
                return _0x450d4d % _0x107d6d;
            }, "EpjZa": function (_0x54d0f7, _0x37f36f) {
                return _0x54d0f7 ^ _0x37f36f;
            }, "WgDgB": function (_0x166316, _0x170b36) {
                return _0x166316 < _0x170b36;
            }, "vwjta": function (_0x13d5f4, _0x4d75ba) {
                return _0x13d5f4 + _0x4d75ba;
            }
        };
        for (i = 0; _0x320253["EmMtr"](i, 256); i++) {
            _0x2c3abf[i] = _0xfc0e29[_0x320253["YJmqv"](i, _0x1a1b75)]["charCodeAt"]();
            _0x1c7cc5[i] = i;
        }
// log(_0x1c7cc5);
        for (j = i = 0; _0x320253["EmMtr"](i, 256); i++) {
            j = _0x320253["INrFk"](_0x320253["vwjta"](j, _0x1c7cc5[i]) + _0x2c3abf[i], 256);
            tmp = _0x1c7cc5[i];
            _0x1c7cc5[i] = _0x1c7cc5[j];
            _0x1c7cc5[j] = tmp;
        }
// log(_0x2c3abf);
// log(_0x1c7cc5);
        for (a = j = i = 0; _0x320253["WgDgB"](i, _0x3e9518); i++) {
            a = _0x320253["IVJrP"](a + 1, 256);
            j = _0x320253["aTggn"](j, _0x1c7cc5[a]) % 256;
            tmp = _0x1c7cc5[a];
            _0x1c7cc5[a] = _0x1c7cc5[j];
            _0x1c7cc5[j] = tmp;
            k = _0x1c7cc5[_0x320253["txtvd"](_0x320253["aTggn"](_0x1c7cc5[a], _0x1c7cc5[j]), 256)];
            _0xc6d095 += String["fromCharCode"](_0x320253["EpjZa"](_0x4909f4[i]["charCodeAt"](), k));
            // log(_0x4909f4[i]);
        }
// log(_0x1c7cc5);
        log(_0xc6d095);
        url = unescape(_0xc6d095);
        if (/m3u8|mp4/.test(url)) {
            realUrl = url;
        } else {
            realUrl = toast(input + '解析失败:' + url);
        }
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}