import collections
from typing import List


# 哈希表
# O(NlogN) O(N)

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # 将每个人的放到一起
        record = collections.defaultdict(list)
        for i in range(len(keyName)):
            name = keyName[i]
            time = float(keyTime[i].replace(":", "."))
            record[name].append(time)

        # 排序每个人的时间线
        for name, times in record.items():
            record[name] = list(sorted(times))

        # 检查每个人是否需要被警告
        ans = set()
        for name, times in record.items():
            now = []
            for time in times:
                now.append(time)
                if len(now) >= 3:
                    old_time = now.pop(0)
                    if 0 <= time - old_time <= 1.00000001:
                        ans.add(name)

        return list(sorted(ans))


if __name__ == "__main__":
    # ["daniel"]
    print(Solution().alertNames(keyName=["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                                keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))

    # ["bob"]
    print(Solution().alertNames(keyName=["alice", "alice", "alice", "bob", "bob", "bob", "bob"],
                                keyTime=["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]))

    # []
    print(Solution().alertNames(keyName=["john", "john", "john"], keyTime=["23:58", "23:59", "00:01"]))

    # ["clare","leslie"]
    print(Solution().alertNames(keyName=["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"],
                                keyTime=["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]))

    # ["b"]
    print(Solution().alertNames(keyName=["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b"],
                                keyTime=["04:48", "23:53", "06:36", "07:45", "12:16", "00:52", "10:59", "17:16",
                                         "00:36", "01:26", "22:42"]))

    # ["ab","bb","da","ea","wa","xa"]
    print(Solution().alertNames(
        keyName=["aa", "aa", "aa", "aa", "aa", "aa", "aa", "aa", "ba", "ba", "ba", "ba", "ba", "ba", "ba", "ba", "ca",
                 "ca", "ca", "ca", "ca", "ca", "ca", "ca", "da", "da", "da", "da", "da", "da", "da", "da", "ea", "ea",
                 "ea", "ea", "ea", "ea", "ea", "ea", "fa", "fa", "fa", "fa", "fa", "fa", "fa", "fa", "ga", "ga", "ga",
                 "ga", "ga", "ga", "ga", "ga", "ha", "ha", "ha", "ha", "ha", "ha", "ha", "ha", "ia", "ia", "ia", "ia",
                 "ia", "ia", "ia", "ia", "ja", "ja", "ja", "ja", "ja", "ja", "ja", "ja", "ka", "ka", "ka", "ka", "ka",
                 "ka", "ka", "ka", "la", "la", "la", "la", "la", "la", "la", "la", "ma", "ma", "ma", "ma", "ma", "ma",
                 "ma", "ma", "na", "na", "na", "na", "na", "na", "na", "na", "oa", "oa", "oa", "oa", "oa", "oa", "oa",
                 "oa", "pa", "pa", "pa", "pa", "pa", "pa", "pa", "pa", "qa", "qa", "qa", "qa", "qa", "qa", "qa", "qa",
                 "ra", "ra", "ra", "ra", "ra", "ra", "ra", "ra", "sa", "sa", "sa", "sa", "sa", "sa", "sa", "sa", "ta",
                 "ta", "ta", "ta", "ta", "ta", "ta", "ta", "ua", "ua", "ua", "ua", "ua", "ua", "ua", "ua", "va", "va",
                 "va", "va", "va", "va", "va", "va", "wa", "wa", "wa", "wa", "wa", "wa", "wa", "wa", "xa", "xa", "xa",
                 "xa", "xa", "xa", "xa", "xa", "ya", "ya", "ya", "ya", "ya", "ya", "ya", "ya", "za", "za", "za", "za",
                 "za", "za", "za", "za", "ab", "ab", "ab", "ab", "ab", "ab", "ab", "ab", "bb", "bb", "bb", "bb", "bb",
                 "bb", "bb", "bb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "db", "db", "db", "db", "db", "db",
                 "db", "db"],
        keyTime=["03:32", "10:12", "15:52", "08:28", "13:20", "21:40", "02:54", "19:02", "21:14", "08:57", "14:36",
                 "02:05", "13:24", "04:27", "21:52", "13:27", "05:58", "07:50", "11:08", "23:44", "14:15", "04:31",
                 "15:30", "21:50", "20:50", "07:27", "21:23", "01:09", "14:50", "05:31", "05:48", "05:09", "11:06",
                 "12:30", "01:32", "09:31", "01:29", "11:13", "08:11", "01:55", "04:46", "03:17", "15:53", "13:22",
                 "14:17", "08:09", "20:52", "12:28", "08:59", "13:21", "07:50", "17:53", "14:33", "06:40", "01:26",
                 "02:05", "10:08", "11:40", "15:42", "12:55", "04:12", "07:23", "00:58", "19:47", "00:05", "19:36",
                 "05:31", "09:31", "09:52", "23:12", "11:18", "22:00", "11:08", "09:21", "11:26", "01:12", "12:48",
                 "10:01", "01:23", "16:31", "14:20", "15:53", "11:41", "14:02", "01:33", "23:16", "05:53", "19:05",
                 "13:51", "06:35", "21:36", "03:32", "06:55", "23:42", "15:27", "12:48", "12:46", "13:31", "20:15",
                 "11:05", "16:05", "06:19", "04:18", "17:44", "06:53", "20:34", "22:25", "12:51", "23:01", "16:32",
                 "21:09", "08:03", "18:39", "07:29", "10:21", "10:23", "05:51", "19:59", "15:14", "06:36", "14:15",
                 "10:21", "15:02", "03:08", "17:36", "00:52", "17:17", "20:16", "15:39", "01:44", "18:52", "03:10",
                 "00:30", "03:02", "00:48", "21:55", "03:12", "22:36", "20:50", "15:54", "18:41", "12:11", "11:03",
                 "01:42", "10:19", "04:32", "01:02", "14:44", "00:44", "18:12", "13:16", "05:33", "05:42", "01:45",
                 "20:45", "20:27", "22:18", "04:37", "16:56", "22:07", "01:05", "22:30", "15:13", "17:07", "04:47",
                 "18:41", "03:59", "06:36", "06:48", "20:51", "11:19", "15:06", "06:51", "17:56", "20:18", "13:28",
                 "00:19", "17:24", "14:45", "14:32", "17:05", "14:54", "02:18", "06:27", "10:10", "12:46", "22:51",
                 "15:20", "10:33", "12:59", "12:49", "08:29", "07:29", "22:48", "13:49", "17:40", "11:19", "22:19",
                 "11:50", "05:33", "12:18", "06:33", "10:56", "08:12", "22:54", "02:33", "10:41", "04:57", "00:37",
                 "01:41", "23:04", "22:31", "00:12", "07:37", "05:16", "22:32", "16:22", "01:40", "20:32", "23:33",
                 "04:53", "03:53", "04:25", "06:42", "20:26", "16:54", "10:22", "11:47", "13:14", "11:19", "01:39",
                 "02:32", "19:40", "02:57", "03:32", "12:32", "07:15", "00:00", "12:31", "23:59"]))
