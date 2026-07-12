# 本机 Codex 技能安装清单与来源

本文件记录 2026-07-11 至 2026-07-13 期间安装到本机 Codex 的能力。公开仓只镜像了已确认 MIT 许可证的技能目录；没有在当前本机目录中确认可再发布许可证的内容仅保留来源，不重新发布。

## 已镜像到 `skills/` 的技能

### WPS Skills

来源：`lc2panda/wps-skills`，MIT，许可证见 `licenses/WPS-SKILLS-MIT.txt`。

- `wps-office`
- `wps-word`
- `wps-excel`
- `wps-ppt`

### AI Berkshire

来源：`xbtlin/ai-berkshire`，MIT，许可证见 `licenses/AI-BERKSHIRE-MIT.txt`。

- `bottleneck-hunter`
- `deep-company-series`
- `dyp-ask`
- `earnings-review`
- `earnings-team`
- `financial-data`
- `industry-funnel`
- `industry-research`
- `investment-checklist`
- `investment-memo-craft`
- `investment-research`
- `investment-team`
- `management-deep-dive`
- `news-pulse`
- `portfolio-review`
- `private-company-research`
- `quality-screen`
- `thesis-drift`
- `thesis-tracker`
- `wechat-article`

## 已安装但仅记录来源的能力

### 通用技能

- `ui-ux-pro-max`
- `file-organizer`
- `research`
- `research-add-fields`
- `research-add-items`
- `research-deep`
- `research-report`
- `agent-reach`：来源 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)。

### 飞书/Lark 技能

- `lark-shared`、`lark-doc`、`lark-drive`、`lark-markdown`、`lark-sheets`、`lark-base`、`lark-slides`、`lark-whiteboard`、`lark-wiki`
- `lark-im`、`lark-mail`、`lark-contact`、`lark-calendar`、`lark-task`、`lark-approval`、`lark-okr`、`lark-attendance`
- `lark-vc`、`lark-vc-agent`、`lark-minutes`、`lark-note`、`lark-event`、`lark-apps`、`lark-openapi-explorer`、`lark-skill-maker`
- `lark-workflow-standup-report`、`lark-workflow-meeting-summary`

### 插件和项目内工作流

- Remotion：动态图表和视频合成插件。
- Build Web Data Visualization：交互式网页数据可视化插件。
- Data Analytics：KPI、看板、指标诊断和分析报告插件。
- Firecrawl：网页抓取和 Markdown 提取插件，来源 [firecrawl-codex-plugin](https://github.com/mendableai/firecrawl-codex-plugin)。
- OpenMontage：项目内视频制作工作流，来源 [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)，AGPL-3.0；本机项目路径为 `D:\文档\GitHub\OpenMontage`。

## 未镜像原因

本仓库是公开仓库。对于当前目录中没有明确附带许可证、或属于插件/项目运行时的能力，直接复制到这里可能遗漏上游的授权、依赖或运行环境。保留来源清单能保证后续按原始项目安全重装，同时避免将登录配置、密钥、缓存或不完整的第三方代码发布到公开仓库。
