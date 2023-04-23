const DOM_CHECK_ATTR = /(url|src|href|-original|-src|-play|-url)$/;
const SELECT_REGEX = /:eq|:lt|:gt|#/g;
const SELECT_REGEX_A = /:eq|:lt|:gt/g;
const parseTags = {
    jq:{
        pdfh(html, parse, base_url) {
            if (!parse || !parse.trim()) {
                return ''
            }
            parse = parse.trim();
            let option = null;
            if (parse.startsWith('body&&')) {
                parse = parse.substr(6);
            }
            print('pdfh parse前:'+parse);
            if (parse.indexOf('&&') > -1) {
                let sp = parse.split('&&');
                option = sp[sp.length - 1];
                sp.splice(sp.length - 1);
                sp.forEach((it,idex)=>{
                    if(/:eq\((.*?)\)/.test(it)){
                        let pos = parseInt(it.match(/:eq\((.*?)\)/)[1]);
                        if(pos >= 0 ){ // jsoup的eq 正整数从1开始
                            it = it.replace(/:eq\((.*?)\)/,`:eq(${pos+1})`);
                            sp[idex] = it;
                        }
                    }else if (!SELECT_REGEX.test(it) && it!=='body') {
                        sp[idex] = it+':eq(1)'; // jsoup的eq从1开始
                    }
                });
                parse = sp.join(' ');
            }
            if(parse === 'Text'){
                parse = 'body';
                option = 'Text';
            }else if(parse === 'Html'){
                parse = 'body';
                option = 'Html';
            }
            print('pdfh parse后:'+parse+',option:'+option);
            let result = defaultParser.pdfh(html,parse + " " + option);
            print(result);
            if(option&&/style/.test(option.toLowerCase())&&/url\(/.test(result)){
                try {
                    result =  result.match(/url\((.*?)\)/)[1];
                }catch (e) {}
            }
            if (result && base_url && option && DOM_CHECK_ATTR.test(option)) {
                if (/http/.test(result)) {
                    result = result.substr(result.indexOf('http'));
                } else {
                    result = urljoin(base_url, result)
                }
            }
            return result;
        },
        pdfa(html, parse) {
            if (!parse || !parse.trim()) {
                print('!parse');
                return [];
            }
            parse = parse.trim();
            print('pdfa parse前:'+parse);
            if (parse.indexOf('&&') > -1) {
                let sp = parse.split('&&');
                sp.forEach((it,idex)=>{
                    if(/:eq\((.*?)\)/.test(it) && idex < sp.length - 1){
                        let pos = parseInt(it.match(/:eq\((.*?)\)/)[1]);
                        if(pos >= 0 ){ // jsoup的eq 正整数从1开始
                            it = it.replace(/:eq\((.*?)\)/,`:eq(${pos+1})`);
                            sp[idex] = it;
                        }
                    }else if (!SELECT_REGEX_A.test(it) && idex < sp.length - 1 && it!=='body') {
                        sp[idex] = it+':eq(1)'; // jsoup的eq从1开始
                    }
                });
                parse = sp.join(' ');
            }
            print('pdfa parse后:'+parse);
            let result = defaultParser.pdfa(html,parse);
            // print(result);
            print(result.length);
            return result;
        },
        pd(html,parse,uri){
            return parseTags.jq.pdfh(html, parse, MY_URL);
        },
    },
};