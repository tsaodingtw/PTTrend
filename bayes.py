# coding=utf-8
import numpy as np
import jieba

class Counter(dict):
    def __missing__(self, key):
        return 0

chinese_dict = Counter()
index = 0
def features(str):
    global index
    global chinese_dict
    x = np.zeros(10000)
    seg_list = jieba.cut(str)
    for i in seg_list:
        if chinese_dict[i] == 0:
            chinese_dict[i] = index
            index += 1
        x[chinese_dict[i]] += 1
    return x

#training data
#不是政治文
non_pol = "八卦版有宅宅 有大學生 也有兩者交集沒女友的悲憤大學宅宅 整天在宿舍發廢文 抱著粗音顆顆笑 孤單一個人 豪恐怖喔QQ 有沒有哪間大學宅宅最多的八卦？"
#是政治文
pol = "民進黨今天說，「出席WHA，新政府堅持主權與尊嚴」；新政府這次在沒有接受任何政治框架的前提，能夠順利受邀、出席、並完成演說，且獲得國際支持，這過程是關關難過關關過。民進黨中央今天透過官方臉書指出，面對政權交接的刁難，在國共的內外夾殺下，完成新政府上台後第一項艱鉅的國際任務。民進黨指出，政權交接時，馬政府即不斷威脅新政府需盡快提出衛福部部長人選，否則來不及完成報名；從3月起，馬政府和部分媒體不斷威脅恐嚇未收到邀請，來不及完成報名。交接小組不斷努力和各國友人組織溝通，5月7日確定收到邀請函。民進黨說，邀請函加註「依據聯合國2758號等決議所反映的一中原則」等文字，對台橫加政治框架。馬政府附和九二共識、一中各表造成回函各表；新政府回函強調沒有必要連結一中原則，台灣人民的健康與充分參與國際社會的權益，不能以任何政治框架加以限縮。民進黨指出，新政府以「沒有接受任何政治框架」前提回函，經各方努力溝通、協調順利完成報名確定成行，是得來不易的成果。民進黨說，衛生福利部長林奏延報到稱謂是部長，沒有被矮化成「醫師」。不同於前衛生署長葉金川在2009年出席，領到的第一張出席證是醫師，而非預期的「署長」。新政府的堅持和努力，沒有影響台灣的參與。民進黨並說，林奏延雖未和中國有雙邊會談，但仍和中國代表禮貌互動，且和其他各國雙邊會談不下過往，維持各國對台灣參與的支持肯定，也有多國友邦為台灣參與發表不平之鳴；經過多方會商、協談，林奏延順利登台演說，為台灣在國際發聲。"

non_pol_x = features(non_pol)
pol_x = features(pol)
X = np.array([non_pol_x, pol_x])
y = [0, 1]
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
print(clf.predict(non_pol_x))
print(clf.predict(pol_x))

test = ["民進黨", "哈哈交大哈哈ob'_'ov"]#第一篇是政治文，第二篇不是政治文
for i in test:
    print(clf.predict(features(i)))

