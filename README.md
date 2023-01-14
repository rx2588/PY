
- [初始化](#初始化)
  - [Python 依赖](#python-依赖)
- [操作步骤](#操作步骤)
  - [转换账号文件](#转换账号文件)
  - [抓取任务](#抓取任务)
  - [通过写作猫生成文章](#通过写作猫生成文章)
    - [需要认证的情况](#需要认证的情况)

# 初始化

## Python 依赖

```shell
pip install requests
pip install loguru
pip install pysocks
pip install python-docx
pip install --upgrade openai
```

# 操作步骤

## 转换账号文件

以账号文件 `account-173-18.csv` 为例子，将文件复制到 `tools/account2json` 目录下后，在该目录下执行下面的命令：

```shell
java -Xbootclasspath/a:lib/selenium-java-4.7.2/selenium-api-4.7.2.jar:lib/fastjson-1.2.83.jar Main account-173-18.csv
```

执行完成后将会生成对应的 JSON 文件 `account-173-18.json`，将其复制到 `conf` 目录下，修改成 `xiezuocat_cookies.json` 文件即可。`xiezuocat_cookies.json` 就是我们的账号文件。


## 抓取任务

从墨斗鱼后台抓取到 curl 命令，替换到 `conf/fetch_tasks_curl.txt` 内容里面，然后运行如下命令

```
python3 fetch_tasks.py
```

执行完成后就抓取成功了。可以通过修改 `settings.json` 修改需要抓取的类别。

## 通过写作猫生成文章

配置好 `xiezuocat_cookies.json` 和抓取到任务后，就可以通过下面的命令生成写作猫生成文章：

```
python3 generate_articles_by_xiezuocat.py
```

账号失去额度后，会自动使用下一个账号继续生成文章，直至账号被消耗完。

### 需要认证的情况


```
遇到需要认证的错误错误，请在网页上完成认证，地址： https://xiezuocat.com/#/tutorial 当前 Cookie 为
[{"domain": ".xiezuocat.com", "expirationDate": 1671194831.477312, "hostOnly": false, "httpOnly": false, "name": "traceid", "path": "/", "sameSite": "no_restriction", "secure": true, "session": false, "storeId": null, "value": "8c56ec9e95564b73"}, {"domain": ".xiezuocat.com", "expirationDate": 1671194831.4773152, "hostOnly": false, "httpOnly": false, "name": "uid", "path": "/", "sameSite": "no_restriction", "secure": true, "session": false, "storeId": null, "value": "639964d8ebdb21ce267f7f39"}, {"domain": ".xiezuocat.com", "expirationDate": 1671194831.4773161, "hostOnly": false, "httpOnly": false, "name": "JSESSIONID", "path": "/", "sameSite": "no_restriction", "secure": true, "session": false, "storeId": null, "value": "A7404D982E9B3D70127E5E447DC8B7B9"}, {"domain": ".xiezuocat.com", "expirationDate": 1671194831.4773178, "hostOnly": false, "httpOnly": false, "name": "Hm_lpvt_099c1a390e23e6b73b081c48519f6e8e", "path": "/", "sameSite": "no_restriction", "secure": true, "session": false, "storeId": null, "value": "1670997179"}, {"domain": ".xiezuocat.com", "expirationDate": 1671194831.477324, "hostOnly": false, "httpOnly": false, "name": "Hm_lvt_099c1a390e23e6b73b081c48519f6e8e", "path": "/", "sameSite": "no_restriction", "secure": true, "session": false, "storeId": null, "value": "1670997179"}, {"domain": ".xiezuocat.com", "expirationDate": 1671194831.4773262, "hostOnly": false, "httpOnly": false, "name": "sid", "path": "/", "sameSite": "no_restriction", "secure": true, "session": false, "storeId": null, "value": "2747a14472cf4141b714607de4946b90"}]
```

出现这种情况，需要将 Cookie 复制出来，打开写作猫的页面，替换 Cookie 后，尝试 AI 写作就会弹出认证。完成认证后输入 y 即可继续

