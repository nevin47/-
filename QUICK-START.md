# Markdown AI 编辑器 - 5分钟快速开始

## 步骤 1：打开编辑器 (30秒)

双击打开 `markdown-ai-editor.html` 文件，浏览器会自动打开编辑器。

## 步骤 2：配置API (2分钟)

1. 点击右上角的 **⚙️ 配置** 按钮
2. 填写以下信息：

### 使用 Ollama（推荐本地部署）

```
API 地址: http://localhost:11434/v1/chat/completions
API Key: （留空）
模型名称: qwen2.5
```

**首次使用 Ollama？**

```bash
# 安装 Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 下载模型
ollama pull qwen2.5

# 启动服务（自动运行）
```

### 使用 LM Studio

```
API 地址: http://localhost:1234/v1/chat/completions
API Key: （留空）
模型名称: （在LM Studio中选择的模型名）
```

### 使用 OpenAI API

```
API 地址: https://api.openai.com/v1/chat/completions
API Key: sk-your-api-key-here
模型名称: gpt-3.5-turbo
```

3. 点击 **保存配置** 按钮

## 步骤 3：测试AI补全 (2分钟)

1. 在编辑器中输入：

```markdown
# 我的第一篇文章

人工智能正在改变
```

2. 将光标放在"改变"后面

3. 按下 `Ctrl+E`

4. 等待AI生成建议（2-5秒）

5. 按 `Tab` 接受补全，或按 `Esc` 拒绝

## 步骤 4：调整补全粒度 (1分钟)

在配置面板中：

**快速补全（适合列要点）：**
- 补全粒度：句子

**正常写作（适合写段落）：**
- 补全粒度：段落

**长文写作（适合写章节）：**
- 补全粒度：章节

## 常用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+E` | AI智能补全 |
| `Ctrl+S` | 保存文件 |
| `Ctrl+O` | 打开文件 |
| `Ctrl+N` | 新建文档 |
| `Tab` | 接受补全 |
| `Esc` | 拒绝补全 |

## 实用技巧

### 技巧 1：逐步补全

1. 输入标题：`## 如何使用Python`
2. 按 `Ctrl+E` 生成导语句子
3. 接受后，继续按 `Ctrl+E` 补全下一句
4. 重复步骤3，逐步完成整段

### 技巧 2：大纲扩展

使用"句子"粒度先写出大纲：

```markdown
## 产品特点

1. 易用性
2. 高性能
3. 可扩展
```

然后将粒度改为"段落"，在每个要点后补全详细说明。

### 技巧 3：创意激发

如果不知道写什么，可以：

1. 输入一个主题或关键词
2. 调高 Temperature 到 0.8-1.0
3. 按 `Ctrl+E` 让AI给出创意
4. 选择喜欢的方向继续

## 故障排查

### ❌ 问题：按 Ctrl+E 无反应

**检查：**
- API地址是否正确？
- 本地API服务是否在运行？
- 打开浏览器控制台（F12）查看错误

**解决：**
```bash
# 如果使用 Ollama
ollama serve

# 测试 API 是否可用
curl http://localhost:11434/v1/chat/completions
```

### ❌ 问题：生成内容太长/太短

**解决：**
1. 启用"长度控制"选项
2. 调整对应粒度的 Max Tokens：
   - 句子：30-50
   - 段落：150-200
   - 章节：400-500

### ❌ 问题：CORS错误

**错误信息：** `Access to fetch at '...' has been blocked by CORS policy`

**解决：**
- 使用支持CORS的API
- 或在本地运行代理服务器

对于 Ollama，确保使用 `/v1/chat/completions` 端点。

## 下一步

✅ 完成快速开始后，你可以：

1. 📖 阅读 [完整使用指南](README-MARKDOWN-EDITOR.md)
2. 📝 打开 [示例文档](example-document.md) 进行练习
3. ⚙️ 自定义提示词以适应你的写作风格
4. 🎯 尝试不同的模型和参数组合

## 推荐配置组合

### 📚 技术文档写作

```
输入粒度: 最近500字符
补全粒度: 段落
Temperature: 0.4
模型: qwen2.5 / codellama
```

### ✍️ 博客文章写作

```
输入粒度: 当前章节
补全粒度: 段落
Temperature: 0.7
模型: qwen2.5 / llama3
```

### 💡 创意写作

```
输入粒度: 最近500字符
补全粒度: 章节
Temperature: 0.9
模型: llama3 / mistral
```

### 📋 学习笔记整理

```
输入粒度: 当前段落
补全粒度: 句子
Temperature: 0.3
模型: qwen2.5
```

## 视频教程（可选）

如果你更喜欢视频学习，可以录制以下操作：

1. ⏱️ 0:00-0:30 - 打开编辑器
2. ⏱️ 0:30-2:00 - 配置API
3. ⏱️ 2:00-3:30 - 第一次AI补全
4. ⏱️ 3:30-5:00 - 调整粒度和参数

## 获取帮助

遇到问题？

1. 📖 查看 [README](README-MARKDOWN-EDITOR.md) 的常见问题部分
2. 🔍 启用调试模式查看详细日志
3. 💬 在项目仓库提交 Issue
4. 📧 发送反馈邮件

---

**🎉 恭喜！你已经掌握了基本使用方法，开始享受AI辅助写作吧！**

*提示：建议将编辑器HTML文件添加到浏览器书签，方便随时使用。*
