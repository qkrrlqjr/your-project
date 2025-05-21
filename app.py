from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/skill', methods=['POST'])
def skill():
    data = request.get_json()
    user_utterance = data.get('userRequest', {}).get('utterance', '')

    if '메뉴' in user_utterance:
        response_text = '저희 메뉴는 김밥, 라면, 돈까스가 있습니다.'
    else:
        response_text = '무슨 말인지 잘 모르겠어요.'

    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": response_text
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
