from flask import Flask, render_template, request, send_file, redirect
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    file.save("input.txt")
    model_type = request.form['model']

    if model_type == 'word-frequency':
        analyze_word_frequency()

        result_file = f"../../Documents/Sogang Uni/2학년1학기/빅데이터비즈니스플랫폼개발(이동훈)/강의자료/7주차 Data Analytics Service/DataAnalyticsService - SHARE/static/result/result.txt"
        return send_file(result_file,
                         mimetype='text/plain',
                         attachment_filename='result.txt',
                         as_attachment=True)

    elif model_type == 'word-cloud':
        analyze_word_cloud()

        result_file = f"../../Documents/Sogang Uni/2학년1학기/빅데이터비즈니스플랫폼개발(이동훈)/강의자료/7주차 Data Analytics Service/DataAnalyticsService - SHARE/static/result/result.png"
        return send_file(result_file,
                         mimetype='image/png',
                         attachment_filename='result.png',
                         as_attachment=True)

    # word-stemming 모델을 선택하였을 때
    elif model_type == '':
        print("아래 코드를 작성하세요")
        # stemming 함수 호출

        # stemming 결과인 result.txt를 다운로드


    else:
        return redirect('/')

    return redirect('/')


def stemming():
    # input.txt File Open

    # open한 파일을 utf-8로 디코딩

    # nltk의 PorterStemmer()를 활용하여 Stemming
    # stemmer = PorterStemmer()
    # stemmed_data = stemmer.stem(data)

    # Stemming 한 결과를 static\result\result.txt 파일에 저장
    # with open(f'.\\static\\result\\result.txt', 'w', encoding='utf8') as f:
    #     f.write("%s \n" % stemmed_data)
    # f.close()

    return


def analyze_word_frequency():
    nltk.download('punkt')

    with open(
            "../../Documents/Sogang Uni/2학년1학기/빅데이터비즈니스플랫폼개발(이동훈)/강의자료/7주차 Data Analytics Service/DataAnalyticsService - SHARE/input.txt", "rb") as file:
        data = file.read()

    data = data.decode("utf-8")

    tokenized_word = word_tokenize(data)

    freq_dist = FreqDist(tokenized_word)

    freq_dist_list = [(word, freq) for word, freq in freq_dist.items()]
    with open(
            f'../../Documents/Sogang Uni/2학년1학기/빅데이터비즈니스플랫폼개발(이동훈)/강의자료/7주차 Data Analytics Service/DataAnalyticsService - SHARE/static/result/result.txt', 'w', encoding='utf8') as f:
        for item in freq_dist_list:
            f.write("%s %s\n" % (item[0], item[1]))
    f.close()
    return


def analyze_word_cloud():
    with open(
            "../../Documents/Sogang Uni/2학년1학기/빅데이터비즈니스플랫폼개발(이동훈)/강의자료/7주차 Data Analytics Service/DataAnalyticsService - SHARE/input.txt", "rb") as file:
        data = file.read()

    data = data.decode("utf-8")

    cloud = WordCloud(background_color='white',
                      width=800, height=800).generate(data)

    plt.imshow(cloud)
    plt.axis('off')

    plt.savefig(f".\\static\\result\\result.png")

    return


if __name__ == '__main__':
    app.run()
