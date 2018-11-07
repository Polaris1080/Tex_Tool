from   PIL    import Image, ImageOps
import pandas as     pd

def Frip(Input, Output, mode="RGBA", mirror=[False]*4, flip=[False]*4, Order=[0,1,2,3]):
    image_splited = Image.open(Input).split()            #読み込み → チャンネル分割
    def _mirror(p): return ImageOps.mirror(p) if mirror[len(img)] else p #左右反転
    def _flip(p)  : return ImageOps.  flip(p) if flip  [len(img)] else p #上下反転
    img = [];     [img.append(_flip(_mirror(t))) for t in image_splited] #画像処理
    #チャンネルを並び替え → 結合 → 保存
    if   (mode == "RGBA") and (len(image_splited) == 4): #RGBA mode
        Image.merge("RGBA", [img[i] for i in Order[0:4]]).save(Output)
    elif (mode == "RGB")  or  (len(image_splited) == 3): #RGB  mode
        Image.merge("RGB",  [img[i] for i in Order[0:3]]).save(Output)

if __name__ == '__main__':
    print("Please enter the location of 'FripTexture.csv'")
    name_csv = input() #入力を受け付ける
    try:               #csvを読み込む、空なら既定のcsv(FripTexture.csv)に
        csv_input = pd.read_csv(name_csv if name_csv else '../csv/FripTexture.csv')
    except IOError:    #ファイルが存在しない場合
        print("File can't be found")
    else:              #ファイルが読み込める場合
        for i in range(len(csv_input)): #一行ごとに実行していく
            row = csv_input.iloc[i].tolist();  Input = row[0];  Output = row[1]
            if (Input == Input) and (Output == Output): #入出力が指定されている事を確認
                Frip(Input, Output, row[2], row[3:7], row[7:11], row[11:15])
            else: #エラーメッセージの表示
                if Input  != Input:   print( "Input not specified / Row:{}".format(i))
                if Output != Output:  print("Output not specified / Row:{}".format(i))