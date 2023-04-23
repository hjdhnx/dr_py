js:
var d=[];
VOD={vod_id:input};
// print(input);
try {
let html=request(input);
print(html);
html = JSON.parse(html);
let node = html.data;
VOD = {
    "vod_id":node['id'],
    "vod_name":node['videoName'],
    "vod_pic":node['videoCover'],
    "type_name":node['subCategory'],
    "vod_year":node['year'],
    "vod_area":node['area'],
    "vod_remarks":node['msg'],
    "vod_actor":node['actor'],
    "vod_director":node['director'],
    "vod_content":node['brief'].strip()
}
// print(VOD);
let tid = input.split('ids=')[1];
let listUrl = 'http://api.kunyu77.com/api.php/provide/videoPlaylist?devid=453CA5D864457C7DB4D0EAA93DE96E66&package=com.sevenVideo.app.android&version=1.8.7&ids='+tid;
html = request(listUrl);
html = JSON.parse(html);
let episodes = html.data.episodes;
let playMap = {};
if(typeof(play_url)==='undefined'){
    var play_url = '';
}
play_url = play_url.replace('&play_url=','&type=json&play_url=');
episodes.forEach(function (ep){
    let playurls = ep['playurls'];
    playurls.forEach(function (playurl){
        let source = playurl['playfrom'];
        if(!playMap.hasOwnProperty(source)){
            playMap[source] = [];
        }
        playMap[source].append(playurl['title'].strip() + '$' + play_url+urlencode(playurl['playurl']));
    });

});

let playFrom = [];
let playList = [];
Object.keys(playMap).forEach(function (key){
    playFrom.append(key);
    playList.append(playMap[key].join('#'));
});
// print(playFrom);
// print(playList);
let vod_play_from = playFrom.join('$$$');
let vod_play_url = playList.join('$$$');
VOD['vod_play_from'] = vod_play_from;
VOD['vod_play_url'] = vod_play_url;
// print(VOD);
}catch (e) {
    log('获取二级详情页发生错误:'+e.message);
}