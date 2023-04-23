js:
var items = [];
var video_list = [];
var list = [];
eval(fetch('hiker://files/rules/js/g-parse-list.js', {}).split('eval(getCryptoJS());')[0]);

function toUrl(mode, url) {
    if (typeof mode === 'number') {
        if (mode === 0) {
            return 'hiker://empty#' + url + `@rule=js:var items = []; var origin_url = MY_URL.split('#')[1]; eval(fetch('hiker://files/rules/js/g-parse-list.js', {}).split('eval(getCryptoJS());')[0]); items.push({ title: '直链解析合集', col_type: 'text_1' }); for (var i in sort_json['qq']) { var parse_list_arr = parse_list[sort_json['qq'][i]].split('￥'); items.push({ title: parse_list_arr[0], url: parse_list_arr[1] + origin_url + parse_list_arr[2], col_type: 'text_2' }) } items.push({ title: '网页解析合集', col_type: 'text_1' }); for (var i in parsing_list) { var parsing_list_arr = parsing_list[i].split('￥'); items.push({ title: parsing_list_arr[0], url: parsing_list_arr[1] + origin_url, col_type: 'text_3' }) } setHomeResult({ data: items });`;
        } else if (mode <= parse_list.length) {
            return parsing_list[mode - 1].split('￥')[1] + url;
        }
    } else if (typeof mode === 'string') {
        for (var key in parse_list) {
            if (parse_list[key].indexOf(mode) > -1) {
                return parse_list[key].split('￥')[1] + url + parse_list[key].split('￥')[2];
            }
        }
    }
    return url;
}
if (MY_URL.indexOf('get_playsource') > 0) {
    var video_lists = [];
    eval(getResCode());
    var indexList = QZOutputJson.PlaylistItem.indexList;
    for (var i in indexList) {
        eval(fetch('https://s.video.qq.com/get_playsource?id=' + MY_URL.match(/id=(\d*?)&/)[1] + '&plat=2&type=4&data_type=3&range=' + indexList[i] + '&video_type=10&plname=qq&otype=json', {}));
        video_lists.push.apply(video_lists, QZOutputJson.PlaylistItem.videoPlayList);
    }
    for (var i in video_lists) {
        var data = video_lists[i];
        list.push(data.title + '￥' + data.playUrl);
        items.push({
            title: data.title,
            pic_url: data.pic,
            desc: data.episode_number + '\t\t\t播放量：' + data.thirdLine,
            url: getVar('cj','断插')=='直链'?toUrl(qq_mode, data.playUrl):($(data.playUrl).lazyRule(() => {
var config=JSON.parse(fetch("hiker://files/cache/MyParseSet.json")); eval(fetch(config.cj));
return aytmParse(input);
                    })),
            col_type: 'movie_1'
        });
    }
} else {
    var json = JSON.parse(getResCode());
    var video_lists = json.c.video_ids;
    var cid = MY_URL.split('cid=')[1];
    var url = 'https://v.qq.com/x/cover/' + cid + '.html';
/*    if (json.c.type == 100&&json.c.clips_ids!=null) {
        eval(fetch('https://s.video.qq.com/get_playsource?id=' + json.c.column_id + '&plat=2&type=2&data_type=3&video_type=8&plname=qq&otype=json', {}));
        var video_lists = [];
        var indexList = QZOutputJson.PlaylistItem.indexList;
        for (var i in indexList) {
            eval(fetch('https://s.video.qq.com/get_playsource?id=' + json.c.column_id + '&plat=2&type=4&data_type=3&range=' + indexList[i] + '&video_type=10&plname=qq&otype=json', {}));
            video_lists.push.apply(video_lists, QZOutputJson.PlaylistItem.videoPlayList);
        }
        for (var i in video_lists) {
            var data = video_lists[i];
            list.push(data.title + '￥' + data.playUrl);
            items.push({
                title: data.title,
                pic_url: data.pic,
                desc: data.episode_number + '\t\t\t播放量：' + data.thirdLine,
                url: getVar('cj','断插')=='直链'?toUrl(qq_mode, data.playUrl):($(data.playUrl).lazyRule(() => {
var config=JSON.parse(fetch("hiker://files/cache/MyParseSet.json")); eval(fetch(config.cj));
return aytmParse(input);
                    })),
                col_type: 'movie_1'
            });
        }
    } else */
    if (video_lists.length == 1) {
        items.push({
            title: '直链解析',
            col_type: 'text_1'
        });
        for (var i in sort_json['qq']) {
            var parse_list_arr = parse_list[sort_json['qq'][i]].split('￥');
            items.push({
                title: parse_list_arr[0],
                url: getVar('cj','断插')=='直链'?(parse_list_arr[1] + url + parse_list_arr[2]):($(url).lazyRule(() => {
var config=JSON.parse(fetch("hiker://files/cache/MyParseSet.json")); eval(fetch(config.cj));
return aytmParse(input);
                    })),
                col_type: 'text_2'
            });
        }
        items.push({
            title: '网页解析',
            col_type: 'text_1'
        });
        for (var i = 0; i < parsing_list.length; i++) {
            items.push({
                title: parsing_list[i].split('￥')[0],
                url: parsing_list[i].split('￥')[1] + url,
                col_type: 'text_3'
            });
        }
    } else if (video_lists.length > 1) {
        for (var i = 0; i < video_lists.length; i += 30) {
            video_list.push(video_lists.slice(i, i + 30));
        }
        for (var i = 0; i < video_list.length; i++) {
            var o_url = 'https://union.video.qq.com/fcgi-bin/data?otype=json&tid=682&appid=20001238&appkey=6c03bbe9658448a4&union_platform=1&idlist=' + video_list[i].join(',');
            eval(fetch(o_url, {}));
            var col_type = QZOutputJson.results[0].fields.title.length > 12 ? 'movie_1' : 'movie_2';
            for (var j = 0; j < QZOutputJson.results.length; j++) {
                var data = QZOutputJson.results[j].fields;
                var url = 'https://v.qq.com/x/cover/' + cid + '/' + data.vid + '.html';
                list.push(data.title + '￥' + url);
                items.push({
                    title: data.title,
                    pic_url: data.pic160x90,
                    desc: data.video_checkup_time,
                    url: getVar('cj', '断插') == '直链' ? toUrl(qq_mode, url) : ($(url).lazyRule(() => {
var config=JSON.parse(fetch("hiker://files/cache/MyParseSet.json")); eval(fetch(config.cj));
return aytmParse(input);
                    })),
                    col_type: col_type
                });
            }
        }
    } else {
        items.push({
            title: '原网页',
            url: 'https://v.qq.com/x/cover/' + cid + '.html',
            col_type: 'text_center_1'
        });
    }
}
if (MY_URL.indexOf('get_playsource') > 0 || json.c.type == 10 || video_lists.length > 1) {
    items.unshift({
        title: '默认设置',
        url: 'hiker://empty' + `@rule=js:var items = []; eval(fetch('hiker://files/rules/js/g-parse-list.js', {}).split('eval(getCryptoJS());')[0]); var tip = "hiker://empty@lazyRule=.js:'toast://别点了,再点就坏了,要讲点武德'"; if (qq_mode == 0) { items.push({ title: '解析集合页✔', url: tip, col_type: 'text_2' }); } else { items.push({ title: '解析集合页', url: "hiker://empty@lazyRule=.js:var html = fetch('hiker://files/rules/js/g-parse-list.js', {});writeFile('hiker://files/rules/js/g-parse-list.js', html.replace(/var qq_mode.*?;/,'var qq_mode = 0;'));refreshPage();'toast://已设置为解析集合页'", col_type: 'text_2' }); }items.push({col_type: 'line' });for (var i in sort_json['qq']) { var index = sort_json['qq'][i]; var title = parse_list[index].split('￥')[0]; if (isNaN(qq_mode) && parse_list[index].indexOf(qq_mode) >= 0) { items.push({ title: title + '✔', url: tip, col_type: 'text_2' }); } else { items.push({ title: title, url: "hiker://empty@lazyRule=.js:var html = fetch('hiker://files/rules/js/g-parse-list.js', {});writeFile('hiker://files/rules/js/g-parse-list.js', html.replace(/var qq_mode.*?;/,'var qq_mode = " + '"' + title + '"' + ";'));refreshPage();'toast://已设置为" + title + "'", col_type: 'text_2' }); } }items.push({col_type: 'line' }); for (var i in parsing_list) { var title = parsing_list[i].split('￥')[0]; var mode = parseInt(i) + 1; if (qq_mode == mode) { items.push({ title: title + '✔', url: tip, col_type: 'text_3' }); } else { items.push({ title: title, url: "hiker://empty@lazyRule=.js:var html = fetch('hiker://files/rules/js/g-parse-list.js', {});writeFile('hiker://files/rules/js/g-parse-list.js', html.replace(/var qq_mode.*?;/,'var qq_mode = " + mode + ";'));refreshPage();'toast://已设置为" + title + "'", col_type: 'text_3' }); } } if (isNaN(qq_mode) && qq_mode.indexOf('北极XS') >= 0) { items.push({ title: '以下设置仅在北极XS中有效', col_type: 'text_1' }); for (var key in qq_sharpness_sets) { if (qq_sharpness_sets[key] == qq_sharpness) { items.push({ title: key + '✔', url: tip, col_type: 'text_4' }); } else { items.push({ title: key, url: "hiker://empty@lazyRule=.js:var html = fetch('hiker://files/rules/js/g-parse-list.js', {});writeFile('hiker://files/rules/js/g-parse-list.js', html.replace(/var qq_sharpness =.*?;/,'var qq_sharpness = " + '"' + qq_sharpness_sets[key] + '"' + ";'));refreshPage();'toast://已设置为" + key + "'", col_type: 'text_4' }); } } } setHomeResult({ data: items });`,
        col_type: 'text_3'
    });
    items.unshift({
        title: "网页解析",
        url: 'hiker://empty' + `@rule=js:var res={};var items=[];var list = ["` + list.join('","') + `"];var parsing_list=["` + parsing_list.join('","') + `"];for(var i=0;i<parsing_list.length;i++){items.push({title:parsing_list[i].split('￥')[0]+' ==>',col_type:'text_1'});for(var j=0;j<list.length;j++){items.push({title:list[j].split('￥')[0],url:parsing_list[i].split('￥')[1]+list[j].split('￥')[1],col_type:((list[j].split('￥')[0].length)>10?'text_1':'text_2')})}}res.data=items;setHomeResult(res);`,
        col_type: 'text_3'
    });
    /* items.unshift({
         title: "直链解析",
         url: set_switch/*'hiker://empty' + `@rule=js:var items = [];var list = ["` + list.join('","') + `"]; eval(fetch('hiker://files/rules/js/g-parse-list.js', {}).split('eval(getCryptoJS());')[0]); for (var i in sort_json['qq']) { var parse_list_arr = parse_list[sort_json['qq'][i]].split('￥'); items.push({title:parse_list_arr[0]+' ==>',col_type:'text_1'}); for(var j=0;j<list.length;j++){ items.push({title:list[j].split('￥')[0],url:parse_list_arr[1]+list[j].split('￥')[1]+parse_list_arr[2],col_type:((list[j].split('￥')[0].length)>10?'text_1':'text_2')}) } } setHomeResult({ data: items });`,
         col_type: 'text_3'
     });*/
}
(function() {
    if (getVar('cj', '断插') == '断插') {
        eval(JSON.parse(request('hiker://page/a2')).rule);
        items.unshift({
            title: getVar('cj', '断插'),
            url: '#noHistory#'+set,
            col_type: 'text_3'
        })
    } else {
        eval(JSON.parse(request('hiker://page/a1')).rule)
    };
})();
setHomeResult({
    data: items
});