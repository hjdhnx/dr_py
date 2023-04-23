js:
let d=[];
let html = request(input);
// print(html);
let jsonA = JSON.parse(html.match(/INITIAL_STATE.*?({.*});/)[1]);
print(jsonA);
jsonA = jsonA.result.longVideo.results;
jsonA.forEach(function (it){
    let name=it.name;
    let introduction=it.introduction;
    let pic= it.v_picurl;
    let url= it.tiny_url;
    let zone=it.zone;
    let score=it.score||'暂无';
    let style=it.style;
    if(it.play.item_list){
        let r = {};
        r.title = name.replace(//,'').replace(//,'');
        r.url= 'https://v.sogou.com'+url;
        r.desc = it.list_category.join(',');
        r.content= introduction;
        r.pic_url= pic;
        d.push(r);
    }
});
// print(d);
setResult(d);