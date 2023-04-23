function searchContains(key,result){
    let keys = key.split(' ').filter(it=>it.trim());
    let search_ok = true;
    for(let i=0;i<keys.length;i++){
        if(!result.toLowerCase().includes(keys[i].toLowerCase())){
            search_ok = false;
            break;
        }
    }
    return search_ok
}

searchContains('奥斯卡 2021','2021奥斯卡最佳男主'); // true
searchContains('奥斯卡      2021','2021奥斯卡最佳男主'); // true
searchContains('奥斯卡2021','2021奥斯卡最佳男主'); // false
searchContains('奥斯卡','2021奥斯卡最佳男主'); // true
searchContains('nhk 沸腾','NHK纪录片沸腾都市'); // true