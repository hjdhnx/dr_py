js:
var d = [];
let html=request(input);
let json = JSON.parse(html);
// print(json);
json.pageComponentList.forEach(function (it){
    if (it.hasOwnProperty('commonData')) {
        it = it.commonData;
        d.push({
            title: it.titleDTO.displayName,
            img: it.posterDTO.vThumbUrl,
            // desc: it.feature,
            desc: it.stripeBottom,
            content: it.updateNotice+' '+it.feature,
            url: 'https://search.youku.com/api/search?appScene=show_episode&showIds=' + it.showId + '&appCaller=h5'
        });
    }
});
setResult(d);