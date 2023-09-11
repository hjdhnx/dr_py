var commonUtil = {
    isVideo(playUrl){
        let res_url = playUrl.split('?')[0];
        if(playUrl.endsWith('.m3u8')||res_url.endsWith('.m3u8')){
                return true
        }else if(playUrl.endsWith('.mp4')||res_url.endsWith('.mp4')){
                return true
        }else if(/\.(m4a|mp3|flv|aac)$/.test(playUrl)||/\.(m4a|mp3|flv|aac)$/.test(res_url)){
            return true
        }
        return false
    },
    getLocationFromRedirect(
          originUrl,
          method = "GET"
        ){
          return new Promise<string>((resolve, reject) => {
            const xhr = new XMLHttpRequest();
            xhr.open(method, originUrl, true);
            xhr.onload = function () {
              resolve(xhr.responseURL);
            };
            xhr.onerror = reject;
            xhr.send(null);
          })
    },
    get302UrlResponse(url, callback) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onload = function () {
            callback(xhr.responseURL);
        }
        xhr.send(null);
    },
    async getRealUrl(url,callback){
        const res = await axios.get(`web/302redirect?url=${encodeURIComponent(url)}`);
        return callback(res);
    }
};