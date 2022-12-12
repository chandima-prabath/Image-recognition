from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_string():
    if request.method == 'POST':
            user_input = request.form['user_input']
                    if isinstance(user_input, str):
                                return 'It is a string'
                                        else:
                                                    return 'It is not a string'
                                                        else:
                                                                return '''
                                                                        <form method="POST">
                                                                                    Enter some text: <input type="text" name="user_input"><br>
                                                                                                <input type="submit" value="Submit"><br>
                                                                                                        </form>
                                                                                                                '''

                                                                                                                if __name__ == '__main__':
                                                                                                                    app.run()
                                                                                                                    