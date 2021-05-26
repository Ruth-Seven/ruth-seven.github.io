---
title: anki+GD单词解决方案
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 12:32:27
tags:
---

Anki作为一款记忆神器，丰富的插件和本身的记忆原理相得益彰。这几天学习了一下其强大的功能，作为背单词的实用工具。本身只用Anki背诵单词，那么主要采取两种方法来快速生成导入单词卡片。

<!--more-->

## GoldDict + FastWordQuery

GoldDict是一款俄罗斯大佬开发的开源单词软件，支持本地词典、在线词典，网页查词查询，拥有快捷键，收藏，取词查词支持等丰富功能，基本上已经覆盖了查词的任何需求。选择单词并`Ctrl+C`两次可快速查词，`Ctrl+E`可快速收藏，收藏后的单词支持导出为txt文件。

将txt文件的单词导入Anki软件后，后续可由Anki插件FastWordQuery快速查词并制作卡片。

> FastWQ插件安装码 [1807206748](https://ankiweb.net/shared/info/1807206748)， [使用教程](https://zhuanlan.zhihu.com/p/81645669)

推荐配置如下：

[![image-20200503125952535](http://static.come2rss.xyz/image-20200503125952535.png)](http://static.come2rss.xyz/image-20200503125952535.png)

[image-20200503125952535](http://static.come2rss.xyz/image-20200503125952535.png)



正面卡片模板如下:

```
<section class="_135editor" data-tools="135编辑器" data-id="97876">
    <section style="margin:10px auto;text-align: center;">
        <section style="display:inline-block;color:#f28461;">
            <section class="assistant" style="text-align:right;">
                <section class="assistant" style="width:70px;display:inline-block;">
                    <img class="assistant" style="width:100%;display:block;" src="https://bdn.135editor.com/files/images/editor_styles/de6c8d76ce15363fdd1b8feccfe81302.jpg" data-ratio="0.3157894736842105" data-w="475" data-width="100%"/>
                </section>
            </section>
            <section style="border:1px solid #fcbd6b;padding-right:5px;box-sizing: border-box;margin-top:-5px;">
                <section class="135brush" data-brushtype="text" style="border-right:1px solid #fcbd6b;letter-spacing:1.5px;font-size:16px;padding:8px 1.2em;box-sizing: border-box;">
                    {{单词}}
                </section>
            </section>
            <section style="display:flex;justify-content:flex-end;align-items:center;border:1px solid #fcbd6b;box-sizing: border-box;border-top:none;">
                <section class="assistant" style=";width:6px;height:6px;background-color:#fcbd6b;box-sizing: border-box;transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);"></section>
            </section>
        </section>
    </section>
</section>
<section class="_135editor" data-tools="135编辑器" data-id="97722" >
    <section style="margin:10px auto;">
        <section style="text-align: center;">
            <section style="display:inline-block;border-top:1px solid #7f5c32;border-bottom:1px solid #7f5c32;padding:0px 0.1em;text-align: center;">
                <section style="background-color: #fffaf3;color:#7f5c32;padding:2px 4px;">
                    <section style="display: flex;justify-content:center;align-items: center;">
                        <section class="135brush" data-brushtype="text" style="letter-spacing:1.5px;font-size:16px;text-align: center;">
                            {{发音}}
                        </section>
                    </section>
                </section>
            </section>
        </section>
    </section>
</section>
<section class="_135editor" data-role="paragraph">
    <p>
        <br/>
    </p>
</section>
```

背面卡片模板如下：

```
<section class="_135editor" data-tools="135编辑器" data-id="97713">
    <section style="margin:10px auto;">
        <section style=";width:28px;height:28px;background-color: #fff;color:#7f5c32;text-align:center;line-height:26px;border:1px solid #b68b58;box-sizing: border-box;font-size:18px;transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);">
            0<span class="autonum" data-original-title="" title="">1</span>
        </section>
        <section style="margin-top:-20px;">
            <section class="assistant" style="display:flex;justify-content: flex-start;align-items: center;">
                <section style="background-color:#b68b58;box-sizing: border-box;height:1px;flex:1;margin-right:3px;"></section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;">
                    <section class="assistant" style="width:0px; height:0px; border-bottom:solid 6px transparent; border-left:solid 6px #b68b58;"></section>
                </section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;margin-left:3px;">
                    <section class="assistant" style="width:0px; height:0px; border-bottom:solid 6px #b68b58; border-left:solid 6px #b68b58;"></section>
                </section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;margin-left:3px;">
                    <section class="assistant" style="width:0px; height:0px; border-bottom:solid 6px transparent; border-right:solid 6px #b68b58;"></section>
                </section>
            </section>
            <section style="border:1px solid #b68b58;color:#7f5c32;padding:6px 6px 0px 6px;box-sizing: border-box;">
                <section data-autoskip="1" class="135brush" style="padding:10px;color:#7f5c32;text-align: justify;line-height:1.75em;letter-spacing: 1.5px;font-size:14px;">
                    <p>
					{{音标}}
				</p>
				<p>
                        {{释义}}</span>
                    </p>
                </section>
                <section style="text-align: right;">
                    <section style="width:35px;display:inline-block;">
                        <img class="assistant" style="width:100%;display:block;" src="http://image2.135editor.com/cache/remote/aHR0cHM6Ly9tbWJpei5xbG9nby5jbi9tbWJpel9wbmcvN1FSVHZrSzJxQzVIaWFTRjdCcEVqU1c4MnFpYkxBZTRRMHRxY3EwNHRVV3U5Q3dod3JGWWlheWZHaWN0Yzkzc24xZzFOSE9ZS1BJZ1E3R3NvM0M2V2hNejVBLzA/d3hfZm10PXBuZw==" data-ratio="0.5555555555555556" data-w="54" data-width="100%"/>
                    </section>
                </section>
            </section>
        </section>
    </section>
</section>
<section class="_135editor" data-tools="135编辑器" data-id="97713">
    <section style="margin:10px auto;">
        <section style=";width:28px;height:28px;background-color: #fff;color:#7f5c32;text-align:center;line-height:26px;border:1px solid #b68b58;box-sizing: border-box;font-size:18px;transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);">
            0<span class="autonum" data-original-title="" title="" data-num="2">2</span>
        </section>
        <section style="margin-top:-20px;">
            <section class="assistant" style="display:flex;justify-content: flex-start;align-items: center;">
                <section style="background-color:#b68b58;box-sizing: border-box;height:1px;flex:1;margin-right:3px;"></section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;">
                    <section class="assistant" style="width:0px; height:0px; border-bottom:solid 6px transparent; border-left:solid 6px #b68b58;"></section>
                </section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;margin-left:3px;">
                    <section class="assistant" style="width:0px; height:0px; border-bottom:solid 6px #b68b58; border-left:solid 6px #b68b58;"></section>
                </section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;margin-left:3px;">
                    <section class="assistant" style="width:0px; height:0px; border-bottom:solid 6px transparent; border-right:solid 6px #b68b58;"></section>
                </section>
            </section>
            <section style="border:1px solid #b68b58;color:#7f5c32;padding:6px 6px 0px 6px;box-sizing: border-box;">
                <section data-autoskip="1" class="135brush" style="padding:10px;color:#7f5c32;text-align: justify;line-height:1.75em;letter-spacing: 1.5px;font-size:14px;">
                    <p>
                        {{例子}}
                    </p>
                </section>
                <section style="text-align: right;">
                    <section style="width:35px;display:inline-block;">
                        <img class="assistant" style="width:100%;display:block;" src="http://image2.135editor.com/cache/remote/aHR0cHM6Ly9tbWJpei5xbG9nby5jbi9tbWJpel9wbmcvN1FSVHZrSzJxQzVIaWFTRjdCcEVqU1c4MnFpYkxBZTRRMHRxY3EwNHRVV3U5Q3dod3JGWWlheWZHaWN0Yzkzc24xZzFOSE9ZS1BJZ1E3R3NvM0M2V2hNejVBLzA/d3hfZm10PXBuZw==" data-ratio="0.5555555555555556" data-w="54" data-width="100%"/>
                    </section>
                </section>
            </section>
        </section>
    </section>
</section>
<section class="_135editor" data-tools="135编辑器" data-id="97713" >
    <section style="margin:10px auto;">
        <section style=";width:28px;height:28px;background-color: #fff;color:#7f5c32;text-align:center;line-height:26px;border:1px solid #b68b58;box-sizing: border-box;font-size:18px;transform: rotate(0deg);-webkit-transform: rotate(0deg);-moz-transform: rotate(0deg);-o-transform: rotate(0deg);">
            03
        </section>
        <section style="margin-top:-20px;">
            <section class="assistant" style="display:flex;justify-content: flex-start;align-items: center;">
                <section style="background-color: #b68b58; box-sizing: border-box; height: 1px; flex: 1 1 0%; margin-right: 3px; overflow: hidden;"></section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;">
                    <section class="assistant" style="width: 0px; height: 6px; border-bottom: 6px solid transparent; border-left: 6px solid #b68b58; overflow: hidden; box-sizing: border-box;"></section>
                </section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;margin-left:3px;">
                    <section class="assistant" style="width: 0px; height: 6px; border-bottom: 6px solid #b68b58; border-left: 6px solid #b68b58; overflow: hidden; box-sizing: border-box;"></section>
                </section>
                <section style="border:1px solid #b68b58;display:inline-block;box-sizing: border-box;margin-left:3px;">
                    <section class="assistant" style="width: 0px; height: 6px; border-bottom: 6px solid transparent; border-right: 6px solid #b68b58; overflow: hidden; box-sizing: border-box;"></section>
                </section>
            </section>
            <section style="border:1px solid #b68b58;color:#7f5c32;padding:6px 6px 0px 6px;box-sizing: border-box;">
                <section data-autoskip="1" class="135brush" style="padding: 10px; color: #7f5c32; text-align: justify; line-height: 1.75em; letter-spacing: 1.5px; font-size: 14px; box-sizing: border-box;">
                    <p>
                        {{词形变化}}
                    </p>
                </section>
                <section style="text-align: right;">
                    <section style="width:35px;display:inline-block;">
                        <img class="assistant" style="width:100%;display:block;" src="http://image2.135editor.com/cache/remote/aHR0cHM6Ly9tbWJpei5xbG9nby5jbi9tbWJpel9wbmcvN1FSVHZrSzJxQzVIaWFTRjdCcEVqU1c4MnFpYkxBZTRRMHRxY3EwNHRVV3U5Q3dod3JGWWlheWZHaWN0Yzkzc24xZzFOSE9ZS1BJZ1E3R3NvM0M2V2hNejVBLzA/d3hfZm10PXBuZw==" data-ratio="0.5555555555555556" data-w="54" data-width="100%"/>
                    </section>


                </section>
            </section>
        </section>
    </section>
</section>
<script type="text/javascript">
var initVoice = function () {
    var player = document.getElementById('dictVoice');
    document.addEventListener('click', function (e) {
        var target = e.target;
        if (target.hasAttribute('role') && target.getAttribute('role').indexOf('dict_audio_js') >= 0) {
            var url = target.getAttribute('data-rel');
            player.setAttribute('src', url);
            player.volume = 1;
            player.play();
            e.preventDefault();
        }
    }, false);
};
initVoice();
</script>
```

预览

[![image-20200503130008304](http://static.come2rss.xyz/image-20200503130008304.png)](http://static.come2rss.xyz/image-20200503130008304.png)

[image-20200503130008304](http://static.come2rss.xyz/image-20200503130008304.png)



## Anki-connect + 在线词典助手

面向网页浏览的英语**语境**单词学习，支持在线选词同时配合Anki-connect一键生成卡片到Anki。

> [开发者教程](https://zhuanlan.zhihu.com/p/22472893)
>
> anki-connect的插件获取码 [2055492159](https://ankiweb.net/shared/info/2055492159)
>
> anki-connect默认不支持同词多次插入，[修改教程](https://www.laohuang.net/20180214/ankiconnect-dupe-card-issue/)在此。
>
> [在线词典助手](https://chrome.google.com/webstore/detail/online-dictionary-helper/lppjdajkacanlmpbbcdkccjkdbpllajb)

在线词典助手配置如下

[![image-20200503130021147](http://static.come2rss.xyz/image-20200503130021147.png)](http://static.come2rss.xyz/image-20200503130021147.png)

[image-20200503130021147](http://static.come2rss.xyz/image-20200503130021147.png)



### 资源

[anki各种资源](https://zhuanlan.zhihu.com/p/21328602)

[有道风格模板](https://zhuanlan.zhihu.com/p/24287378?refer=-anki)