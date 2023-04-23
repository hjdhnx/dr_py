js:
if(/^http/.test(input)){
input = {
  jx:1,
  url:input,
  parse:0
};
}else{
let ids = input.split('_');
let result = {};
let url = 'https://api.bilibili.com/pgc/player/web/playurl?qn=116&ep_id='+ids[0]+'&cid='+ids[1];
let html = request(url);
let jRoot = JSON.parse(html);
if(jRoot['message'] !== 'success'){
    print("需要大会员权限才能观看");
    input = '';
}else{
    let jo = jRoot['result'];
    let ja = jo['durl'];
    let maxSize = -1;
    let position = -1;
    ja.forEach(function (tmpJo,i){
        if(maxSize < Number(tmpJo['size'])){
            maxSize = Number(tmpJo['size'])
            position = i;
        }
    });
    let url = '';
    if(ja.length > 0){
        if(position === -1){
          position = 0;
        }
        url = ja[position]['url'];
    }
    result["parse"] = 0;
    result["playUrl"] = '';
    result["url"] = url;
    result["header"] = {
            "Referer": "https://www.bilibili.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    };
    result["contentType"] = 'video/x-flv';
    input = result;
}
}