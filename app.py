from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 舔狗语录库
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

# 生成语录接口
@app.route('/jianheng')
def generate():
    line = random.choice(dog_lines)
    return jsonify({"content": line})

if __name__ == '__main__':
    app.run(debug=True)