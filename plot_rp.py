import matplotlib.pyplot as plt

# x = [0, 1, 2, 3] # x座標
# y = [1, 5, 2, 111] # y座標

# plt.plot(x, y, color="k") # 点列(x,y)を黒線で繋いだプロット
# # plt.show() # プロットを表示
# plt.savefig('img/test.png')

def plot_rp(rp_dict_list):
    img_path = 'img/test.png'
    x = []
    y = []
    for d in rp_dict_list:
        x.append(d['registerd_at'])
        y.append(d['rp'])
    plt.plot(x, y)
    plt.savefig(img_path)
    # print(x[0].year)
    return img_path