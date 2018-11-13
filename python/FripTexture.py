from   PIL    import Image, ImageOps
import pandas as     pd

def Frip(Input, Output, mode, mirror, flip, Order):
    #テクスチャの読み込み・分離
    image_splited = Image.open(Input).split()
    def _mirror(p): return ImageOps.mirror(p) if mirror[len(img)] else p #左右反転
    def _flip(p)  : return ImageOps.  flip(p) if flip  [len(img)] else p #上下反転
    #左右反転・上下反転
    img = [];  [img.append(_flip(_mirror(t))) for t in image_splited]
    #チャンネル移動・テクスチャマスクの結合・画像データに変換して出力
    if   (mode == "RGBA") and (len(image_splited) == 4): #RGBA mode
        Image.merge("RGBA", [img[i] for i in Order[0:4]]).save(Output)
    elif (mode == "RGB")  or  (len(image_splited) == 3): #RGB  mode
        Image.merge("RGB",  [img[i] for i in Order[0:3]]).save(Output)

if __name__ == '__main__':
    print("Please enter the location of 'FripTexture.csv'")
    name_csv = input() #入力の取得
    try:               #ファイルの読み込み（空なら既定のcsv[FripTexture.csv]に）
        csv_input = pd.read_csv(name_csv if name_csv else '../csv/FripTexture.csv')
    except IOError:    #読み込み失敗
        print("File can't be found")
    else:              #読み込み成功
        for i in range(len(csv_input)):
            row = csv_input.iloc[i].tolist()            #csvの読み込み
            Input = row[0];  Output = row[1]
            if (Input == Input) and (Output == Output): #入出力先が指定されている事を確認してから実行
                Frip(Input, Output, row[2], row[3:7], row[7:11], row[11:15])
            else:                                       #空欄ならエラーメッセージを出力
                if Input  != Input:   print( "Input not specified / Row:{}".format(i))
                if Output != Output:  print("Output not specified / Row:{}".format(i))