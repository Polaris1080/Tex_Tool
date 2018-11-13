from   PIL    import Image
import pandas as     pd

def UnBond(Target, Input):
    image = Image.open(Input) #テクスチャの読み込み
    img   = image.split()     #テクスチャの分離
    #チャンネル別に画像データに変換して出力
    if (image.mode == 'RGBA') or (image.mode == 'RGB'):
        [img[i].save(Target[i]) for i in range(len(img)) if Target[i]==Target[i]]
    else: #RGBA・RGB以外
        print("Can UnBond 'RGB(A)-Texture' only")
    
if __name__ == '__main__':
    print("Please enter the location of 'UnBondTexture.csv'");  name_csv = input() #入力の取得
    try:            #ファイルの読み込み（空なら既定のcsv[UnBondTexture.csv]に）
        csv_input = pd.read_csv(name_csv if name_csv else "../csv/UnBondTexture.csv", dtype=str)
    except IOError: #読み込み失敗
        print("File can't be found")
    else:           #読み込み成功
        for i in range(len(csv_input)):
            row = csv_input.iloc[i].tolist();  Input = row[4]       #csvの読み込み
            if Input == Input:  UnBond(row[0:4], Input)             #出力先が指定されている事を確認してから実行
            else:  print('Output not specified / Row:{}'.format(i)) #空欄ならエラーメッセージを出力