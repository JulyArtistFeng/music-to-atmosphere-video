# 音乐氛围短片 · 2.0

技能名：`music-to-atmosphere-video`。仓库可见性保持 **Public**。

以用户原曲为主时钟，将音乐结构、歌词/意象与连续视觉组织为氛围短片；支持纯器乐。

不替换原曲，不制作攻略/影视解说/实况集锦，不默认转数字人唱歌。

## 本轮升级

以原曲时钟做分段和剪点，处理半倍速BPM与无歌词输入，增加镜头身份锚点和歌词未知状态。

入口：[SKILL.md](SKILL.md)。职责专属的[五项高星候选及取舍](references/upgrade-20261124.md)与[来源锁定](references/upgrade-source-lock.json)记录星标、许可、具体提交和文件指纹。排名限于本次查得且按职责筛选的候选池，不声称穷尽全GitHub。

仅独立归纳可适用方法，不复制上游代码、模型、权重或整套提示词；不因高星假定工具已安装或服务已接通。原包参考中的工具名和固定参数按当前入口校准。

## 安装与使用

将本仓库放入用户技能目录的 `music-to-atmosphere-video` 文件夹，保留相对路径。

```text
请使用 $music-to-atmosphere-video，根据我的素材与目标完成本次任务。
```

只加载本次相关参考，不要求安装总目录中的其他技能。发布内容、调用付费服务或发送原始素材仍遵守当前任务授权。

## 检查

本职契约见 [production-contract.md](references/production-contract.md)。

```sh
python -B scripts/check_contract.py examples/contract.json
python -B -m unittest discover -s scripts -p "test_*.py"
```

[示例JSON](examples/contract.json)为合成结构样例，不是真实信源、已批准素材或已渲染视频。实际使用时填写当前素材与时序。检查器只验证声明的契约，不证明内容真假、手部解剖、视听效果或最终质量。

本轮测试及独立试用的实际范围和局限由总目录的升级报告记录；不把结构通过称为实际媒体/游戏输出已经验收。

[个人 Skills 总目录](https://github.com/TTTTTfeng/skills-index)（私有管理入口；公开技能仓库可单独访问）。
