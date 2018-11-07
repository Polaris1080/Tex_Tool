from   PIL    import Image
import pandas as     pd

def UnBond(Target,Input):
    img = Image.open(Input).split();  ch = len(img)  #ファイル読み込み → チャンネル分割
    if (ch == 3) or (ch == 4): #カラーモード確認("RGB"or"RBGA") → 出力先が指定されている時のみ出力
        [img[i].save(Target[i]) for i in range(ch) if Target[i]==Target[i]]
    else:  print("Can UnBond 'RGB(A)-Texture' only") #RGB(A)以外なら、エラーメッセージを出力
    
if __name__ == '__main__':
    print("Please enter the location of 'UnBondTexture.csv'");  name_csv = input() #入力を受け付ける    
    try:            #csvを読み込む（空なら既定のcsv[UnBondTexture.csv]に）
        csv_input = pd.read_csv(name_csv if name_csv else "../csv/UnBondTexture.csv", dtype=str)
    except IOError: #ファイルが存在しない場合
        print("File can't be found")
    else:           #ファイルが読み込める場合
        for i in range(len(csv_input)):      #一行ごとに実行していく
            row = csv_input.iloc[i].tolist() #出力先が指定されている事を確認
            if row[4] == row[4]:  UnBond(row[0:4], row[4])          #指定されているなら実行
            else:  print('Output not specified / Row:{}'.format(i)) #空ならばエラーメッセージを出力