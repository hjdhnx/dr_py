js:
// let d = [];
// VOD = {vod_id:input};
VOD = {};
let html = request(input);

function adhead(url){
    let hd = 'https://v.sogou.com';
    if(!url.startsWith(hd)){
        url = hd+url
    }
    return urlencode(url)
}
try {
    let json = JSON.parse(html.match(/INITIAL_STATE.*?({.*});/)[1]).detail.itemData;
    let key = json.dockey;
    let name = json.name;
    let zone = json.zone;
    let score = json.score ? json.score: '暂无';
    let style = json.style;
    let emcee = json.emcee ? '主持：' + json.emcee: json.name;
    let director = json.director ? '导演：' + json.director: name;
    director = director.replace(/;/g, '\t');
    let starring = json.starring ? '演员：' + json.starring: '声优：' + json.shengyou;
    starring = starring.replace(/.*undefined/, '').replace(/;/g, '\t')
    let update = json.update_wordstr ? json.update_wordstr: '';
    let tv_station = json.tv_station ? json.tv_station: zone;
    let introduction = json.introduction;
    let shengyou = json.shengyou;
    let shows = json.play_from_open_index;
    let plays = json.play.item_list;
    if (shows) {
        VOD.vod_name = name;
        VOD.vod_area = emcee + ',' + tv_station;
        VOD.vod_director = director;
        VOD.vod_actor = starring;
        VOD.vod_pic = jsp.pd(html, '#thumb_img&&img&&src');
        VOD.vod_remarks = style + ' 评分:' + score + ',' + update;
        VOD.vod_content = introduction;
    } else {
        VOD.vod_name = name;
        // VOD.vod_area = '';
        VOD.vod_director = director;
        VOD.vod_actor = starring;
        VOD.vod_pic = jsp.pd(html, '#thumb_img&&img&&src');
        // VOD.vod_remarks = style + ' 评分:' + score + ',' + update;
        VOD.vod_content = introduction;
    }
    let tp = '&type=json';
    try {
        let tabs = [];
        let lists = [];
        plays.forEach(function (it){
            lists.push(it.info);
            let tbn = it.sitename[0]||it.site.replace('.com','');
            tbn = tbn.split('').join(' '); // 加空格防止被软件拦截
            tabs.push(tbn);
        });
        VOD.vod_play_from = tabs.join('$$$');
        // print(VOD);
        // print(lists);
        // print(shows);
        let vod_lists = []; // 拿$$$去填
        // if(typeof(play_url)==='undefined'){
        //     var play_url = '';
        // }
        print('play_url1:'+play_url);
        play_url = play_url.replace('&play_url=','&type=json&play_url=');
        print('play_url2:'+play_url);
        lists.forEach(function (item,idex){ // item是个json列表
            if (item || shows) { // 动漫,电视剧
                if(item && Array.isArray(item)&&item.length>1){
                    // let tmp = item.slice(1).map(function (its){return its.index+'$'+play_url+'https://v.sogou.com'+its.url});
                    let tmp = item.slice(1).map(function (its){return its.index+'$'+play_url+base64Encode(adhead(its.url))});
                    vod_lists.push(tmp.join('#'));
                }
                if (shows) { //综艺,纪录片
                    let arr = [];
                    let tmp = [];
                    let zy = shows.item_list[idex];
                    zy.date.forEach(function (date){
                        let day = date.day;
                        for (let j=0;j<day.length;j++) {
                            let dayy = day[j][0] >= 10 ? day[j][0] : "0" + day[j][0];
                            let Tdate = date.year + date.month + dayy;
                            arr.push(Tdate);
                        }
                    });

                    for (let k = 0; k < arr.length; k++) {
                        let url = "https://v.sogou.com/vc/eplay?query=" + arr[k] + "&date=" + arr[k] + "&key=" + key + "&st=5&tvsite=" + plays[idex].site;
                        tmp.push("第" + arr[k] + "期"+'$'+play_url+base64Encode(adhead(url)));
                    }
                    vod_lists.push(tmp.join('#'));
                }
            } else if (plays[idex].site) {//电影
                // print(plays[idex].site);
                let tmp = [];
                if (!plays[idex].flag_list.includes('trailer')) {
                    tmp.push(plays[idex].sitename[0]+'$'+play_url+base64Encode(adhead(plays[idex].url)));
                } else {
                    tmp.push(plays[idex].sitename[0] + '—预告'+'$'+play_url+base64Encode(adhead(plays[idex].url)));
                }
                vod_lists.push(tmp.join('#'));
            }
        });
        // print(vod_lists);
        VOD.vod_play_url = vod_lists.join('$$$');
    } catch(e) {
        let img = json.photo.item_list;
        VOD.vod_name = '本片无选集';
        VOD.vod_pic = img.length>0?img[0]:'';
    }
} catch(e) {
    print('发生了错误:'+e.message);
}