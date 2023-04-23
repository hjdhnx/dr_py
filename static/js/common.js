function copy(text,mode){
    mode = mode||0;
    if(mode === 0){
        let el = $('<input id="input_to_copy" style="position: absolute;top: 0;left: 0;opacity: 0;z-index: -10"/>');
    　　 $('body').prepend(el); //添加到元素内部的前面
        el.val(text); // 修改文本框的内容
        el.select(); //选中
        console.log('复制的内容:\n'+text);
        document.execCommand("copy"); // 执行浏览器复制命令
        el.remove();
    }else{
        let el = $(text);
        console.log('复制的内容:\n'+el.val());
        el.select(); //选中
        document.execCommand("copy"); // 执行浏览器复制命令
    }
    alert("复制成功");
}