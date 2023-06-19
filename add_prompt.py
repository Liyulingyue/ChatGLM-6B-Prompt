# run the file to add a prompt
# dont push the file



# 读取配置信息
import json
with open('prompts.json') as f:
    data = json.load(f)

# 添加一个新的Prompt
a_prompt = {'name': '请输入一个简单易懂的名称',
            'prompt': '请输入你的Prompt，以&*keys*&作为占位符，用于替换用户输入的内容',
            'example_input': '一个示例输入',
            'introduction': "对这个Prompt的介绍"}
data.append(a_prompt)

# 保存到文件中
with open('prompts.json','w') as f:
    json.dump(data,f)