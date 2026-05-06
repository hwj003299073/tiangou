from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# 舔狗日记库
dog_lines = [
    "我好像得了一种病，一不回我消息就心慌的病。",
    "你随便敷衍我吧，我不介意，我可以自己骗自己。",
    "没关系，你可以一直冷着我，我习惯了。",
    "你不用理我，我就是想告诉你我想你了。",
    "只要你理我一下，我就能开心一整天。",
    "我不找你不是不想你，是怕你烦我。",
    "你说什么都对，我永远站你这边。",
    "我可以一直等，等你想起我的那天。",
    "你不用回应我，我只是想对你好。",
    "你开心就好，我怎么样都无所谓。",
    "我不怕你忽冷忽热，我只怕你彻底不理我。",
    "你不用解释，我都信，我永远信你。",
    "我不困，你想聊多久我都陪你。",
    "我没事，你快去忙吧，不用管我。",
    "只要能陪着你，以什么身份都可以。",
    "你不用特意找我，我会一直找你。",
    "我不生气，真的不生气，你别不理我就好。",
    "我什么都能包容，除了你不理我。",
    "你的一句晚安，能让我安心睡到天亮。",
    "我不重要，你开心最重要。"
]

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 随机日记接口（给前端调用）
@app.route('/jianheng')
def generate():
    line = random.choice(dog_lines)
    return jsonify({"content": line})

# 评论提交接口（可选，这里用前端本地存储即可）
@app.route('/comment', methods=['POST'])
def comment():
    name = request.form.get('name')
    content = request.form.get('content')
    return jsonify({"status": "ok", "name": name, "content": content})

if __name__ == '__main__':
    app.run(debug=True)
