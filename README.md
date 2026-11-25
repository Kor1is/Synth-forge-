# Infinity Workbench

本地单机、无账号、无云端依赖的合成生物学工作台。它把 **部件 → 组装方案 → 结构验证 → 测序验证 → 记录留痕 → 实验卡 → 报告** 串成一条可复现的实验流程。

> 本项目代码、界面文案与演示数据均为原创；演示序列是合成的，不包含 Addgene、iGEM 或论文附件中的受版权保护材料。详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

![Infinity Workbench](docs/assets/app-icon.png)

## 能做什么

| 分组 | 模块 | 说明 |
| --- | --- | --- |
| 分析 | 序列分析 | 长度、GC、ORF、翻译、常见酶切位点 |
| 分析 | 密码子优化 | 大肠杆菌 / 酵母 / CHO 宿主，输出 FASTA、CAI 与 GC 曲线 |
| 分析 | 代谢模型 | 载入 SBML，培养基覆盖、目标代谢物与敲除建议 |
| 设计 | 引物设计 | 目标区间、Tm / GC 约束、候选引物对 |
| 设计 | 组装方案 | Gibson / Golden Gate 片段重叠、引物与加样顺序 |
| 设计 | 基因线路 | 通过外部 Cello 进程把 Verilog 映射为构建体（可选） |
| 设计 | RBS 强度 | 本地启发式候选表与外部计算入口 |
| 验证 | 结构预测 | 通过外部 ColabFold 进程预测 PDB（可选） |
| 验证 | 结构评估 | RMSD、pLDDT、TM、SASA、二级结构比例 |
| 验证 | 测序验证 | 设计序列与 reads 比对，自动识别反向互补 |
| 验证 | 质粒图谱 | 环形图与 feature 表 |
| 验证 | 设计规则 | 1-based 位置的 error / warning / info 规则检查 |
| 验证 | 构建体差异 | 两个构建体的序列与 feature 差异 |
| 计算 | 实验计算 | 摩尔、稀释、拷贝数、OD600、效率、Tm、引物 |
| 计算 | 批量运行 | 1–50 个文件复用已有模块，单项失败不中断 |
| 资源 | 资源库 | 本地部件与质粒资源的导入、导出、检索 |

交付能力：**实验报告**（多 run 汇总 HTML，可用浏览器打印为 PDF）与 **A4 实验卡**（按构建体生成，含 60 bp 分块序列和签名栏）。

## Windows 启动

双击项目根目录的 `启动 Infinity Workbench.cmd`：它会在后台启动仅绑定 `127.0.0.1:8501` 的本机服务，等待服务就绪后用系统默认浏览器打开 `http://127.0.0.1:8501`。命令行窗口会短暂出现并自动关闭；服务已在运行时重复双击只会重新打开同一页面。运行产物保存在项目 `workspace\` 下。需要停止服务时，在任务管理器中结束对应的 `pythonw.exe`。

桌面快捷方式：右键 `启动 Infinity Workbench.cmd` → 发送到 → 桌面，然后右键快捷方式 → 属性 → 更改图标，选择 `docs\assets\app.ico`。

首次启动可点击“加载示例数据”，会创建完全合成的演示项目。源码版使用本机 `.venv`，不依赖预打包的 EXE。

## 快速开始

要求 Python 3.11+。所有命令都在项目根目录执行。

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

浏览器打开终端提示的地址（默认 `http://localhost:8501`）。首次启动可点击“加载示例数据”，会创建完全合成的演示项目。

Linux / macOS：

```bash
bash scripts/setup_env.sh
.venv/bin/python -m streamlit run app.py
```

## 设计约束

- **本地优先**：运行时不发起网络请求；唯一的外部跳转是 M13 页面上由用户手动点击的计算服务链接。
- **单机单用户**：没有登录、云同步、遥测或远程数据库。SQLite 与产物都在 `workspace/`。
- **可审计**：每次运行有独立日志、状态机、产物校验和；失败与部分成功都可重试。
- **可复现**：依赖锁定在 `requirements.txt`；结构预测与 Cello 只通过 `subprocess` 调用，主进程不 import 这些包。
- **主题唯一来源**：颜色 token 只在 `core/config.py` 定义，组件只读 CSS 变量。

## 目录

```text
app.py                 入口与路由
启动 Infinity Workbench.cmd  Windows 启动器（本机服务 + 默认浏览器）
core/                  配置、数据库、任务、文件、日志、主题、自检
adapters/              M1–M16 适配器与共享工具
ui/                    布局、12 个固定组件、页面
templates/             报告与实验卡 Jinja2 模板
data/demo/             每个模块的原创合成示例
data/resources/        可再分发的离线资源
docs/                  使用、依赖与排错说明
tests/                 适配器、核心与 UI 冒烟测试
workspace/             运行产物（git 忽略）
.tmp/                  临时文件（git 忽略）
DISCLAIMER.md          生物安全、隐私与责任边界
```

## 可选外部工具与缺失依赖

默认安装只包含宽松许可证的依赖，16 个模块中 **13 个可直接运行**；M4、M7、M12 需要可选外部工具，M11 和报告 PDF 会自动降级。测试结果中的 `3 skipped` 就是这三个可选依赖，不是失败。

| 缺失项 | 影响 | 没有它时 | 补装方式 |
| --- | --- | --- | --- |
| **COBRApy** | M4 代谢模型 | 模块灰显，返回 `E_DEP_MISSING` | `.\.venv\Scripts\python.exe -m pip install cobra==0.32.1`（GPL-3.0，可选） |
| **ColabFold** | M7 结构预测 | 模块灰显，不联网下载模型 | 独立安装 ColabFold，把 `COLABFOLD_BIN` 指向 `colabfold_batch` |
| **Cello + Java** | M12 基因线路 | 模块灰显 | 安装 Java 与 Cello，确保 `java`、`cello` 在 `PATH` 中 |
| **DNA Weaver** | M11 组装 | 自动降级为内置重叠区扫描，标记 `partial` + warning | `.\.venv\Scripts\python.exe -m pip install dnaweaver` |
| **WeasyPrint** | 报告 PDF | 仍生成 HTML，可浏览器打印为 PDF | `.\.venv\Scripts\python.exe -m pip install weasyprint==68.1`，Windows 还需 GTK |

完整步骤、许可证说明、验证命令和排错见 **[docs/dependencies.md](docs/dependencies.md)**。M3 引物设计已改为内置评分，不再需要 primer3。

## 依赖自检

在应用“设置”页可查看每个依赖的 `ready / missing / error` 状态；也可运行：

```powershell
.\.venv\Scripts\python.exe -c "from core.env_check import self_check; print(self_check())"
```

安装可选组件后重启应用，左侧对应模块会从灰色恢复可点击。缺失依赖不会影响其他模块，也不会损坏已有数据。

## 测试

```powershell
.\.venv\Scripts\python.exe -m pytest
```

测试会把临时目录放在项目内的 `workspace/tmp/pytest`，不会写到系统临时目录。预期结果：未安装可选组件时为 `25 passed, 3 skipped`。

## 数据与隐私

上传文件在提交时复制到 `workspace/runs/<run_id>/inputs/`，运行结果、图件与日志都保存在该目录或 `workspace/` 下。删除 `workspace/` 不会损坏代码，但会丢失历史和设置页中的清理记录。本软件不设账号、云同步或遥测，也不在运行时主动发起网络请求；M13 的外部计算入口只在你手动点击时由浏览器打开。

## 免责声明

本项目仅用于教学、科研构思和实验流程整理，**不构成医疗、临床、制药或生物安全建议**。任何湿实验、基因编辑、微生物操作或环境释放都必须由具备资质的专业人员评估，并遵守适用的生物安全、生物安保、伦理、出口管制和法律要求。软件按“现状”提供，不附带任何担保；作者与贡献者不对使用后果承担责任。完整条款见 **[DISCLAIMER.md](DISCLAIMER.md)**。

## 许可

代码以 MIT License 发布。第三方依赖的许可证见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。演示数据为原创合成内容，可随项目一起再分发。