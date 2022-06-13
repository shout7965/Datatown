import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from flask import Flask, render_template, jsonify, send_file, redirect
from flask.globals import request
from flask_cors import CORS
from wordcloud import WordCloud
from crawl_basic import get_basic
from crawl_total import get_total
from chart_builder import make_chart
from crawl_job import get_job_list
from crawl_job import get_job_count
import requests
import matplotlib.pyplot as plt


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )
CORS(app)

@app.route('/')
def dashboard():
    # category1_job_list = get_job_list("161")
    # category2_job_list = get_job_list("162")

    basic = get_basic()
    total = get_total()

    # make_chart()

    return render_template('index_competition.html',
                           # category1_job_list=category1_job_list,
                           # category2_job_list=category2_job_list,
                           basic=basic,
                           total=total
                           )

# @app.route('/weather_forecast')
# def get_weather_forecast_info():
#     result = requests.get(
#         'https://api.openweathermap.org/data/2.5/onecall?lat=37.413294&lon=126.734086&exclude=current,minutely,hourly,alerts&appid=3c9021aa10b48b8251d6555460a9f989&units=metric')
#     json_result = result.json()
#
#     return jsonify(json_result['daily'])

# @app.route('/job_trend_161')
# def get_job_trend_161():
#     job_count_161 = get_job_count("161")
#
#     return jsonify(job_count_161)
#
# @app.route('/job_trend_162')
# def get_job_trend_162():
#     job_count_162 = get_job_count("162")
#
#     return jsonify(job_count_162)

@app.route('/basic')
def dashboard_basic():
    basic = get_basic()

    return jsonify(basic)

@app.route('/total')
def dashboard_total():
    total = get_total()

    return jsonify(total)

# @app.route('/file')
# def file_form():
#     return render_template('file_form.html')
#
# @app.route('/fileupload', methods=['POST'])
# def file_upload():
#     file = request.files['file']
#     print(file)
#     file.save(file.filename)
#
#     return 'File Uploaded'
#
# @app.route('/form')
# def form():
#     return render_template('form.html')
#
# @app.route('/submit', methods=['POST'])
# def submit():
#
#     print(request.form)
#     print(request.form['email'])
#     print(request.form['password'])
#     print(request.form['gender'])
#     return "OK"
#
# @app.route('/analyze_form')
# def analyze_form():
#     return render_template('analyze_form.html')
#
# @app.route('/analyze', methods=['POST'])
# def analyze():
#     file = request.files['file']
#     file.save("input.txt")
#     model_type = request.form['model']
#
#     if model_type == 'word-frequency':
#         analyze_word_frequency()
#
#         result_file = f".\\static\\result\\result.txt"
#         return send_file(result_file,
#                          mimetype='text/plain',
#                          download_name='result.txt',
#                          as_attachment=True)
#
#     elif model_type == 'word-cloud':
#         analyze_word_cloud()
#
#         result_file = f".\\static\\result\\result.png"
#         return send_file(result_file,
#                          mimetype='image/png',
#                          download_name='result.png',
#                          as_attachment=True)
#
#     # word-stemming 모델을 선택하였을 때
#     elif model_type == 'word-stemming':
#         print("아래 코드를 작성하세요")
#         # stemming 함수 호출
#         stemming()
#
#         # stemming 결과인 result.txt를 다운로드
#         result_file = f".\\static\\result\\result.txt"
#         return send_file(result_file,
#                          mimetype='text/plain',
#                          download_name='result.txt',
#                          as_attachment=True)
#
#     else:
#         return redirect('/')
#
#     return redirect('/')
#
# def stemming():
#     # input.txt File Open
#     with open(
#             ".\\input.txt", "rb") as file:
#         data = file.read()
#
#     # open한 파일을 utf-8로 디코딩
#     data = data.decode("utf-8")
#
#     # nltk의 PorterStemmer()를 활용하여 Stemming
#     stemmer = PorterStemmer()
#     stemmed_data = stemmer.stem(data)
#
#     # Stemming 한 결과를 static\result\result.txt 파일에 저장
#     with open(f'.\\static\\result\\result.txt', 'w', encoding='utf8') as f:
#          f.write("%s \n" % stemmed_data)
#     f.close()
#
#     return
#
# def analyze_word_frequency():
#     nltk.download('punkt')
#
#     with open(
#             ".\\input.txt", "rb") as file:
#         data = file.read()
#
#     data = data.decode("utf-8")
#
#     tokenized_word = word_tokenize(data)
#
#     freq_dist = FreqDist(tokenized_word)
#
#     freq_dist_list = [(word, freq) for word, freq in freq_dist.items()]
#     with open(f'.\\static\\result\\result.txt', 'w', encoding='utf8') as f:
#         for item in freq_dist_list:
#             f.write("%s %s\n" % (item[0], item[1]))
#     f.close()
#     return
#
# def analyze_word_cloud():
#     with open(
#             ".\\input.txt", "rb") as file:
#         data = file.read()
#
#     data = data.decode("utf-8")
#
#     cloud = WordCloud(background_color='white',
#                       width=800, height=800).generate(data)
#
#     plt.imshow(cloud)
#     plt.axis('off')
#
#     plt.savefig(f".\\static\\result\\result.png")
#
#     return

if __name__ == '__main__':
    app.run(debug=True)
