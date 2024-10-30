import unittest

"""
综合天赋较高的学徒，对于通用的技能释放速度较快，蓝耗较少
对于不同属性的天赋，玩家根据天赋值不同，选择不同的发展路线，如火系天赋高的，那么火系技能威力增强，升级所需经验/资源更少，
技能带有爆破效果，范围随天赋值增长
冰系天赋高的，冰系技能冻结概率更大，时间更长，升级所需经验/资源更少
也可以增加转职功能，比如玩家将冰系作为主系，在到达50级后，根据自身天赋，选择另一个比如雷系作为副系，到达30级，
这时可以转职为冰雷法师

任务系统可以根据玩家天赋值设置奖励，哪个天赋高设置适合的资源奖励，比如增加火系技能威力的法杖
同时任务内容可以根据属性克制：比如为水系法师安排击杀火系怪物的任务，减小难度，或是相反，增加难度
针对pvp，不同属性的敌人存在克制关系，因此可以提前安排战术，穿上含有抵抗能力的装备，或者追求pvp相对公平，可以增加buff/debuff
比如减少冰系法师控制时间，增加其输出能力；减少属性克制过大的影响，对被克制的一方增加输出，减少承受伤害
同时天赋值高的伤害会更高，同样体现在pvp中
"""


def find_median_talent_index(fire_ability, ice_ability):
    """
    遍历fire_ability, ice_ability，时间复杂度为O(m+n)，空间复杂度为O(m+n)
    """
    f, i = 0, 0
    merged = []
    while f < len(fire_ability) or i < len(ice_ability):
        if f == len(fire_ability):
            merged.append(ice_ability[i])
            i += 1
        elif i == len(ice_ability):
            merged.append(fire_ability[f])
            f += 1
        elif fire_ability[f] < ice_ability[i]:
            merged.append(fire_ability[f])
            f += 1
        else:
            merged.append(ice_ability[i])
            i += 1
    n = len(merged)
    if n % 2:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) /2


class FindMedianTalentIndexTest(unittest.TestCase):
    def test_find_median_talent_index(self):
        test_cases = [
            (([1, 3, 7, 9, 11], [2, 4, 8, 10, 12,   14]), 8),  # 奇数个
            (([1, 2], [3, 4]), 2.5),  # 偶数个
            (([], [1, 2, 3, 4]), 2.5),  # 一个列表为空
            (([1, 2, 3], []), 2),  # 一个列表为空
            (([1, 2, 3], [1, 2, 3]), 2),  # 两个列表包含相同的元素
            (([-5, -3, -1], [-4, -2, 0]), -2.5),  # 包含负数
        ]

        for (fire_ability, ice_ability), expected in test_cases:
            with self.subTest(fire_ability=fire_ability, ice_ability=ice_ability):
                result = find_median_talent_index(fire_ability, ice_ability)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)


