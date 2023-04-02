from flask import Flask, request
import openai
import ssl

app = Flask(__name__)

# Установите ключ API OpenAI
openai.api_key = "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"

# Создайте контекст SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/path/to/cert', '/path/to/key')

# Определите функцию-обработчик POST-запросов
@app.route('/', methods=['POST'])
def handle_request():
    # Получить вопрос пользователя из запроса
    user_input = request.form['user_input']

    # Сгенерировать ответ с помощью модели GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Отправить ответ пользователю
    return str(response.choices[0].text)

if __name__ == '__main__':
    # Запустить приложение с поддержкой HTTPS и SSL
    app.run(host='0.0.0.0', port=443, ssl_context=context)

