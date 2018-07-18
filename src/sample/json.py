import collections as cl #collectionsをインポート

#ys = {}
#{}の代わりに，collections.OrderedDict()で初期化する
ys = cl.OrderedDict()

ys["honoka"] = cl.OrderedDict({"B": 78, "W": 58, "H": 82})
ys["eri"]    = cl.OrderedDict({"B": 88, "W": 60, "H": 84})
ys["kotori"] = cl.OrderedDict({"B": 80, "W": 58, "H": 80})
ys["umi"]    = cl.OrderedDict({"B": 76, "W": 58, "H": 80})
ys["rin"]    = cl.OrderedDict({"B": 75, "W": 59, "H": 80})
ys["maki"]   = cl.OrderedDict({"B": 78, "W": 56, "H": 83})
ys["nozomi"] = cl.OrderedDict({"B": 90, "W": 60, "H": 82})
ys["hanayo"] = cl.OrderedDict({"B": 82, "W": 60, "H": 83})
ys["niko"]   = cl.OrderedDict({"B": 74, "W": 57, "H": 79})



print(ys)
#出力：OrderedDict([('honoka', OrderedDict([('B', 78), ('H', 82), ('W', 58)])), ('eri', OrderedDict([('B', 88), ('H', 84), ('W', 60)])), ('kotori', OrderedDict([('B', 80), ('H', 80), ('W', 58)])), ('umi', OrderedDict([('B', 76), ('H', 80), ('W', 58)])), ('rin', OrderedDict([('B', 75), ('H', 80), ('W', 59)])), ('maki', OrderedDict([('B', 78), ('H', 83), ('W', 56)])), ('nozomi', OrderedDict([('B', 90), ('H', 82), ('W', 60)])), ('hanayo', OrderedDict([('B', 82), ('H', 83), ('W', 60)])), ('niko', OrderedDict([('B', 74), ('H', 79), ('W', 57)]))])