import heapq
import unittest


def get_top_scores_heap(scores, m):
    """
    使用小顶堆的方法来获取前m大的元素
    遍历一次数组O(n), 堆操作heapreplace O(log(m))
    排序O(mlog(m))
    最终时间复杂度O(nlog(m))，空间复杂度O(m)
    """
    # 验证输入是否有效
    if not scores or m <= 0:
        return []

    # 如果 m 大于数组长度，返回整个数组按降序排列
    if m >= len(scores):
        return sorted(scores, reverse=True)

    # 构建一个大小为 m 的小顶堆
    min_heap = scores[:m]
    heapq.heapify(min_heap)

    # 遍历剩余的元素，如果元素大于堆顶，则替换堆顶
    # 内部自动维护堆
    for score in scores[m:]:
        if score > min_heap[0]:
            heapq.heapreplace(min_heap, score)

    # 将堆中的元素按降序返回
    return sorted(min_heap, reverse=True)


# 测试类
class LeaderboardSystemHeapTests(unittest.TestCase):
    def test_get_top_scores_heap(self):
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
                result = get_top_scores_heap(scores, m)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
