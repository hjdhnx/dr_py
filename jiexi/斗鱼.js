js:
//输入的input如:https://m.douyu.com/312212?dyshid=0-00000003333&dyshci=1
function getSign(script, rid, did, tt){

    let result = script.match(/(function ub98484234.*)\s(var.*)/)[0];
    let func_ub9 = result.replace(/eval.*;}/, 'strc;}', result);
    eval(func_ub9);

    let res = ub98484234();
    let v = res.match(/v=(\d+)/)[0].replace("v=", '');
    let rb = md5(rid + did + tt + v);

    let func_sign = res.replace(/return rt;}\);?/, 'return rt;}');
    func_sign = func_sign.replace('(function (', 'function sign(');
    func_sign = func_sign.replace('CryptoJS.MD5(cb).toString()', '"' + rb + '"');
    eval(func_sign);

    let params = sign(rid, did, tt) + "&ver=219032101&rate=-1&rid="+rid;
    return params
}
// log(env);
// fetch_params.headers.Referer = input;
var flag = [];
function lazy() {
    try {
        // realUrl = null;
        let html = request(input);
        // log(html);
        let rid = html.match(/rid":(.*?),"vipId/)[1];
        log(rid);
        // let tt = Date.parse(new Date()).toString().substr(0, 10);
        let tt = Math.round(new Date().getTime() / 1000).toString();
        let did = '10000000000000000000000000001501';
        let param_body = getSign(html, rid, did, tt);
        log(param_body);
        let stream_json = request('https://m.douyu.com/api/room/ratestream', {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            }, body: param_body, method: 'POST'
        });
        log(stream_json);
        let stream = JSON.parse(stream_json).data;
        realUrl = stream.url;
        log('解析到真实播放地址:' + realUrl);
    } catch (e) {
        log('解析发生错误:' + e.message);
        realUrl = input;
    }
    return realUrl
}