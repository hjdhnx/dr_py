js:
// log(input);
let url=input.split(";")[0];
let d = [];
let body={searchword:input.split(";")[1]};
fetch_params.body=body;
let html = post(url,fetch_params);
// print(html);\
let pdfa = jsp.pdfa;
let pdfh = jsp.pdfh;
let pd = jsp.pd;
let lists = pdfa(html,'ul.stui-vodlist__media&&li');
lists.forEach(function (it){
   d.push({
       title:pdfh(it,'.title&&Text'),
       url:pd(it,'a&&href'),
       desc:pdfh(html,'.pic-text&&Text'),
       pic_url:pd(html,'.lazyload&&data-original'),
   });
});
setResult(d);