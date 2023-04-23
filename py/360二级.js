js:
// 请不要在里面使用单引号
// let html = fetch(input,fetch_params);
let html = JSON.parse(fetch(input,fetch_params));
let data = html.data;
// let tilte = jsp.pjfh(html,"data.title");
let tilte = data.title;
// let img = jsp.pj(html,"data.cdncover");
let img = data.cdncover;
// let vod_type = jsp.pjfa(html,"data.moviecategory").join(",");
let vod_type = data.moviecategory.join(",");
// let area = jsp.pjfa(html,"data.area").join(",");
let area = data.area.join(",");
// let director = jsp.pjfa(html,"data.director").join(",");
let director = data.director.join(",");
// let actor = jsp.pjfa(html,"data.actor").join(",");
let actor = data.actor.join(",");
// let content = jsp.pjfh(html,"data.description");
let content = data.description;
let base_vod = {
    vod_id:input,
    vod_name:tilte,
    type_name:vod_type,
    vod_actor:actor,
    vod_director:director,
    vod_content:content,
    vod_remarks:area,
    vod_pic:urljoin2(input,img),
    // vod_pic:img,
};
let delta = 200;
let vod_play = {};
// let sites = jsp.pjfa(html,"data.playlink_sites"); //data.playlinksdetail.#idv.quality
let sites = data.playlink_sites; //data.playlinksdetail.#idv.quality
sites.forEach(function (site){
    let playList = "";
    let vodItems = [];
    if(data.allupinfo){
        let total = parseInt(data.allupinfo[site]);
        // print('total:'+String(total));
        for(let j=1;j<total;j+=delta){
            let end = Math.min(total,j + delta-1);
            let url2 = buildUrl(input,{
                            "start": j,
                            "end": end,
                            "site": site
                        });
            // print(url2);
            let vod_data = JSON.parse(fetch(url2),fetch_params).data;
            if(vod_data.allepidetail){ //电视剧或者动漫
                vod_data = vod_data.allepidetail[site];
                vod_data.forEach(function(item,index) {
                    vodItems.push((item.playlink_num||"") + "$" + urlDeal(item.url||""));
                });
            }else{// 综艺
                vod_data = vod_data.defaultepisode;
                vod_data.forEach(function(item,index) {
                    vodItems.push((item.period||"")+(item.name||"") + "$" + urlDeal(item.url)||"");
                });
            }
        }
    }else{
        // print(data.playlinksdetail);
        let item = data.playlinksdetail[site];
        vodItems.push((item.sort||"") + "$" +urlDeal(item.default_url||""));
    }
    if(vodItems.length > 0){
       playList = vodItems.join("#");
    }
    // print(playList);
    if(playList.length < 1){
       return
    }
    vod_play[site]=playList;
});
// print(vod_play);
let tabs = Object.keys(vod_play);
// let playUrls = Object.values(vod_play); // 没法使用values方法和列表的join方法
let playUrls = [];
for(let id in tabs){
    print('id:'+id);
    playUrls.push(vod_play[tabs[id]]);
}
// print(tabs);
// print(playUrls);
if(tabs.length>0){
   // vod_play_from = join(tabs,"$$$");
   let vod_play_from = tabs.join("$$$");
   // vod_play_url = join(playUrls,"$$$");
   let vod_play_url = playUrls.join("$$$");
   // print(vod_play_from);
   // print(vod_play_url);
   base_vod.vod_play_from = vod_play_from;
   base_vod.vod_play_url = vod_play_url;
}
VOD = base_vod;
// print(VOD);