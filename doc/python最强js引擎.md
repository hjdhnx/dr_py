#### 人生苦短,我用python
#### 不想换行,js最强
###### 道长踩过的坑,推荐一波python的js引擎

#### 从弱到强推荐,大家仔细看

| 模块                                                         | 性能  | es6          | python交互 | 相关文档 | 架构兼容性 | 个人评价                             |
|------------------------------------------------------------|-----|--------------|----------|------|-------|----------------------------------|
| [pyv8](https://github.com/emmetio/pyv8-binaries)           | 较差  | ❌            | ✅        | 少    | 差     | 年代久远,可以放弃了                       |
| [PyExecJS](https://github.com/doloopwhile/PyExecJS)        | 差   | ❌            | ❌        | 多    | 好     | 年代久远,应用挺多,勉强能用                   |
| [v8py](https://github.com/tbodt/v8py)                      | 好   | ✅完美支持        | ✅        | 少    | 差     | 文档少,架构兼容性差,不太会用                  |
| [pyjsparser](https://github.com/PiotrDabkowski/pyjsparser) | 一般  | ❌            | ❌        | 少    | 差     | 几乎不用                             |
| [dukpy](https://github.com/amol-/dukpy)                    | 好   | ❌部分支持        | 支持       | 官仓示例 | 差     | 没见人用过                            |
| [py_mini_racer](https://github.com/sqreen/PyMiniRacer)     | 一般  | ✅完美支持        | ❌        | 少    | 差     | 不支持js交互,文档少,架构兼容性差,不怎么会用         |
| [js2py](https://github.com/PiotrDabkowski/Js2Py)           | 一般  | ❌部分支持,实际应用鸡肋 | ✅        | 还行   | 好     | python交互好,没得选了                   |
| [quickjs](https://github.com/PetterS/quickjs)              | 好   | ✅完美支持        | ✅部分支持    | 几乎没有 | 好     | 有测试案例代码,看完就会用,issue有人提了交互的更多代码   |
| [jsengine](https://github.com/SeaHOH/jsengine)              | 好   | ✅完美支持        | ✅部分支持    | 几乎没有 | 好     | quickjs的个人封装,比较新,整合怪             |
| [thquickjs](https://gitlab.com/tangledlabs/thquickjs)              | 好   | ✅完美支持        | ✅部分支持    | 几乎没有 | 好     | quickjs的个人封装,比较新,python交互不如js2py |

### 本项目的最终选择

quickjs + js2py  

#### 使用说明
quickjs负责读取js文件源的模块,速度非常快  
js2py负责python执行js的源逻辑，交互python注入的任意类型变量  
#### 研究方向
quickjs如何交互python非基础类型数据,看quickjs的pr和issue有人提出过,但是作者没有合并以及修改支持,需要自己动手了
