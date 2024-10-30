import unittest


def get_top_scores(scores, m):
    """
    使用内置的sorted函数，算法时间复杂度为O(nlog(n))空间复杂度为n
    """
    # 验证输入是否有效
    if not scores or m <= 0:
        return []

    sorted_scores = sorted(scores, reverse=True)
    top_m_scores = sorted_scores[:m]

    return top_m_scores


# 测试类
class LeaderboardSystemTests(unittest.TestCase):
    def test_get_top_scores(self):
        # 测试数据点
        test_cases = [
            ([120, 85, 230, 45, 77, 320, 65], 3, [320, 230, 120]),  # 正常情况
            ([], 3, []),  # 空数组
            ([120, 85, 230, 45, 77, 320, 65], 7, [320, 230, 120, 85, 77, 65, 45]),  # m等于数组长度
            ([120, 85, 230, 45, 77, 320, 65], 18, [320, 230, 120, 85, 77, 65, 45]),  # m大于数组长度
            ([120, 85, 230, 45, 77, 320, 65], 0, []),  # m为0
            ([120, 85, 230, 45, 77, 320, 65], -1, [])  # m为负数
        ]

        for scores, m, expected in test_cases:
            with self.subTest(scores=scores, m=m):
                result = get_top_scores(scores, m)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
