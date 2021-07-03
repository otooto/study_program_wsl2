#!usr/bin/env python3
#-*- conding: utf-8 -*-

from pdfminer.high_level import extract_text
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import time

def main():

    #ここからpdfのテキスト化
    
    print("読み込むファイル名を拡張子まで含めて入力してください")
    FALE_PATH = str(input())
    
    text = extract_text(FALE_PATH,maxpages=2)

    f = open('m.txt','w')

    f.write(text)

    f.close()

    #ここから翻訳

    translator = Translator()

    f = open('m.txt','r')

    ff = open('file.txt','w')

    s = f.read()

    sl = s.split('\n')#改行で1行1行に分ける。戻り値はlistになる。

    count = 0#読み込んだ行数のカウント
    break_count = 0#読み込んだ行数の内、空白行のカウント

    for line in sl:

        if line == '':#空白行はエラーになるので反映はしない
            ff.write('\n')
            break_count += 1
            continue

        else:#グーグル翻訳
            data2 = translator.translate(line,dest='ja',src='en')
            ff.write(data2.text + '\n')

        count += 1

    f.close()

    ff.close()

    print("終了しました。")

    print('処理時間は{}秒です'.format(count - break_count))#空白行分を抜いたグーグル翻訳を行った行



if __name__ == '__main__':

    t1 = time.time() 
    main()
    t2 = time.time()
    elapsed_time = t2-t1
    print(f"経過時間：{elapsed_time}")
"""

def create_pdf():

    test_data = open("translation_file.txt", "r")
    # すべての内容を読み込む
    contents = test_data.read()
    #pdfを生成
    c = canvas.Canvas('sample.pdf', pagesize=portrait(A4))

    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    #フォントを指定
    c.setFont('HeiseiKakuGo-W5', 10)
    w, h = A4
    c.drawCentredString(w / 2, h / 2, contents)
    print("起動")

    #c.showPage()

    test_data.close()

    #pdfとして保存
    c.save()


raise TypeError(f'the JSON object must be str, bytes or bytearray, '
TypeError: the JSON object must be str, bytes or bytearray, not NoneType
"""