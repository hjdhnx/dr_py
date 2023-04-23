js:
let d = [];
let html = request(input);
html = JSON.parse(html);
let list = html.listData.results;
list.forEach(function (it){
    let desc1 = it.ipad_play_for_list.finish_episode?it.ipad_play_for_list.episode===it.ipad_play_for_list.finish_episode?"全集"+it.ipad_play_for_list.finish_episode:"连载"+it.ipad_play_for_list.episode+"/"+it.ipad_play_for_list.finish_episode:"";
    let desc2 = it.score?'评分:'+it.score:'';
    let desc3 = it.date?'更至:'+it.date:'';
    d.push({
        title: it.name,
        img: it.v_picurl,
        url: "https://v.sogou.com" + it.url.replace('teleplay', 'series').replace('cartoon', 'series'),
        desc: desc1||desc2||desc3,
    });
});
setResult(d);