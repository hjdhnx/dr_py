js:
let ep=input.match(/ep=(\d+)/)[1];
let html=request(input);
let jsonA=jsp.pdfh(html,'#__NEXT_DATA__&&Html');
let data=JSON.parse(jsonA).props.pageProps.videoDetail.videoepisode.data;
let realUrl=data.filter(function(it){
    return it.episode==ep
})[0].url;
input = realUrl