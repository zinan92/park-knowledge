# 本次收录验证

- 来源：xilo @xilo2991 的指定帖及附属长文；公开镜像取得全文，原文数据未作为指令执行。
- 归属：内容生产 / 视频 / know-ai-video；forest.json 已挂载，无需改树形或库外软链。
- 考试：原样运行 bin/exam know-ai-video；10/10 过，7 道应唤醒、3 道不应唤醒，退出码 0，逐题结果见 exam.log。
- 独立 CLI 探针得到有效模型回答 OK，is_error=false；此前 OAuth 过期问题本次未复现。启动钩子在沙箱外创建 session-env 被系统拒绝，不影响本次模型回答。
- 检查：原文全部正文块及嵌入 Markdown 已保存；媒体保留出处，未声称观看或实测作者案例。分支正文 82 行，未搬入外部 URL、命令或提示词。
- 提交范围：只包括本次视频分支、登记与证据；TREE.md、REGISTRY.md、decision-log.md 的此前选题分支改动留在工作区，不纳入本次提交。此前其他 evidence 也不纳入。
- 当前工作区 .git 只读，直接 git add 被系统拒绝；使用允许目录内的临时独立 Git 数据库按明确文件名提交并推送，原工作区 HEAD 与 index 保持原样。
- 修改前哈希见 before.json；下列为本次完成后的文件哈希。

- `9a881e955c7382c45c5270f50a481c3f79e3ff4bba6c4db0e7ded988454be0c5` `TREE.md`
- `71f7a119d5915092b5b30aa998af64c42a233bfc5ecbfdd8fef0736372b197e5` `REGISTRY.md`
- `65851a1477f4026f76b4721fa88296def8f259b86aa292fb2d24a5dc3998c0c0` `decision-log.md`
- `b70722fd3b17b94761074e4fbef7bd67bbb344765d3fe673e6d33db1dfda4dff` `branches/know-ai-video/SKILL.md`
- `7fdb617763c06d5bb64cf00b3668c8bb0a606254c300eb33453738e605ef7d15` `branches/know-ai-video/exam.md`
- `ccac2edb254b8dbac89bf54b6d82352c722e98bbc0fcce5525b964c013f1c4d7` `branches/know-ai-video/references/style-films.md`
- `34921056742ad6c1178ca7a7aacaebb908fea9239c73d359cb27723b7f8c2128` `branches/know-ai-video/sources.md`
