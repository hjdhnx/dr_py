/**
 * 比较字符串
 * @param str1
 * @param str2
 */
function strCompare(str1, str2) {
    // 处理数据为null的情况
    if (str1 == undefined && str2 == undefined) {
        return 0;
    }
    if (str1 == undefined) {
        return -1;
    }
    if (str2 == undefined) {
        return 1;
    }

    // 比较字符串中的每个字符
    let c1;
    let c2;

    let regexArr = ['-', '_', '—', '~', '·'], canRegex = /[^0-9\.]/g;
    // 如果都不是数字格式（含有其它内容）
    if (canRegex.test(str1) && canRegex.test(str2)) {
        for (let i = 0; i < regexArr.length; i++) {
            let regex = eval('(/[^0-9\\' + regexArr[i] + '\\.]/g)');
            // 去除后缀
            let tps1 = str1.replace(/\.[0-9a-zA-Z]+$/, '');
            let tps2 = str2.replace(/\.[0-9a-zA-Z]+$/, '');
            // 如果在名字正则要求范围内（没有正则以外的值）
            if (!regex.test(tps1) && !regex.test(tps2)) {
                // 转换为字符串数组
                let numberArray1 = tps1.split(regexArr[i]);
                let numberArray2 = tps2.split(regexArr[i]);
                return compareNumberArray(numberArray1, numberArray2);
            }
        }
    }

    // 逐字比较返回结果
    for (let i = 0; i < str1.length; i++) {
        c1 = str1[i];
        if (i > str2.length - 1) { // 如果在该字符前，两个串都一样，str2更短，则str1较大
            return 1;
        }
        c2 = str2[i];
        // 如果都是数字的话，则需要考虑多位数的情况，取出完整的数字字符串，转化为数字再进行比较
        if (isNumber(c1) && isNumber(c2)) {
            let numStr1 = "";
            let numStr2 = "";
            // 获取数字部分字符串
            for (let j = i; j < str1.length; j++) {
                c1 = str1[j];
                if (!isNumber(c1) && c1 !== '.') { // 不是数字则直接退出循环
                    break;
                }
                numStr1 += c1;
            }
            for (let j = i; j < str2.length; j++) {
                c2 = str2[j];
                if (!isNumber(c2) && c2 !== '.') {
                    break;
                }
                numStr2 += c2;
            }
            // 将带小数点的数字转换为数字字符串数组
            let numberArray1 = numStr1.split('.');
            let numberArray2 = numStr2.split('.');
            return compareNumberArray(numberArray1, numberArray2);
        }

        // 不是数字的比较方式
        if (c1 != c2) {
            return c1 - c2;
        }
    }
    return 0;
}

/**
 * 判断是否为数字
 * @param obj
 * @returns
 */
function isNumber(obj) {
    if (parseFloat(obj).toString() == "NaN") {
        return false;
    }
    return true;
}

/**
 * 比较两个数字数组
 *
 * @param numberArray1
 * @param numberArray2
 */
export function compareNumberArray(numberArray1, numberArray2) {
    for (let i = 0; i < numberArray1.length; i++) {
        if (numberArray2.length < i + 1) { // 此时数字数组2比1短，直接返回
            return 1;
        }
        let compareResult = parseInt(numberArray1[i]) - parseInt(numberArray2[i]);
        if (compareResult !== 0) {
            return compareResult;
        }
    }
    // 说明数组1比数组2短，返回小于
    return -1;
}


/**
 * 自然排序
 * ["第1集","第10集","第20集","第2集","1","2","10","12","23","01","02"].sort(naturalSort())
 * @param options { direction: 'desc', caseSensitive: true }
 */
export function naturalSort(options) {
    if (!options) options = {};

    return function (a, b) {
        var EQUAL = 0;
        var GREATER = (options.direction == 'desc' ?
                -1 :
                1
        );
        var SMALLER = -GREATER;

        var re = /(^-?[0-9]+(\.?[0-9]*)[df]?e?[0-9]?$|^0x[0-9a-f]+$|[0-9]+)/gi;
        var sre = /(^[ ]*|[ ]*$)/g;
        var dre = /(^([\w ]+,?[\w ]+)?[\w ]+,?[\w ]+\d+:\d+(:\d+)?[\w ]?|^\d{1,4}[\/\-]\d{1,4}[\/\-]\d{1,4}|^\w+, \w+ \d+, \d{4})/;
        var hre = /^0x[0-9a-f]+$/i;
        var ore = /^0/;

        var normalize = function normalize(value) {
            var string = '' + value;
            return (options.caseSensitive ?
                    string :
                    string.toLowerCase()
            );
        };

        // Normalize values to strings
        var x = normalize(a).replace(sre, '') || '';
        var y = normalize(b).replace(sre, '') || '';

        // chunk/tokenize
        var xN = x.replace(re, '\0$1\0').replace(/\0$/, '').replace(/^\0/, '').split('\0');
        var yN = y.replace(re, '\0$1\0').replace(/\0$/, '').replace(/^\0/, '').split('\0');

        // Return immediately if at least one of the values is empty.
        if (!x && !y) return EQUAL;
        if (!x && y) return GREATER;
        if (x && !y) return SMALLER;

        // numeric, hex or date detection
        var xD = parseInt(x.match(hre)) || (xN.length != 1 && x.match(dre) && Date.parse(x));
        var yD = parseInt(y.match(hre)) || xD && y.match(dre) && Date.parse(y) || null;
        var oFxNcL, oFyNcL;

        // first try and sort Hex codes or Dates
        if (yD) {
            if (xD < yD) return SMALLER;
            else if (xD > yD) return GREATER;
        }

        // natural sorting through split numeric strings and default strings
        for (var cLoc = 0, numS = Math.max(xN.length, yN.length); cLoc < numS; cLoc++) {

            // find floats not starting with '0', string or 0 if not defined (Clint Priest)
            oFxNcL = !(xN[cLoc] || '').match(ore) && parseFloat(xN[cLoc]) || xN[cLoc] || 0;
            oFyNcL = !(yN[cLoc] || '').match(ore) && parseFloat(yN[cLoc]) || yN[cLoc] || 0;

            // handle numeric vs string comparison - number < string - (Kyle Adams)
            if (isNaN(oFxNcL) !== isNaN(oFyNcL)) return (isNaN(oFxNcL)) ? GREATER : SMALLER;

            // rely on string comparison if different types - i.e. '02' < 2 != '02' < '2'
            else if (typeof oFxNcL !== typeof oFyNcL) {
                oFxNcL += '';
                oFyNcL += '';
            }
            if (oFxNcL < oFyNcL) return SMALLER;
            if (oFxNcL > oFyNcL) return GREATER;
        }
        return EQUAL;
    };
}