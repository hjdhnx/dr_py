js:
// 将超过10000的数字换成成以万和亿为单位
function zh(num){
    let p='';
    if(Number(num)>100000000){
        p = (num/100000000).toFixed(2)+'亿';
    }else if(Number(num)>10000){
        p = (num/10000).toFixed(2)+'万';
    }else{
        p = num;
    }
    return p
}
let html = request(input);
let jo = JSON.parse(html).result;
let id = jo['season_id'];
let title = jo['title'];
let pic = jo['cover'];
let areas = jo['areas'][0]['name'];
let typeName = jo['share_sub_title'];
let date = jo['publish']['pub_time'].substr(0,4);
let dec = jo['evaluate'];
let remark = jo['new_ep']['desc'];
let stat = jo['stat'];
let status = "弹幕: " + zh(stat['danmakus']) + "　点赞: " + zh(stat['likes']) + "　投币: " + zh(stat['coins']) + "　追番追剧: " + zh(stat['favorites']);
let score = jo.hasOwnProperty('rating')?"评分: " + jo['rating']['score'] + '　' + jo['subtitle']:"暂无评分" + '　' + jo['subtitle'];
let vod = {
"vod_id": id,
"vod_name": title,
"vod_pic": pic,
"type_name": typeName,
"vod_year": date,
"vod_area": areas,
"vod_remarks": remark,
"vod_actor": status,
"vod_director": score,
"vod_content": dec
}
let ja = jo['episodes'];
let playurls1 = [];
let playurls2 = [];
ja.forEach(function (tmpJo){
    let eid = tmpJo['id'];
    let cid = tmpJo['cid'];
    let link = tmpJo['link'];
    let part = tmpJo['title'].replace("#", "-")+' '+tmpJo['long_title'];
    playurls1.push(part+'$'+eid+'_'+cid);
    playurls2.push(part+'$'+link);
});
let playUrl = playurls1.join('#')+'$$$'+playurls2.join('#');
vod['vod_play_from'] = 'B站$$$bilibili'
vod['vod_play_url'] = playUrl
VOD = vod;