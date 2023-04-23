js:
let d = [];
let html = request(input);
let json = JSON.parse(html).data;
VOD = {
    vod_id:'',
    vod_url:input,
    vod_name:'',
    type_name:'',
    vod_actor:'',
    vod_year:'',
    vod_director:'',
    vod_area:'',
    vod_content:'',
    vod_remarks:'',
    vod_pic:'',
};
VOD.vod_name = json.name;
try {
    if (json.latestOrder) {
        VOD.vod_remarks = "类型: " + (json.categories[0].name || "") + "\t" + (json.categories[1].name || "") + "\t" + (json.categories[2].name || "") + "\t" + '评分：' + (json.score || "") + "\n更新至：第" + json.latestOrder + "集(期)/共" + json.videoCount + "集(期)";
    } else {
        VOD.vod_remarks = "类型: " + (json.categories[0].name || "") + "\t" + (json.categories[1].name || "") + "\t" + (json.categories[2].name || "") + "\t" + '评分：' + (json.score || "") + json.period;
    }
} catch (e) {
    VOD.vod_remarks = json.subtitle;
}
VOD.vod_area = (json.focus || "") + "\n资费：" + (json.payMark === 1 ? "VIP" : "免费") + "\n地区：" + ((json.areas) || "");
let vsize = '579_772'
try {
    vsize = json.imageSize[12];
}catch (e) {}
VOD.vod_pic =  json.imageUrl.replace('.jpg', ('_'+vsize+'.jpg?caplist=jpg,webp'));
// print(VOD.vod_pic);
VOD.type_name =  json.categories.map(function (it){return it.name}).join(',');
if(json.people.main_charactor){
    let vod_actors = [];
    json.people.main_charactor.forEach(function (it){
        vod_actors.push(it.name);
    });
    VOD.vod_actor = vod_actors.join(',')
}
VOD.vod_content = json.description;
let playlists = []
if (json.channelId === 1 || json.channelId === 5) {
    playlists = [{
        "playUrl": json.playUrl,
        "imageUrl": json.imageUrl,
        //"subtitle": json.subtitle,
        "shortTitle": json.shortTitle,
        "focus": json.focus,
        "period": json.period
    }]
} else {
    if (json.channelId === 6) {
        let qs = json.period.split('-')[0];
        let listUrl = "https://pcw-api.iqiyi.com/album/source/svlistinfo?cid=6&sourceid=" + json.albumId + "&timelist=" + qs;
        // print(listUrl);
        let playData = JSON.parse(request(listUrl)).data[qs];
        playData.forEach(function (it){
            playlists.push({
                "playUrl": it.playUrl,
                "imageUrl": it.imageUrl,
                //"subtitle": it.subtitle,
                "shortTitle": it.shortTitle,
                "focus": it.focus,
                "period": it.period
            })
        });
    } else {
        let listUrl = 'https://pcw-api.iqiyi.com/albums/album/avlistinfo?aid=' + json.albumId + '&size=200&page=1';
        let data = JSON.parse(request(listUrl)).data;
        let total = data.total;
        playlists = data.epsodelist;
        if(total>200){
            for(let i=2;i<(total/200)+1;i++){
                let listUrl = 'https://pcw-api.iqiyi.com/albums/album/avlistinfo?aid=' + json.albumId + '&size=200&page='+i;
                let data = JSON.parse(request(listUrl)).data;
                playlists = playlists.concat(data.epsodelist);
            }
        }
        //log(listUrl)
    }
}
playlists.forEach(function (it){
    d.push({
            title: (it.shortTitle) || ('第' + it.order + '集'),
            desc: it.subtitle || it.focus || it.period,
            img: it.imageUrl.replace('.jpg', '_480_270.jpg?caplist=jpg,webp'),
            url: it.playUrl,
    });
});
VOD.vod_play_from = 'qiyi';
VOD.vod_play_url = d.map(function (it){
    return it.title + '$' + it.url;
}).join('#');