import pyprosail

res = pyprosail.run(1.5, 40, 8, 0, 0.01, 0.009, 1, 3, 0.01, 30, 0, 10, 0, pyprosail.Planophile)

# import matplotlib.pyplot as plt
#
# wvl = [x for x in range(400, 2501)]
# plt.plot(wvl, res)
# plt.show()