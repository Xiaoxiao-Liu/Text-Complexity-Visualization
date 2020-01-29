#encoding:utf-8

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    freqData = [{"Title": "乌木马的故事", "Content": {"NB": 29, "NC": 10, "ND": 24, "NE": 23, "NG": 1, "NH": 7, "NI": 13, "NL": 6, "PA": 67, "PB": 15, "PC": 17, "PD": 21, "PE": 13, "PF": 7, "PG": 23, "PK": 28}},
                {"Title": "海姑娘", "Content": {"NB": 49, "NC": 23, "ND": 25, "NE": 39, "NG": 3, "NH": 2, "NI": 17, "NL": 12, "PA": 105, "PB": 82, "PC": 25, "PD": 51, "PE": 25, "PF": 16, "PG": 41, "PK": 44}},
                {"Title": "渔夫和比目鱼", "Content": {"NB": 55, "NC": 21, "ND": 67, "NE": 42, "NG": 10, "NH": 8, "NI": 10, "NL": 29, "PA": 85, "PB": 50, "PC": 25, "PD": 51, "PE": 21, "PF": 11, "PG": 42, "PK": 19}},
                {"Title": "阿拉丁", "Content": {"NB": 11, "NC": 7, "ND": 23, "NE": 11, "NG": 7,"NH": 2, "NI": 5, "NL": 8, "PA": 124, "PB": 52, "PC": 21, "PD": 55, "PE": 7, "PF": 5, "PG": 29, "PK": 9}},
                {"Title": "阿里巴巴与四十大盗","Content": {"NB": 35, "NC": 27, "ND": 71, "NE": 25, "NG": 4, "NH": 3, "NI": 13, "NL": 9, "PA": 79,"PB": 27, "PC": 22, "PD": 27, "PE": 15, "PF": 25, "PG": 32, "PK": 10}},
                {"Title": "麦仑", "Content": {"NB": 43, "NC": 9, "ND": 26, "NE": 33, "NG": 4, "NH": 5, "NI": 15, "NK": 2, "NL": 16, "PA": 78, "PB": 65, "PC": 9, "PD": 27, "PE": 12, "PF": 11, "PG": 26, "PK": 21}},
                {"Title": "孔马康出走", "Content": {"NB": 66, "NC": 21, "ND": 59, "NE": 71, "NG": 3, "NH": 7, "NI": 27, "NL": 16, "PA": 111, "PB": 91, "PC": 19, "PD": 46, "PE": 21, "PF": 31, "PG": 41, "PK": 29}},
                {"Title": "睡着的国王", "Content": {"NB": 65, "NC": 9, "ND": 34, "NE": 28, "NG": 4, "NH": 1, "NI": 3, "NL": 12, "PA": 72, "PB": 20, "PC": 5, "PD": 20, "PE": 14, "PF": 4, "PG": 25, "PK": 20}},
                {"Title": "狐狸和狼", "Content": {"NB": 55, "NC": 21, "ND": 59, "NE": 34, "NG": 1, "NH": 20, "NI": 8, "NL": 21, "PA": 58, "PB": 39, "PC": 9, "PD": 39, "PE": 30, "PF": 6, "PG": 47, "PK": 7}}
                ]

    return render_template('index.html',**locals())


@app.route('/dataVis_2/')
def data_vis_2():
    freqData = [{"Title": "乌木马的故事",
                 "Content": {"NB": 29, "NC": 10, "ND": 24, "NE": 23, "NG": 1, "NH": 7, "NI": 13, "NL": 6, "PA": 67,
                             "PB": 15, "PC": 17, "PD": 21, "PE": 13, "PF": 7, "PG": 23, "PK": 28}},
                {"Title": "海姑娘",
                 "Content": {"NB": 49, "NC": 23, "ND": 25, "NE": 39, "NG": 3, "NH": 2, "NI": 17, "NL": 12, "PA": 105,
                             "PB": 82, "PC": 25, "PD": 51, "PE": 25, "PF": 16, "PG": 41, "PK": 44}},
                {"Title": "渔夫和比目鱼",
                 "Content": {"NB": 55, "NC": 21, "ND": 67, "NE": 42, "NG": 10, "NH": 8, "NI": 10, "NL": 29, "PA": 85,
                             "PB": 50, "PC": 25, "PD": 51, "PE": 21, "PF": 11, "PG": 42, "PK": 19}},
                {"Title": "阿拉丁",
                 "Content": {"NB": 11, "NC": 7, "ND": 23, "NE": 11, "NG": 7, "NH": 2, "NI": 5, "NL": 8, "PA": 124,
                             "PB": 52, "PC": 21, "PD": 55, "PE": 7, "PF": 5, "PG": 29, "PK": 9}},
                {"Title": "阿里巴巴与四十大盗",
                 "Content": {"NB": 35, "NC": 27, "ND": 71, "NE": 25, "NG": 4, "NH": 3, "NI": 13, "NL": 9, "PA": 79,
                             "PB": 27, "PC": 22, "PD": 27, "PE": 15, "PF": 25, "PG": 32, "PK": 10}},
                {"Title": "麦仑",
                 "Content": {"NB": 43, "NC": 9, "ND": 26, "NE": 33, "NG": 4, "NH": 5, "NI": 15, "NK": 2, "NL": 16,
                             "PA": 78, "PB": 65, "PC": 9, "PD": 27, "PE": 12, "PF": 11, "PG": 26, "PK": 21}},
                {"Title": "孔马康出走",
                 "Content": {"NB": 66, "NC": 21, "ND": 59, "NE": 71, "NG": 3, "NH": 7, "NI": 27, "NL": 16, "PA": 111,
                             "PB": 91, "PC": 19, "PD": 46, "PE": 21, "PF": 31, "PG": 41, "PK": 29}},
                {"Title": "睡着的国王",
                 "Content": {"NB": 65, "NC": 9, "ND": 34, "NE": 28, "NG": 4, "NH": 1, "NI": 3, "NL": 12, "PA": 72,
                             "PB": 20, "PC": 5, "PD": 20, "PE": 14, "PF": 4, "PG": 25, "PK": 20}},
                {"Title": "狐狸和狼",
                 "Content": {"NB": 55, "NC": 21, "ND": 59, "NE": 34, "NG": 1, "NH": 20, "NI": 8, "NL": 21, "PA": 58,
                             "PB": 39, "PC": 9, "PD": 39, "PE": 30, "PF": 6, "PG": 47, "PK": 7}}
                ]
    return render_template('dataVis_2.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
