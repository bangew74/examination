import unittest

"""
策略影响：
玩家首先需要确定如何得到最大的能量场，但由于地图是长条形的，如果只得到最大的能量场，导致行走时只有过少的
区域可以享受能量场（举一个比较极端的例子[1, 1, 1, 100, 100, 1, 1, 1]），这种情况就要考虑选择面积最大，还是选择
覆盖更多的x轴，此外建造塔可能要消耗资源，比如[1, 8, 6, 2, 5, 4, 8, 3, 7]，高度越大消耗资源越高，如果想要追求后期
即追求最大面积的能量场，那么前期的作战能力比不了选择面积较小，但是消耗资源少的塔

游戏玩法：
引入不同的塔，比如攻击塔，防御塔，辅助塔，同时每个格子只能有一种塔，每种塔也有不同的功能，比如可以让攻击塔：两个塔离得越远
攻击速度越慢（或者说伤害频率越低），辅助塔：能量场中间有塔，即可增加攻速，暴击率等，使其可以利用高度较低的格子，或是直接对
敌人施加debuff。
可以引入魔法道具，比如提到的增加塔的高度，或增加塔的攻速
引入特色的敌人，比如干扰攻速，免疫某些类型的攻击塔的攻击；对某些防御塔额外造成伤害；免疫debuff，如减速，减防御等
可以给塔升级，减少由于前期错误决策：如能量场面积不够大，导致后期根本没法玩的结果
"""


def max_energy_field(heights):
    """
    算法时间复杂度为O(n)，空间复杂度为1
    """
    l, r = 0, len(heights) - 1
    max_field = 0
    while l < r:
        if heights[l] == 0:
            l += 1
            continue
        if heights[r] == 0:
            r -= 1
            continue
        now_field = (heights[l] + heights[r]) * (r - l) / 2
        max_field = max(max_field, now_field)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return max_field


class MaxEnergyFieldTests(unittest.TestCase):
    def test_max_energy_field(self):
        test_cases = [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 52.5),  # 正常情况
            ([5, 5, 5, 5], 15.0),  # 所有高度相等
            ([1, 1, 1, 100, 100, 1, 1, 1], 202.0),  # 最大的在中间
            ([0, 0, 0, 0], 0)  # 都为0
        ]

        for heights, expected in test_cases:
            with self.subTest(heights=heights):
                result = max_energy_field(heights)
                self.assertAlmostEqual(result, expected, places=2)


def max_energy_field_with_magic(heights, magic_height):
    """
    计算使用魔法道具后的最大能量场强度
    """
    max_filed = 0.0
    # 遍历每个位置，假设在该位置使用魔法道具
    for i in range(len(heights)):
        # 创建一个新的数组，模拟魔法道具增加高度
        new_heights = heights[:]
        new_heights[i] += magic_height
        # 使用原有算法计算最大面积
        max_filed = max(max_filed, max_energy_field(new_heights))

    return max_filed


if __name__ == '__main__':
    unittest.main()


