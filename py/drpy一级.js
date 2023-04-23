js:
let d = [];
let douban = input.split("douban=")[1].split("&")[0];
// let douban_api_host = "https://frodo.douban.com/api/v2";
let douban_api_host = "http://api.douban.com/api/v2";
let miniapp_apikey = "0ac44ae016490db2204ce0a042db2916";
// let miniapp_apikey = "054022eaeae0b00e0fc068c0c0a2102a";
const count = 30;

function miniapp_request(path, query) {
    try {
        let url = douban_api_host + path;
        query.apikey = miniapp_apikey;
        fetch_params.headers = oheaders;
        url = buildUrl(url, query);
        // print(url);
        // print(fetch_params);
        let html = fetch(url, fetch_params);
        if(/request_error/.test(html)){
            print(html);
        }
        // print(html);
        return JSON.parse(html)
    } catch (e) {
        print("发生了错误:" + e.message);
        return {}
    }
}

function cate_filter(d, douban) {
    douban = douban || "";
    try {
        let res = {};
        if (MY_CATE === "interests") {
            // print(douban);
            if (douban) {
                let status = MY_FL.status || "mark";
                let subtype_tag = MY_FL.subtype_tag || "";
                let year_tag = MY_FL.year_tag || "全部";
                let path = "/user/" + douban + "/interests";
                res = miniapp_request(path, {
                    type: "movie",
                    status: status,
                    subtype_tag: subtype_tag,
                    year_tag: year_tag,
                    start: (MY_PAGE - 1) * count,
                    count: count
                })
            } else {
                return {}
            }
        } else if (MY_CATE === "hot_gaia") {
            let sort = MY_FL.sort || "recommend";
            let area = MY_FL.area || "全部";
            let path = "/movie/" + MY_CATE;
            res = miniapp_request(path, {
                area: area,
                sort: sort,
                start: (MY_PAGE - 1) * count,
                count: count
            })
        } else if (MY_CATE === "tv_hot" || MY_CATE === "show_hot") {
            let stype = MY_FL.type || MY_CATE;
            let path = "/subject_collection/" + stype + "/items";
            res = miniapp_request(path, {
                start: (MY_PAGE - 1) * count,
                count: count
            })
        } else if (MY_CATE.startsWith("rank_list")) {
            let id = MY_CATE === "rank_list_movie" ? "movie_real_time_hotest" : "tv_real_time_hotest";
            id = MY_FL.榜单 || id;
            let path = "/subject_collection/" + id + "/items";
            res = miniapp_request(path, {
                start: (MY_PAGE - 1) * count,
                count: count
            })
        } else {
            let path = "/" + MY_CATE + "/recommend";
            let selected_categories;
            let tags;
            let sort;
            if (Object.keys(MY_FL).length > 0) {
                sort = MY_FL.sort || "T";
                tags = Object.values(MY_FL).join(",");
                if (MY_CATE === "movie") {
                    selected_categories = {
                        "类型": MY_FL.类型 || "",
                        "地区": MY_FL.地区 || ""
                    }
                } else {
                    selected_categories = {
                        "类型": MY_FL.类型 || "",
                        "形式": MY_FL.类型 ? MY_FL.类型 + "地区" : "",
                        "地区": MY_FL.地区 || ""
                    }
                }
            } else {
                sort = "T";
                tags = "";
                if (MY_CATE === "movie") {
                    selected_categories = {
                        "类型": "",
                        "地区": ""
                    }
                } else {
                    selected_categories = {
                        "类型": "",
                        "形式": "",
                        "地区": ""
                    }
                }
            }
            let params = {
                tags: tags,
                sort: sort,
                refresh: 0,
                selected_categories: stringify(selected_categories),
                start: (MY_PAGE - 1) * count,
                count: count
            };
            // print(params);
            res = miniapp_request(path, params)
        }
        let result = {
            page: MY_PAGE,
            pagecount: Math.ceil(res.total / count),
            limit: count,
            total: res.total
        };
        let items = [];
        if (/^rank_list|tv_hot|show_hot/.test(MY_CATE)) {
            items = res["subject_collection_items"]
        } else if (MY_CATE === "interests") {
            res["interests"].forEach(function(it) {
                items.push(it.subject)
            })
        } else {
            items = res.items
        }
        let lists = [];
        items.forEach(function(item) {
            if (item.type === "movie" || item.type === "tv") {
                let rating = item.rating ? item.rating.value : "";
                let rat_str = rating || "暂无评分";
                let title = item.title;
                let honor = item.honor_infos || [];
                let honor_str = honor.map(function(it) {
                    return it.title
                }).join("|");
                let vod_obj = {
                    vod_name: title !== "未知电影" ? title : "暂不支持展示",
                    vod_pic: item.pic.normal,
                    vod_remarks: rat_str + " " + honor_str
                };
                let vod_obj_d = {
                    url: item.type + "$" + item.id,
                    title: title !== "未知电影" ? title : "暂不支持展示",
                    pic_url: item.pic.normal,
                    desc: rat_str + " " + honor_str
                };
                lists.push(vod_obj);
                d.push(vod_obj_d)
            }
        });
        result.list = lists;
        return result
    } catch (e) {
        print(e.message)
    }
    return {}
}
let res = cate_filter(d,douban);
setResult2(res);