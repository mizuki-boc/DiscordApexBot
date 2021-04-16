import matplotlib.pyplot as plt
# pyplotモジュールを"plt"という名前でインポートする

x = [0, 1, 2, 3] # x座標
y = [1, 5, 2, 111] # y座標

plt.plot(x, y, color="k") # 点列(x,y)を黒線で繋いだプロット
# plt.show() # プロットを表示
plt.savefig('img/test.png')

def plot_rp()