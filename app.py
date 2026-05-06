from flask import Flask, render_template, jsonify, request
import random
import json
import os

app = Flask(__name__)

# 舔狗语录库
dog_lines = [
    "我好像得了一种病，一不回我消息就心慌的病。",
    "你随便敷衍我吧，我不介意，我可以自己骗自己。",
    "没关系，你可以一直冷着我，习惯了。",
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
    "我不生气，别不理我就好。",
    "我什么都能包容，除了你不理我。",
    "你的一句晚安，能让我安心睡到天亮。",
    "我不重要，你开心最重要。"
]

# ===================== JSON 持久化存储评论 =====================
COMMENTS_FILE = "comments.json"

# 初始化 JSON 文件
def init_comments_file():
    if not os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

# 读取评论
def load_comments():
    with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存评论
def save_comments(comments):
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

init_comments_file()

# ===================== 路由 =====================
@app.route('/')
def index():
    return render_template('index.html')

# 随机日记接口
@app.route('/jianheng')
def generate():
    line = random.choice(dog_lines)
    return jsonify({"content": line})

# 发表评论
@app.route('/api/comment/add', methods=['POST'])
def add_comment():
    name = request.form.get('name', '').strip()
    content = request.form.get('content', '').strip()

    if not name or not content:
        return jsonify({"ok": False, "msg": "姓名和内容不能为空"})

    comments = load_comments()
    # 最新评论放最前面
    comments.insert(0, {
        "name": name,
        "content": content
    })
    save_comments(comments)
    return jsonify({"ok": True})

# 获取所有评论
@app.route('/api/comment/list')
def get_comments():
    return jsonify(load_comments())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
