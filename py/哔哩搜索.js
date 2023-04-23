js:
let url1 = input+'media_bangumi';
let url2 = input+'media_ft';
let html = request(url1);
let msg = JSON.parse(html).message;
if(msg!=='0'){
    VODS = [{vod_name:KEY + '➢'+msg,vod_id:'no_data',vod_remarks:'别点,缺少bili_cookie',vod_pic:'https://ghproxy.com/https://raw.githubusercontent.com/hjdhnx/dr_py/main/404.jpg'}];
}else {
    let jo1 = JSON.parse(html).data;
    html = request(url2);
    let jo2 = JSON.parse(html).data;
    let videos = [];
    let vodList = [];
    if (jo1['numResults'] === 0) {
        vodList = jo2['result'];
    } else if (jo2['numResults'] === 0) {
        vodList = jo1['result'];
    } else {
        vodList = jo1['result'].concat(jo2['result']);
    }
    vodList.forEach(function (vod) {
        let aid = (vod['season_id'] + '').trim();
        let title = KEY + '➢' + vod['title'].trim().replace("<em class=\"keyword\">", "").replace("</em>", "");
        let img = vod['cover'].trim();
        let remark = vod['index_show'];
        videos.push({
            "vod_id": aid,
            "vod_name": title,
            "vod_pic": img,
            "vod_remarks": remark
        });
    });
    VODS = videos;
}