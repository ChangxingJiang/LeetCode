from typing import List


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        dp = [0] * n  # dp[i]表示到i个箱子的最小路径
        ans = 0  # 持续维护为当前窗口的路程总和

        left = -1  # left=窗口左侧边界
        for right in range(n):  # right=窗口右侧边界
            maxBoxes -= 1
            maxWeight -= boxes[right][1]

            # 从仓库出发的一趟新旅程（增加来回两趟）
            if right == left + 1:
                ans += 2

            # 和上一个箱子不是同一个目标（增加从港口到港口的一趟）
            elif boxes[right][0] != boxes[right - 1][0]:
                ans += 1

            # 移动窗口的左侧边缘（如果dp[left]==dp[left+1]，那么说明窗口左侧边缘可以无损地向右移动，直接向右移动即可）
            while maxBoxes < 0 or maxWeight < 0 or (left < right - 1 and dp[left] == dp[left + 1]):
                left += 1
                maxBoxes += 1
                maxWeight += boxes[left][-1]
                if boxes[left][0] != boxes[left + 1][0]:
                    ans -= 1

            dp[right] = dp[left] + ans

        return dp[-1]


if __name__ == "__main__":
    # 4
    print(Solution().boxDelivering(boxes=[[1, 1], [2, 1], [1, 1]], portsCount=2, maxBoxes=3, maxWeight=3))

    # 6
    print(Solution().boxDelivering(boxes=[[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], portsCount=3, maxBoxes=3,
                                   maxWeight=6))

    # 6
    print(Solution().boxDelivering(boxes=[[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], portsCount=3, maxBoxes=6,
                                   maxWeight=7))

    # 14
    print(Solution().boxDelivering(boxes=[[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]],
                                   portsCount=5, maxBoxes=5, maxWeight=7))

    # 214
    print(Solution().boxDelivering(
        boxes=[[48, 52899], [47, 19850], [33, 29679], [69, 33222], [58, 701], [30, 76794], [25, 81170], [73, 23227],
               [55, 20126], [44, 36120], [45, 31939], [67, 19736], [68, 38178], [17, 83260], [38, 15272], [38, 78703],
               [35, 17238], [75, 18299], [8, 20643], [23, 49506], [64, 11294], [57, 52676], [50, 72049], [18, 62783],
               [72, 47322], [58, 17174], [33, 91245], [41, 20540], [9, 52226], [8, 56422], [38, 67101], [55, 84871],
               [10, 22701], [13, 65749], [10, 75225], [27, 13437], [5, 82776], [53, 69170], [40, 19975], [71, 52129],
               [56, 92827], [77, 91290], [34, 52128], [49, 42076], [65, 14024], [11, 20086], [54, 72018], [64, 64707],
               [43, 53637], [18, 81304], [34, 769], [33, 7418], [60, 1473], [44, 16057], [45, 81799], [50, 91388],
               [2, 88844], [50, 19037], [50, 24485], [2, 79102], [3, 34503], [49, 89167], [18, 18198], [30, 76362],
               [61, 51312], [53, 25332], [53, 85378], [43, 31053], [74, 8190], [55, 22288], [56, 48727], [66, 45387],
               [12, 53165], [46, 66319], [48, 47049], [34, 4879], [20, 35950], [27, 80365], [59, 42479], [50, 17398],
               [63, 26273], [27, 78622], [57, 27062], [16, 53519], [42, 31522], [39, 26623], [35, 71692], [33, 72780],
               [23, 17746], [2, 939], [47, 3748], [63, 71487], [25, 92114], [58, 48662], [24, 45749], [64, 63233],
               [26, 92359], [29, 11382], [58, 785], [59, 11024], [60, 55275], [50, 66923], [10, 6771], [61, 31311],
               [76, 61562], [69, 22497], [29, 24471], [43, 90635], [38, 40760], [64, 87184], [7, 19793], [47, 47690],
               [69, 9570], [39, 16271], [75, 87064], [26, 26233], [53, 69585], [29, 68502], [37, 16523], [34, 10484],
               [22, 88729], [31, 80116], [10, 17864], [33, 47739], [53, 67300], [21, 68588], [69, 58835], [75, 79944],
               [76, 13923]],
        portsCount=77, maxBoxes=17, maxWeight=93070))

    # 1243
    print(Solution().boxDelivering(
        boxes=
        [[70, 4218], [120, 18433], [110, 22269], [78, 12839], [20, 27342], [84, 10528], [104, 39546], [108, 14907],
         [8, 13698], [105, 34242], [98, 9409], [73, 5257], [133, 19449], [86, 29201], [11, 12639], [79, 30639],
         [132, 16935], [158, 12674], [132, 24101], [134, 8190], [90, 26503], [30, 16863], [110, 32868], [137, 14955],
         [128, 37645], [97, 36448], [82, 35207], [68, 13740], [132, 30738], [57, 18454], [83, 28997], [17, 28547],
         [64, 33779], [121, 18477], [21, 10010], [86, 37423], [156, 15291], [100, 3769], [103, 3178], [94, 6410],
         [114, 16567], [94, 34549], [49, 7717], [56, 958], [138, 2360], [91, 31529], [35, 20145], [5, 40149],
         [41, 39314], [53, 30440], [127, 12838], [134, 6306], [31, 4503], [75, 19140], [89, 1119], [116, 19568],
         [65, 22148], [32, 6598], [64, 14414], [99, 2215], [116, 5821], [85, 28108], [45, 17320], [95, 25607],
         [145, 3836], [132, 4135], [41, 424], [105, 10368], [2, 796], [13, 3935], [112, 830], [128, 20604],
         [129, 26011], [23, 41490], [60, 21158], [79, 21133], [12, 25270], [11, 3342], [154, 25815], [134, 14892],
         [82, 23924], [60, 17454], [36, 16981], [5, 38746], [13, 25085], [18, 5966], [139, 20755], [101, 20828],
         [132, 40627], [13, 31712], [30, 22530], [141, 37388], [112, 33145], [58, 20773], [65, 671], [136, 6445],
         [4, 23850], [72, 27540], [20, 5067], [87, 9004], [127, 25010], [87, 9097], [140, 13880], [155, 9321],
         [100, 35034], [59, 2832], [100, 19148], [70, 16955], [23, 148], [125, 2718], [65, 15093], [125, 4656],
         [90, 32745], [52, 8824], [82, 600], [55, 30983], [52, 23859], [39, 11034], [60, 41316], [108, 6386],
         [12, 22004], [74, 17058], [19, 24940], [28, 29119], [79, 13674], [8, 1745], [54, 20860], [78, 40885],
         [98, 30315], [32, 31804], [17, 13019], [58, 26523], [63, 6816], [74, 27976], [99, 18240], [102, 25677],
         [77, 22440], [18, 30761], [119, 16321], [21, 11434], [82, 18024], [109, 22674], [25, 20346], [65, 27824],
         [12, 34936], [151, 29156], [78, 38027], [54, 10083], [154, 23902], [81, 1147], [132, 10336], [106, 27915],
         [5, 750], [114, 22153], [113, 24219], [137, 21120], [48, 16927], [152, 10162], [54, 29645], [83, 17733],
         [34, 4796], [10, 27719], [56, 17966], [131, 19238], [37, 20318], [53, 39737], [62, 34193], [90, 25403],
         [29, 13521], [33, 4084], [38, 34965], [140, 22538], [14, 33348], [84, 5611], [17, 32848], [137, 30910],
         [55, 30801], [104, 21344], [137, 20581], [41, 40335], [25, 40866], [72, 30675], [127, 18821], [27, 33268],
         [57, 16987], [4, 16317], [98, 10822], [145, 36078], [125, 5366], [42, 32446], [7, 18260], [79, 34946],
         [16, 37208], [101, 3467], [125, 39835], [16, 1101], [4, 37180], [152, 24588], [77, 13289], [120, 16586],
         [113, 23260], [30, 39806], [3, 32540], [157, 31743], [103, 15971], [6, 34319], [48, 6657], [70, 5224],
         [35, 39128], [145, 22766], [138, 644], [153, 19175], [18, 39163], [78, 24920], [62, 26122], [1, 3941],
         [72, 37471], [63, 28357], [105, 11172], [124, 26100], [39, 17770], [131, 14261], [18, 34879], [42, 35871],
         [78, 29158], [107, 38404], [103, 4391], [149, 761], [158, 39719], [49, 8021], [73, 23685], [83, 34608],
         [156, 2073], [17, 18444], [138, 25469], [1, 9128], [130, 30892], [58, 8412], [38, 20214], [109, 18849],
         [26, 36862], [132, 35957], [118, 6583], [106, 20542], [49, 3010], [16, 8600], [104, 39098], [157, 23107],
         [142, 6029], [75, 11811], [36, 36461], [8, 12933], [37, 32711], [154, 5659], [61, 6232], [147, 15471],
         [14, 33330], [27, 18912], [78, 34610], [115, 8865], [87, 19881], [63, 24145], [9, 5557], [144, 38315],
         [67, 23483], [32, 3501], [94, 20676], [103, 12634], [103, 27282], [89, 4732], [29, 24393], [60, 31885],
         [88, 33101], [25, 11611], [17, 5349], [5, 38105], [54, 4904], [141, 13917], [12, 996], [103, 5015],
         [95, 21555], [6, 21471], [72, 28609], [145, 3865], [98, 19699], [7, 27467], [21, 37722], [154, 24750],
         [77, 18371], [134, 36551], [44, 11885], [156, 26999], [74, 13938], [63, 15147], [94, 20809], [10, 39174],
         [125, 32841], [29, 19524], [95, 40042], [68, 18709], [28, 40235], [137, 14978], [81, 4664], [103, 6588],
         [74, 32953], [30, 27416], [5, 32197], [24, 3653], [129, 13545], [3, 32114], [51, 22398], [20, 15503],
         [98, 14689], [14, 6116], [61, 38677], [35, 38422], [125, 35233], [108, 40236], [106, 17946], [20, 27906],
         [147, 30545], [111, 8559], [59, 19993], [49, 31738], [137, 37839], [94, 18776], [6, 30976], [19, 22119],
         [40, 30829], [47, 37793], [63, 27718], [153, 5859], [55, 38997], [85, 15986], [58, 33896], [102, 17808],
         [79, 11471], [97, 606], [26, 14374], [145, 25565], [121, 24508], [54, 28592], [128, 4559], [130, 10533],
         [2, 28732], [62, 6875], [68, 34935], [144, 2668], [71, 32405], [144, 34423], [129, 5650], [144, 17438],
         [28, 36779], [147, 38180], [55, 31165], [92, 7058], [4, 9922], [96, 26938], [59, 24932], [54, 26222],
         [42, 28045], [54, 3217], [84, 544], [157, 12619], [51, 40083], [49, 24152], [156, 23202], [57, 35877],
         [41, 11829], [123, 3000], [8, 17462], [133, 13734], [114, 13539], [56, 19624], [25, 12684], [151, 14199],
         [154, 14915], [52, 6365], [128, 15711], [90, 401], [29, 40568], [38, 17782], [146, 4292], [55, 33364],
         [89, 23192], [9, 36140], [66, 40983], [4, 6302], [8, 12309], [74, 40199], [7, 11248], [132, 2829], [66, 11173],
         [40, 17603], [74, 18027], [104, 22697], [68, 11439], [99, 16371], [147, 4755], [83, 37183], [156, 40860],
         [83, 2574], [32, 11710], [114, 15387], [39, 23427], [39, 6145], [120, 31213], [16, 18926], [152, 886],
         [106, 33843], [15, 23493], [143, 17849], [4, 34869], [71, 11669], [27, 18064], [80, 15976], [78, 38601],
         [110, 36294], [60, 6453], [151, 5655], [67, 18752], [66, 560], [29, 30027], [120, 4800], [39, 36369],
         [125, 19872], [15, 21421], [53, 11403], [118, 12483], [60, 18311], [37, 11490], [137, 20447], [114, 21319],
         [38, 4912], [153, 32375], [123, 26510], [38, 7003], [72, 32330], [147, 19172], [14, 5067], [102, 25447],
         [43, 2714], [34, 31060], [151, 12046], [156, 32032], [59, 5997], [28, 36], [34, 6712], [54, 27703],
         [42, 38433], [29, 35805], [52, 17597], [153, 17169], [128, 3353], [39, 18288], [149, 5233], [19, 1939],
         [126, 15834], [83, 37313], [66, 27359], [118, 34244], [80, 10663], [81, 20052], [146, 18294], [61, 21827],
         [20, 30850], [57, 38302], [147, 18777], [2, 10778], [122, 17644], [108, 2291], [26, 37119], [108, 27911],
         [151, 23201], [31, 26877], [96, 28672], [44, 4473], [87, 6974], [89, 26082], [130, 14696], [130, 19162],
         [67, 25831], [23, 24523], [31, 10562], [153, 31378], [50, 16517], [89, 15220], [63, 19298], [91, 9359],
         [101, 1418], [105, 4488], [113, 33041], [143, 34847], [87, 15848], [68, 29557], [104, 12038], [47, 11617],
         [34, 40129], [42, 7857], [117, 33694], [82, 34461], [157, 37350], [87, 1586], [111, 363], [37, 5313],
         [78, 30171], [123, 22884], [9, 12360], [12, 37651], [85, 36765], [95, 11672], [98, 24146], [105, 40087],
         [77, 4737], [154, 22109], [157, 15326], [47, 30602], [32, 8495], [46, 11835], [124, 40220], [91, 37037],
         [37, 39646], [136, 13803], [91, 18527], [109, 40941], [61, 12009], [85, 20252], [158, 8044], [28, 4064],
         [51, 3529], [151, 26139], [59, 17581], [56, 36061], [85, 39543], [123, 22175], [65, 23557], [141, 8166],
         [153, 20988], [97, 38193], [6, 25370], [152, 15203], [126, 32787], [78, 25258], [60, 33880], [125, 17296],
         [126, 5179], [48, 25476], [29, 13422], [63, 21077], [47, 40108], [56, 33666], [111, 13980], [130, 36751],
         [48, 17459], [52, 17807], [109, 27927], [128, 40088], [118, 41345], [148, 12062], [61, 18532], [13, 36568],
         [71, 3930], [83, 18555], [153, 32290], [152, 39393], [52, 23378], [97, 5239], [114, 21889], [86, 14011],
         [41, 18570], [138, 2895], [32, 22898], [62, 23912], [155, 5521], [106, 9534], [28, 4100], [104, 19120],
         [128, 7783], [140, 30231], [59, 24717], [135, 16807], [56, 4492], [82, 36252], [37, 38114], [115, 25425],
         [132, 3384], [6, 31603], [116, 5112], [92, 34346], [79, 29893], [141, 20391], [56, 37242], [91, 2055],
         [140, 17216], [53, 28662], [23, 4854], [15, 25012], [147, 28869], [78, 7042], [10, 29952], [9, 41447],
         [45, 27802], [81, 39733], [76, 18860], [145, 5244], [61, 1010], [59, 23326], [1, 13966], [113, 10806],
         [147, 16033], [105, 40780], [38, 3761], [49, 15332], [84, 7413], [109, 15532], [155, 41417], [134, 38771],
         [40, 20272], [81, 30056], [139, 17225], [46, 2410], [34, 5093], [101, 41205], [134, 26217], [109, 25997],
         [92, 391], [49, 26440], [7, 16286], [148, 34065], [17, 34736], [87, 11723], [46, 14790], [78, 26874],
         [6, 32801], [68, 35555], [6, 13223], [70, 32969], [47, 19022], [17, 29844], [1, 3509], [27, 17964],
         [37, 12499], [28, 36841], [25, 28216], [16, 13846], [17, 32355], [36, 23411], [21, 1140], [85, 6066], [94, 56],
         [61, 12607], [101, 27596], [148, 28253], [138, 4663], [147, 2500], [85, 14078], [144, 19301], [109, 14914],
         [30, 25453], [152, 28840], [100, 19451], [133, 32119], [144, 1279], [140, 4323], [119, 23041], [84, 29209],
         [32, 36046], [155, 29554], [84, 31258], [47, 40432], [53, 8497], [101, 16076], [11, 34243], [109, 26624],
         [150, 17941], [20, 26935], [18, 8029], [126, 16567], [83, 39988], [48, 8620], [103, 28673], [85, 23702],
         [24, 8292], [81, 13248], [152, 39030], [41, 8862], [115, 27971], [127, 15800], [28, 152], [142, 3724],
         [107, 1022], [126, 35742], [140, 18597], [137, 10402], [100, 31122], [73, 18767], [30, 16807], [98, 34295],
         [83, 13249], [114, 32724], [63, 6990], [6, 331], [11, 16981], [7, 10444], [150, 38112], [109, 18419],
         [110, 11018], [120, 5447], [117, 40937], [119, 13869], [13, 26391], [20, 31753], [86, 31180], [100, 27824],
         [101, 5543], [20, 3587], [26, 20607], [155, 2232], [11, 14251], [108, 15137], [108, 33017], [25, 37940],
         [105, 10199], [130, 21425], [30, 36868], [3, 29032], [118, 6787], [90, 11049], [65, 5968], [24, 23525],
         [104, 9296], [157, 1354], [49, 34965], [92, 33827], [125, 8308], [119, 2339], [144, 7747], [129, 16521],
         [142, 13123], [33, 7904], [106, 17072], [151, 27779], [20, 39191], [28, 10031], [76, 35658], [120, 24552],
         [26, 8889], [15, 17424], [111, 8786], [153, 28208], [96, 10174], [10, 38087]],
        portsCount=158, maxBoxes=331, maxWeight=41548
    ))