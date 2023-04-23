js:
VOD = {};
let d = [];
let video_list = [];
let video_lists = [];
let list = [];
let QZOutputJson;
let html = fetch(input,fetch_params);
// print(html);
let sourceId = /get_playsource/.test(input)?input.match(/id=(\d*?)&/)[1]:input.split('cid=')[1];
let cid = sourceId;
let detailUrl = 'https://v.%71%71.com/detail/m/' + cid + '.html';
log('详情页:'+detailUrl);
// let detail_html = fetch(detailUrl,fetch_params);
var pdfh = jsp.pdfh;
var pd = jsp.pd;
//影片信息
try{
let json = JSON.parse(html);
VOD = {
    // vod_id:json.c.vid,
    vod_url:input,
    vod_name:json.c.title,
    type_name:json.typ.join(','),
    vod_actor:json.nam.join(','),
    vod_year:json.c.year,
    // vod_director:director,
    // vod_area:area,
    vod_content:json.c.description,
    vod_remarks:json.rec,
    vod_pic:urljoin2(input,json.c.pic),
};
// print(VOD);
}catch(e){log('解析片名海报等基础信息发生错误:'+e.message) }

//掏直链
if (/get_playsource/.test(input)) {
    // print('流程1');
    eval(html);
    let indexList = QZOutputJson.PlaylistItem.indexList;
    indexList.forEach(function (it) {
        let dataUrl = 'https://s.video.qq.com/get_playsource?id=' + sourceId + '&plat=2&type=4&data_type=3&range=' + it + '&video_type=10&plname=qq&otype=json';
        eval(fetch(dataUrl, fetch_params));
        let vdata = QZOutputJson.PlaylistItem.videoPlayList;
        vdata.forEach(function (item) {
            d.push({
            title:item.title,
            pic_url:item.pic,
            desc:item.episode_number + '\t\t\t播放量：' + item.thirdLine,
            url:item.playUrl,
        });
        });
        video_lists = video_lists.concat(vdata);
    });
}else{
    let json = JSON.parse(html);
    video_lists = json.c.video_ids;
    // print(video_lists);
    let url = 'https://v.qq.com/x/cover/' + sourceId + '.html';
    // if (json.c.type === 10) {//综艺
    //     // print('流程2-1');
    //     let dataUrl = 'https://s.video.qq.com/get_playsource?id=' + json.c.column_id + '&plat=2&type=2&data_type=3&video_type=8&plname=qq&otype=json';
    //     // print(dataUrl);
    //     let o_html = fetch(dataUrl, fetch_params);
    //     eval(o_html);
    //     video_lists = [];
    //     let indexList = QZOutputJson.PlaylistItem.indexList;
    //     indexList.forEach(function (it){
    //         let dataUrl = 'https://s.video.qq.com/get_playsource?id=' + json.c.column_id + '&plat=2&type=4&data_type=3&range=' + it + '&video_type=10&plname=qq&otype=json';
    //         eval(fetch(dataUrl, fetch_params));
    //         let vdata = QZOutputJson.PlaylistItem.videoPlayList;
    //         vdata.forEach(function (item){
    //             d.push({
    //             title:item.title,
    //             pic_url:item.pic,
    //             desc:item.episode_number + '\t\t\t播放量：' + item.thirdLine,
    //             url:item.playUrl,
    //         });
    //         });
    //         video_lists = video_lists.concat(vdata);
    //     });
    // }
    if (video_lists.length === 1) {//电影或者电视剧只有1集
        let vid = video_lists[0];
        url = 'https://v.qq.com/x/cover/' + cid + '/' + vid + '.html';
        // print('流程2-2');
        d.push({
            title: '在线播放',
            url: url,
        });
    } else if (video_lists.length > 1) { // 电视剧 或者动漫? 电影也分普通话版和英语版
        // print('流程2-3');
        for (let i = 0; i < video_lists.length; i += 30) {
            video_list.push(video_lists.slice(i, i + 30))
        }
        // print(video_list);
        video_list.forEach(function (it,idex){
            let o_url = 'https://union.video.qq.com/fcgi-bin/data?otype=json&tid=682&appid=20001238&appkey=6c03bbe9658448a4&union_platform=1&idlist=' + it.join(',');
            let o_html = fetch(o_url, fetch_params);
            eval(o_html);
            QZOutputJson.results.forEach(function (it1){
                it1 = it1.fields;
                let url = 'https://v.qq.com/x/cover/' + cid + '/' + it1.vid + '.html';
                d.push({
                    title: it1.title,
                    pic_url: it1.pic160x90.replace('/160',''),
                    desc: it1.video_checkup_time,
                    url: url,
                    type:it1.category_map&&it1.category_map.length>1?it1.category_map[1]:''
                });
            });
        });

    }

}
// print(d);
let yg = d.filter(function (it){
    return (it.type&&it.type!=='正片')
});
let zp = d.filter(function (it){
    return !(it.type&&it.type!=='正片')
});
VOD.vod_play_from = yg.length<1?'qq':'qq$$$qq 预告及花絮';
VOD.vod_play_url = yg.length<1?d.map(function (it){
    return it.title + '$' + it.url;
}).join('#'):[zp,yg].map(function (it){
    return it.map(function (its){
        return its.title + '$' + its.url;
    }).join('#');
}).join('$$$');