js:
let d = [];
function get_result(url){
    let videos = [];
    let html = request(url);
    let jo = JSON.parse(html);
    if(jo['code'] === 0){
        let vodList = jo.result?jo.result.list:jo.data.list;
        vodList.forEach(function (vod){
            let aid = (vod['season_id']+'').trim();
            let title = vod['title'].trim();
            let img = vod['cover'].trim();
            let remark = vod.new_ep?vod['new_ep']['index_show']:vod['index_show'];
            videos.push({
                "vod_id": aid,
                "vod_name": title,
                "vod_pic": img,
                "vod_remarks": remark
            });
        });
    }
    return videos;
}
function get_rank(tid,pg){
    return get_result('https://api.bilibili.com/pgc/web/rank/list?season_type='+tid+'&pagesize=20&page='+pg+'&day=3')
}

function get_rank2(tid,pg){
    return get_result('https://api.bilibili.com/pgc/season/rank/web/list?season_type='+tid+'&pagesize=20&page='+pg+'&day=3')
}
function home_video(){
    let videos = get_rank(1).slice(0,5);
    [4, 2, 5, 3, 7].forEach(function (i){
        videos = videos.concat(get_rank2(i).slice(0,5))
    });
    return videos;
}
VODS = home_video();