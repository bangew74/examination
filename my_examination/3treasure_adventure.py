import unittest

"""
策略影响：
玩家需要考虑长期规划，比如为了之后利益较高的，放弃当前价值较高的，或是思考如何使用魔法钥匙，负值宝箱则会增加玩家决策难度
增加游戏趣味性
关卡设计：
可以为某些宝箱增加随机性：30%的概率会获得大量分数，70%的概率失去分数
赠加随机事件：某些事件会使箱子的价值变化（随机增加或减少）；下一次获得的价值翻倍；下一次获得的价值 * -1
每一次通关都会获得魔法钥匙，分数达到某些阈值会获得多个钥匙
增加等级：某些宝箱需要到达特定的等级才能开启

"""


def max_treasure_value(treasures):
    """
    遍历一次数组，算法时间复杂度为O(n)，空间复杂度为O(n)
    针对挑战2有些宝箱可能包含负值，算法会忽略掉负数，见单元测试

    """
    if not treasures:
        return 0
    if len(treasures) <= 2:
        return max(treasures)

    dp = [0] * len(treasures)
    dp[0] = treasures[0]
    dp[1] = max(treasures[0], treasures[1])
    for i in range(2, len(treasures)):
        dp[i] = max(treasures[i] + dp[i - 2], dp[i - 1])

    return dp[len(treasures) - 1]


class MaxTreasureValueTest(unittest.TestCase):
    def test_max_treasure_value(self):
        test_cases = [
            ([3, 1, 5, 2, 4], 12),
            ([2, 9, 2, 4, 1], 13),
            ([0], 0),
            ([10, 10, 10, 10, 10, -10, -2, -41], 30)
        ]
        for treasures, expected in test_cases:
            with self.subTest(treasures=treasures):
                result = max_treasure_value(treasures)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
