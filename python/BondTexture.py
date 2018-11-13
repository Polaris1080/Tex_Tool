from   PIL    import Image
import pandas as     pd

def Bond(texture, Output):
    img      = [Image.open(i) if i==i else None  for i in texture] #テクスチャマスクの読み込み
    tex_size =    max([i.size if i    else (0,0) for i in img])    #サイズの確認（Noneなら０と判定）
    def Convert(p): #前処理
        if   (p == None):     return Image.new("L", tex_size, 0) #空欄(None)なら、空のテクスチャを生成。
        elif (p.mode == "L"): return p                           #モノクロなら、変換せずに出力。
        else:                 return p.split()[0]                #カラーなら、赤チャンネルを抽出。
    #テクスチャマスクの結合・画像データに変換して出力
    if None == img[-1]: #RGB
        del img[-1]     #リストの最後尾を削除してRGBに合わせる
        Image.merge("RGB",  [Convert(i) for i in img]).save(Output)
    else:               #RGBA
        Image.merge("RGBA", [Convert(i) for i in img]).save(Output)

if __name__ == '__main__':
    print("Please enter the location of 'BondTexture.csv'");  name_csv = input() #入力の取得
    try:            #ファイルの読み込み（空なら既定のcsv[BondTexture.csv]に）
        csv_input = pd.read_csv(name_csv if name_csv else '../csv/BondTexture.csv', dtype=str)
    except IOError: #読み込み失敗
        print("File can't be found")
    else:           #読み込み成功
        for i in range(len(csv_input)):
            row = csv_input.iloc[i].tolist();  Output = row[4]     #csvの読み込み
            if (Output == Output): Bond(row[0:4], Output)          #出力先が指定されている事を確認してから実行
            else: print('Output not specified / Row:{}'.format(i)) #空欄ならエラーメッセージを出力