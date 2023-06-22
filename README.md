# ChatGLM-6B-Prompt

这是一个基于PaddlePaddle和ChatGLM-6B的Prompt集合仓库。你可以在这个仓库上传Prompt配置，之后就可以在[AiStudio页面](https://aistudio.baidu.com/aistudio/projectdetail/6421937?contributionType=1)快捷使用你的提示词，你也可以将这个页面分享给你朋友，快捷体验你的提示词。

> 🎉
> 在2023.06.21-2023.07.24期间内，报名[灵感中心「Prompt」PR征集](https://aistudio.baidu.com/aistudio/activitydetail/1503019239)并给本仓库提交PR，还可以获得小礼品，包括百度周边雨伞、玩偶、包、被子、耳机、音响等等！ 
> 🎉

## 快速使用
点击[AiStudio页面](https://aistudio.baidu.com/aistudio/projectdetail/6421937?contributionType=1)，在`应用体验`页面，选中`更新提示词选单`，选择对应的`提示词主题`，即可参考说明快速体验ChatGLM-6B问答。

## 如何提交自己的提示词
1. Fork本仓库
2. 更改Fork后仓库中的Prompt.json文件
   - 方法1：你可以将仓库拉到本地，修改项目文件`add_prompt.py`中的第十行到十三内容，运行该脚本即可自动修改`prompts.json`文件，将此文件提交到远程仓库并发起pull request即可。
   - 方法2：如果你本地没有`Python`环境，你可以在`AiStudio`fork[我的项目](https://aistudio.baidu.com/aistudio/projectdetail/6421937?contributionType=1)，以CPU形式启动，里面同样有一个与`add_prompt.py`完全相同的代码块，运行它即可生成对应的`prompts.json`文件，将此文件下载后，上传到自己的Github仓库中，发起Pull request即可。
3. 本仓库的管理员审核后，你就可以在[AiStudio页面](https://aistudio.baidu.com/aistudio/projectdetail/6421937?contributionType=1)快捷使用自己的`Prompts`了。

> 你同样可以在[AiStudio页面](https://aistudio.baidu.com/aistudio/projectdetail/6421937?contributionType=1)快捷体验ChatGLM-6B对话功能。
> 如何建设Prompts请参考[AiStudio页面](https://aistudio.baidu.com/aistudio/projectdetail/6421937?contributionType=1)。