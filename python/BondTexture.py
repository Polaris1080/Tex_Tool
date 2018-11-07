from   PIL    import Image
import pandas as     pd

def Bond(texture,Output):
    #ファイル読み込み（指定されていなければNone）
    img      = [Image.open(i) if i==i else None for i in texture]
    #テクスチャのサイズ(px)を確認（Noneなら０と判定）
    tex_size = max([i.size if i else (0,0) for i in img])
    def Convert(p): #None：０埋め L：変換無し RGB(A)：Rチャンネルを抽出
        if (p == None) : return Image.new("L", tex_size, 0)
        else: return p if (p.mode == "L") else p.split()[0]
    #RGBチャンネルを結合 → 画像データに変換 → ファイルに出力
    if  None == img[-1]:  Image.merge("RGBA", [Convert(i) for i in img]).save(Output)
    else:   del img[-1];  Image.merge("RGB",  [Convert(i) for i in img]).save(Output)

if __name__ == '__main__':
    print("Please enter the location of 'BondTexture.csv'");  name_csv = input() #入力を受け付ける
    try:            #csvを読み込む、空なら既定のcsv(BondTexture.csv)に
        csv_input = pd.read_csv(name_csv if name_csv else '../csv/BondTexture.csv', dtype=str)
    except IOError: #ファイルが存在しない場合
        print("File can't be found")
    else:           #ファイルが読み込める場合
        for i in range(len(csv_input)):                            #一行ごとに実行していく
            row = csv_input.iloc[i].tolist();  Output = row[4]     #出力先が指定されている事を確認
            if (Output == Output): Bond(row[0:4], Output)          #指定されているなら実行、
            else: print('Output not specified / Row:{}'.format(i)) #空ならばメッセージを出力