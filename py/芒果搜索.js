js:
fetch_params.headers.Referer = 'https://www.mgtv.com';
fetch_params.headers['User-Agent'] = UA;
let d = [];
let html = request(input);
let json = JSON.parse(html);
json.data.contents.forEach(function (data){
    if (data.data.sourceList || data.data.yearList) {
        let list = data.data.sourceList ? data.data.sourceList : data.data.yearList[0].sourceList;
        let desc = '';
        list.forEach(function (it){
            desc += it.name + '\t';
        });
        if (list[0].source === 'imgo') {
            let img = data.data.pic ? data.data.pic : data.data.yearList[0].pic;
            d.push({
                title: data.data.title ? data.data.title : data.data.yearList[0].title,
                img:img ,
                content: data.data.story ? data.data.story : data.data.yearList[0].story,
                desc: data.data.playTime,
                url: list[0].vid
            });
        }
    }
});
setResult(d);