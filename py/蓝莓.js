js:
var MY_HOME='http://lanmeiguojiang.com:5244/d/%E8%93%9D%E8%8E%93%E4%BA%91%E7%9B%98';
// let headers = d.headers;
// headers['Referer'] = input;
// let fetch_params = {headers:headers,timeout:d.timeout,encoding:d.encoding};
// print(fetch_params);
let html = fetch(input,fetch_params);
var player = JSON.parse(html.match(/r player_.*?=(.*?)</)[1]);
var jsurl = player.url;
var from = player.from;
if (player.encrypt == '1') {
    var jsurl = unescape(jsurl);
} else if (player.encrypt == '2') {
    var jsurl = unescape(base64Decode(jsurl));
} else {
    jsurl
}
// print(from);
if (/ddzy|duoduo/.test(from)) {
    let mx = true;
    if(mx) {
        let new_obj = JSON.parse(JSON.stringify(fetch_params));
        delete new_obj.headers['Referer'];
        let html = request(MY_HOME + '/pzwj.js',new_obj);
        // print(html);
        eval(html);
        // print('好了');
        var jx = MacPlayerConfig.player_list[from].parse;
        print('第1次多多解析:', jx);
        fetch_params.headers['Referer']='https://www.pipipao.com/';
        eval(fetch(jx + jsurl, fetch_params).match(/var config = {[\s\S]*?}/)[0]);
        jx = jx.replace('?url=', '');
        eval(fetch(jx + 'js/decode.js', fetch_params));
        jxk = fetch(jx + 'js/setting.js', fetch_params).split(',');
        jx += '555tZ4pvzHE3BpiO838.php'; //eval(jxk[32])
        print('第2次多多解析:', jx);
        config.tm = new Date().getTime();
        config.sign = 'F4penExTGogdt6U8'; //eval(jxk[36])
        input = getVideoInfo(JSON.parse(fetch(buildUrl(jx, config), fetch_params)).url);
        // input = input.replace(/,/g,'').slice(2);
    }
} else if(from==='ziqie'){
    let jxurl = "https://lanmeiguojiang.com/dd/?url=" + jsurl;
    // print(jxurl);
    input = maoss(jxurl, jxurl, "A42EAC0C2B408472")
}