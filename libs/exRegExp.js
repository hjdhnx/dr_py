/**
 * 字符串分段处理
 * @param {String} code 处理字符串
 * @param {Array} options 分段数组
 * @param {Array<Function|Boolean>} maps 分段映射函数
 * @param {Boolean} all 是否完全映射
 * @returns {Array} 映射结果
 */
function tsCode(code, options, maps, all) {
    let start = 0, res = [];
    if (maps) {
        if (typeof maps === 'function') {
            options.forEach((part, index) => {
                res.push(maps(code.slice(start, part + start)));
                start += part;
            });
        } else {
            options.forEach((part, index) => {
                if (typeof maps[index] === 'function') {
                    res.push(maps[index](code.slice(start, part + start)));
                } else if (maps[index] !== undefined) {
                    if (maps[index] === true) res.push(code.slice(start, part + start));
                    else res.push(maps[index]);
                } else if (all) res.push(code.slice(start, part + start));
                start += part;
            });
        };
        return res
    } else {
        options.forEach(part => {
            res.push(code.slice(start, part + start));
            start += part;
        });
        return res
    }
}

function range(end, start = 0, reverse) {
    if (reverse) {
        const arr = [];
        for (let i = end; i >= start; i--) {
            arr.push(i);
        };
        return arr;
    } else {
        const arr = [];
        for (let i = start; i <= end; i++) {
            arr.push(i);
        };
        return arr;
    }
}

/**
 * 正则函数调用及函数结果插入递归替换
 * [[mark=func:regExp]] //正则函数调用(标记与函数不同名)
 * [[func:regExp]] //正则函数调用(标记与函数同名)
 * [[mark|func]] //按标记插入结果
 * @param {RegExp} reg 
 */
function splitRegExp({ oldRes, source, flags, split, res, fns, str, old, lastIndex, oldReg, oldLeft, oldRight, inner, oldSource }) {
    function next() {//回溯处理
        const oldData = old[old.length - 1];
        if (oldData) {
            const lefts = res[oldData.oldLeft];
            if (Array.isArray(lefts)) {
                return splitRegExp({ oldRes, flags, split, fns, str, old, ...oldData });
            } else {
                return splitRegExp({ oldRes, flags, split, fns, str, old, ...old.pop() });
            }
        }
    };

    if (oldReg) {//回溯处理
        let oldNum, leftRes;
        if (Array.isArray(res[oldLeft])) {
            res[oldLeft].shift();
            leftRes = oldRes[oldLeft] = res[oldLeft][0];
            if (res[oldLeft].reg[0]) {
                res[oldLeft].reg.shift();
                inner = res[oldLeft].reg[0];
            };
            if (leftRes.length === 1) {
                oldNum = 0;
            }
        } else {
            oldNum = 1;
        }

        let reg = inner ? (
            source = tsCode(oldSource, [lastIndex, res[oldLeft].len, Infinity], {
                1: `(?:${inner})`  //从结果池中以标记为键读取插入到原始正则之中
            }, true).join(''),
            new RegExp(inner, flags)
        ) : oldReg,
            mats = reg.exec(str);

        switch (oldNum) {
            case 0:
                old[old.length - 1] = { lastIndex, oldSource, source, oldReg: reg, oldLeft, oldRight, res: { ...res, [oldLeft]: leftRes }, inner };
                break;
            case 1:
                res[oldLeft] = fns[oldRight](mats, reg);
                old.push({ lastIndex, oldSource, source, oldReg: reg, oldLeft, oldRight, res: { ...res } });
                break;
        };

        return splitRegExp({ oldRes, source, flags, split, res, fns, str, old });

    } else {
        const mat = split.exec(source);//匹配函数调用点或函数结果插入点
        if (mat) {
            let lastIndex = mat.index, so = mat[1], index = so.indexOf(':');
            if (index !== -1) {//函数调用点
                let [first, last] = tsCode(so, [index, 1, Infinity], {
                    0: true,
                    2: true
                }),
                    reg = new RegExp(last, flags),
                    mats = reg.exec(str);
                if (mats) {//匹配成功递归处理
                    const index2 = first.indexOf('='),
                        [left, right] = index2 === -1 ? [first, first] : tsCode(first, [index2, 1, Infinity], {
                            0: true,
                            2: true
                        }), fnRes = fns[right](mats, reg);
                    res[left] = fnRes;
                    if (Array.isArray(fnRes)) {
                        fnRes.len = mat[0].length;
                        if (fnRes.reg[0]) last = fnRes.reg[0];
                        oldRes[left] = fnRes[0];
                    };
                    const oldSource = source;
                    source = tsCode(source, [lastIndex, mat[0].length, Infinity], {
                        1: `(?:${last})`  //从结果池中以标记为键读取插入到原始正则之中
                    }, true).join('');
                    old.push({ lastIndex, oldSource, source, oldReg: reg, oldLeft: left, oldRight: right, res: { ...res } });
                    return splitRegExp({ oldRes, source, flags, split, res, fns, str, old });
                } else return next();
            } else {//函数结果插入点
                const [lenStr, name] = mat;
                let inner;
                if (res[name] === undefined) {
                    try {
                        inner = fns[name]();
                        if (inner === undefined) return next();
                    } catch (e) {
                        return //函数中主动抛出错误,触发匹配失败返回
                    }
                } else if (Array.isArray(res[name])) {
                    inner = oldRes[name];
                } else {
                    inner = res[name]
                };
                source = tsCode(source, [lastIndex, lenStr.length, Infinity], {
                    1: inner  //从结果池中以标记为键读取插入到原始正则之中
                }, true).join('');
                return splitRegExp({ oldRes, source, flags, split, res, fns, str, old });
            }
        } else {
            return { source, next }
        };

    };
};

/**
 * 增强正则工具对象生成
 * @param {RegExp} reg 增强型原始正则
 * @param {Function} fns 插入正则的函数集
 * @param {String|Function} str 待匹配字符串,或生成下一个正则时回调执行函数
 * @param {Function} next 生成下一个正则时回调执行函数
 * @returns {{regExp:RegExp,next:Function,exec:Function,test:Function,match:Function,matchAll:Function,replace:Function,search:Function,split:Function}} 正则工具对象
 */
function exRegExp({ reg, fns, str, next }) {
    const oldSplit = /\[\[(.*?[^\\])\]\]/g;
    let regExp, notFirst, source, flags, newFlags, nextCall, res = {}, oldRes = {}, old = [];
    if (reg) {
        source = reg.source.replace(/\\\[(?=\[)/g, '(?:\\[)');
        if (!(newFlags = reg.flags.replace('y', 'g')).includes('g')) {
            newFlags += 'g';
        };
        if (str) regExp = returnRegExp(oldRes, source, oldSplit, newFlags, fns, str, res, old);
    };

    function matRegExp(mat) {
        if (mat) {
            const { source, next: callback } = mat,
                regExp = new RegExp(source, flags);
            if (next) {
                nextCall = () => {
                    const genReg = matRegExp(callback());
                    next(genReg);
                    return genReg;
                };
            } else {
                nextCall = () => matRegExp(callback());
            }
            return regExp;
        } else {
            //正则表达式出错
            throw { reg, flags, fns, str }
        };
    };
    function returnRegExp(oldRes, source, split, newFlags, fns, str, res, old, inner) {
        return matRegExp(splitRegExp({
            source,
            split,
            flags: newFlags,
            fns,
            str,
            res,
            old,
            inner,
            oldRes
        }));
    };

    function preExec() {
        if (notFirst) {
            try {
                regExp = nextCall();
            } catch (e) {
                return true
            };
        } else {
            notFirst = true;
        }
    };
    function exec() {
        if (preExec()) return null;
        const exec = regExp.exec(str);
        if (exec) {
            return exec
        } else {
            try {
                regExp = nextCall();
                return exec();
            } catch (e) {
                console.log(e);
                return null
            }
        }
    };

    function test() {
        const testRes = regExp.test(str);
        if (testRes) {
            return true
        } else {
            try {
                regExp = nextCall();
                return test();
            } catch (e) {
                console.log(e);
                return false
            }
        }
    };

    function match() {
        const matchRes = str.match(regExp);
        if (matchRes) {
            return matchRes
        } else {
            try {
                regExp = nextCall();
                return match();
            } catch (e) {
                console.log(e);
                return null
            }
        }
    };

    function matchAll() {
        const matchAllRes = str.matchAll(regExp);
        if (matchAllRes) {
            return matchAllRes
        } else {
            try {
                regExp = nextCall();
                return matchAll();
            } catch (e) {
                console.log(e);
                return null
            }
        }
    };

    function replace(callback, change) {
        const replaceRes = str.replace(regExp, callback);
        if (change) {
            if (replaceRes !== str) {
                return replaceRes
            } else {
                try {
                    regExp = nextCall();
                    return replace(str);
                } catch (e) {
                    console.log(e);
                    return str
                }
            };
        } else {
            return replaceRes
        };
    };

    function search() {
        const searchRes = str.search(regExp);
        if (searchRes !== -1) {
            return searchRes
        } else {
            try {
                regExp = nextCall();
                return search(str);
            } catch (e) {
                console.log(e);
                return -1
            }
        };
    };

    function split(limit, change) {
        const splitRes = str.split(regExp, limit);
        if (change) {
            if (splitRes.length !== 1) {
                return splitRes
            } else {
                try {
                    regExp = nextCall();
                    return split(str);
                } catch (e) {
                    console.log(e);
                    return [str]
                }
            };
        } else {
            return splitRes
        };
    };

    return {
        //当前生成的正则
        get regExp() { return regExp },
        set regExp(nv) {
            reg = nv;
            notFirst = false;
            res = {};
            oldRes = {};
            old = [];
            flags = reg.flags;
            nextCall = undefined;
            source = reg.source.replace(/\\\[(?=\[)/g, '(?:\\[)');
            if (!(newFlags = flags.replace('y', 'g')).includes('g')) {
                newFlags += 'g';
            };
            if (str) regExp = returnRegExp(oldRes, source, oldSplit, newFlags, fns, str, res, old);
        },
        //当前匹配的字符串
        get str() {
            return str
        },
        set str(newStr) {
            str = newStr;
            notFirst = false;
            res = {};
            oldRes = {};
            old = [];
            nextCall = undefined;
            if (reg) regExp = returnRegExp(oldRes, source, oldSplit, newFlags, fns, str, res, old);
        },
        next() {//生成下一个有效正则,全部无效时报错
            return nextCall()
        },

        exec, /**
         exec() => regExp.exec(str)
        无需主动执行next,当上个正则耗尽后,再调用exec则主动生成下一个有效正则
        */

        test,/**
         test() => regExp.test(str)
        匹配失败时主动执行next生成下一个有效正则
        可主动执行next,主动生成下一个有效正则作为匹配正则
        */

        match,/**
         * match() => str.match(regExp)
        匹配失败时主动执行next生成下一个有效正则
        可主动执行next,主动生成下一个有效正则作为匹配正则
        */

        matchAll, /**
        matchAll() => str.matchAll(regExp)
        匹配失败时主动执行next生成下一个有效正则
        可主动执行next,主动生成下一个有效正则作为匹配正则
        */

        replace, /**
        //replace(callback, change) => str.replace(regExp,callback);
        change为true时,如果替换后的值与替换前一样,则自动调用next生成下一个有效正则继续执行replace(callback, change)
        change为false时,只要生成的正则有效则只执行一次replace
        可主动执行next,主动生成下一个有效正则作为匹配正则
         */

        search, /**
        search() => str.search(regExp)
        匹配失败时主动执行next生成下一个有效正则
        可主动执行next,主动生成下一个有效正则作为匹配正则
        */

        split /**
        split(limit, change) => str.split(regExp,limit)
        change为true时,如果切割后数组长度为1,则自动调用next生成下一个有效正则继续执行split(limit, change)
        change为false时,只要生成的正则有效则只执行一次split
        可主动执行next,主动生成下一个有效正则作为匹配正则
        */
    }
};

//示例
const obj = exRegExp({
    reg: /ersd[[reg:(ka)+]].*ef(fa){[[reg]]}.*sas/g,
    fns: {
        reg([$0, $1]) {
            const range0 = range($0.length / $1.length, 1, true);
            range0.reg = range0.map(it => new Array(it).fill($1).join(''));
            return range0
        }
    },
    str: 'bvgvgersdkakakaeffafaeffafafasaskuyfu'
});

console.log('match:', obj.match()); //match1: ['ersdkakakaeffafaeffafafasas', 'fa', index: 5, input: 'bvgvgersdkakakaeffafaeffafafasaskuyfu', groups: undefined]

obj.regExp = /[[reg:(ka)+]]ef(fa){[[reg]]}/g;

console.log('match2:', obj.match()); //match2: ['kakaeffafa']