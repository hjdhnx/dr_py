js:
pdfa=jsp.pdfa;
pdfa=jsp.pdfa;
pd=jsp.pd;
let d=[];
log(input);
let html=request(input);
let list=pdfa(html,'.text_list li');
let burl=input.match(/(.*)\/.*?.html/)[1];
log(burl);
MY_URL=burl;
print(list);
list.forEach(function(it){
    let title = pdfh(it,'a&&Text');
    d.push({
        title:title,
        desc:pdfh(it,'.date&&Text'),
        url:pd(it,'a&&href')+'@@'+title
    });
});
setResult(d)