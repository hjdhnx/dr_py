js:
let d = [];
pdfa=jsp.pdfa;pdfh=jsp.pdfh;pd=jsp.pd;
let html = request(input);
let baseList=pdfa(html,'body&&.result_item_v');
baseList.forEach(function(it){
    let longText=pdfh(it,'.result_title&&Text');
    let shortText=pdfh(it,'.sub&&Text');
    let fromTag=pdfh(it,'.result_source&&Text');
    let score=pdfh(it,'.result_score&&Text');
    let content=pdfh(it,'.desc_text&&Text');
    let url=pdfh(it,'.result_title&&a&&href');
    // log(url);
    let img= pd(it,'.figure_pic&&src');
    url='https://node.video.qq.com/x/api/float_vinfo2?cid='+url.match(/.*\/(.*?)\.html/)[1];
    log(shortText+'|'+url);
    if (fromTag.match(/腾讯/)) {
       d.push({
        title: longText.split(shortText)[0],
        img: img,
        url: url,
        content:content,
        desc:"⭐"+longText.split(shortText)[1]+'-'+shortText+' '+score
    });
    }
});
setResult(d);