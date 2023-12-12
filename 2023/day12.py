from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

actual = """
.???#??.?##?#??? 1,1,7
#.???###???#????. 1,5,2,1,1
??.?#??##??.##?##.? 7,5
??????#???????? 7,2
????.##???????????.? 3,10,1,1
?????#????#? 2,1,1,1
?#?.#????.? 1,1,1
????#?.?..????# 3,4
?????????##????? 1,9,1
???##????.#???#? 7,1,3
.?.???#????????? 2,4
?#???#.???.??????. 2,1,1,1,1,4
?..??#????#???#?### 11,3
???#?..?#?#? 3,3
?##???????????#??# 6,2,2,1,2
????.#?.???#??? 1,1,2,3,1
???..?#??? 1,4
?????#?#??#??. 1,3,2
???#???.???#? 2,1,1,2
?#?#?????????????.?. 8,1,1,1,1,1
?????????#???.#.? 3,3,1
???#??.?#.? 3,2
??????.##?# 5,2,1
???????.?? 2,1
?????.??#????? 3,3,2,1
#?#???.?????###?#? 6,3,6
?#????##??#?????#?. 1,12
?#?#?.?#???.? 4,4
.#?????#?####??????? 3,9,2
???#???#?????#??? 1,2,11
.?#?.??.?.?.?. 2,1,1,1
????#.??#?#??.??.?? 5,5,1
?.#?#??##?#? 3,4
?##?.??#??? 3,4
?????????##?#. 4,7
.?.#???.??###???? 1,1,1,6,1
.##??#?????????#? 5,2,1,3
.??#?.??.??. 1,2
.??#????##??? 1,3,2,1
#?????..?#??..?. 1,1,1,4,1
.?#?????#???.? 8,1
.#?.???.???#?#??#.? 2,1,1,7,1,1
?#.???#.??#??#???? 1,1,1,1,8
#??##?.?#? 1,4,1
?.#???.?.?????? 1,3,1,1
?.??#??.??#.?# 5,3,1
??#?###???#? 7,3
???#????????#?. 7,2
.#???????# 1,1,1
.??????????#.??.? 4,1,1,1,1
?#?.??.#.. 3,1,1
#?...??.#?? 2,1,1
???.???.???#? 1,1,1,3
##?#?#?????????.?.#. 2,12,1
.?#?????..???.?? 7,1,1
.#???#??#??.#.???#?? 9,1,5
?#??.????#.????#??# 2,1,3,2,3,1
.?.??#?.??.?##???# 1,2,1,4,1
?.#?????#?#?????? 9,1,1
.?????.#????.??? 1,2,3,1,2
.?????.?#???? 1,4,1
?#?????#????????? 10,1,1,1
.#????????#?. 2,1,4
?????????.??.?? 8,1
????#??#???. 3,1,1,1
.???#.???##.?#?? 3,4,2
.#?.???#?.???#? 1,1,2,1,1
??#?.??##??.#????.?? 3,3,1,1,2,1
..#..??##??.?? 1,4,1
?#?.??#???#?##?##? 1,2,9
????##??.#..??????.. 6,1,2,1,1
?#?????#?????###???? 4,13
?#?##..?#????#?????# 4,1,1,4,2
.?.????????#??? 1,1,5
?.?#???????##?#???.. 2,6
????..?????##.?..?? 3,6,2
..?#???#..? 2,1,1
??????..???????? 3,2,4,1
??#??##.#.??# 1,5,1,2
????.?.???#?. 1,1,1,4
.?##??##???#??? 2,7
?????????? 6,1
.???#?##????#.? 5,3
?#??.??????? 4,2,1
????????#?#? 1,2,6
??#???????.???? 8,2
???#?#?????????.? 3,1,2,2,1
?.???????. 2,1
?.??.#???####??#.. 1,2,2,8
??#?????#.#????. 1,4,1,2
?####????.. 5,2
.???#?.?.#????#? 2,7
.#?###.?#?? 1,3,2
??????#??#???#? 3,2,3,2
.?###?????? 5,3
.#..?????? 1,2,1
???#..?.#???#? 2,1,1,6
??#?#???.? 1,1,1
.?#????##?##? 1,6
#?#?#.?????????#.? 5,3,2,1
.??##?????? 4,2,1
??##??.??. 4,2
??#???????????# 2,1,4,1
???.????#?????? 2,1,1,1,1
.???#??#?.?????. 5,1
.##?.??.?#.# 3,1,1,1
?#?????#?#???##????? 2,11,1,1
..??.#??#??#?#????#? 1,1,7,1,1
???.?##?#??? 1,1,5,1
???#?##???##???????? 2,13,1
..?????##?..##???? 1,2,6
???#??##??#??#?????? 8,3,2
#?#??#.???..??#? 1,4,2,4
??#??.????????#?? 4,2,1,1,1
.#??.????.. 2,2
..?????##??#?#?#???? 7,7
#?#???#??.??.??#?.# 1,5,1,1,4,1
.?#?##???.?.. 5,1
?????.?.#? 2,1
.??.???#??#???##?#?? 1,2,1,7,1,1
?????#.?.?????#??? 1,1,1,1,4,4
???.?..#??.?? 1,3
???????##????#?#?## 2,6,6
?#?????.?? 5,1
??##?.#?..#??? 2,2,1
#.????????#?? 1,5,4
???###??????##???#? 12,2
?.????.??#?????..?. 4,1
????.???.? 1,1
??#..???###??.?#.# 2,1,4,1,1,1
.?????#?????? 8,1,1
??#?##.?.??. 4,1,1
.??????#??#???.?? 6,3,1
??.??.????#??.? 1,2
???????.##????.#.??# 3,2,2,1,1,1
??.??#???.. 1,5
?????????????#???? 2,1,3,1,3,1
#?.??????????#.?? 2,1,2,5,1
?#????#?#.?.??#???? 7,1,1,1,1,1
????.?????.???#???? 2,5,6
??.?????#??.???? 5,1
??#????.##.??????#?. 6,2,7
#..?#???.?.? 1,3
.#??.???.?# 2,3,1
????????#?#?? 1,3,1,2
?##?##????#?#.??? 8,2,1,2
.???#.?.??.????.. 4,1,1,4
.??##??????#???????# 1,2,8,1
.?#..??##?????# 1,1,2,1,1
?.#?.##??????#??? 1,11
.???#?????#? 3,1,3
####?#?#?#??? 8,1,1
.??#?#?..#??. 6,1
###????.???#? 4,5
.?.??####?#???#???. 8,4
.??#???#?####.?? 1,1,7
?.#?.??????#????.? 1,6
??????##??#??.?.???? 11,1,1
?????????#. 4,2
??.???.?#.? 1,1,2
?.??#???#??? 2,3
?..??????.????##? 5,5
.???.???#???#???? 1,10
?..#???.????#? 3,5
?????.?#??????? 1,1,1,1,2
?.?#.?????.? 2,3
.?#?##?.#??? 4,2,1
?#??#??##??.? 1,3,3,1
?#?.?#?..#???.#.???# 2,2,3,1,1,1
???..#????????? 3,1,1,3
???.#.?.?? 1,1,1
.##???#??##.?? 2,6,1
??????#??????#?? 2,1,2,1,5
????.??###?#?#?? 1,8
?#?#.?#????. 2,1,2,2
??#.?#??????????.??? 3,4,1,2,2
?????..??#??.????#? 1,2,1,3,1,3
.????#???#?? 5,4
?..#???.#?#?. 1,2,4
#??????#?.?.???.?? 1,1,2,1,1,2
??#.?#????.?#?. 1,3,2
?##??#??????.#.?.?#? 11,1,1,1
??##????#??. 2,3
#????##??..??? 1,7,1,1
.??????##?. 1,6
.??.???????????. 3,4
?#.#.#??#?.? 1,1,4,1
#.??###??#?.#?.???#? 1,1,6,1,1,1
??##??.?#?.#????.?? 5,1,3,1
.????.#???..? 1,1,4
?.?.#??#?##?#. 1,7,1
????#.#??????.??? 1,1,7,1
.#?????.###?????# 1,3,7,1
??###??#?. 4,3
?????#??.??.??? 1,6,1,3
???.??#??#??? 2,6
.##?..?#??? 2,1,1
.#?#???????? 3,1
???#?#?#.?.??#??.# 7,1,4,1
??????#???.????.???? 1,3,1,4,2
.?#?????#?#?????. 3,1,5,2
?.#?###??#?#?.? 1,10,1
.??.?.#??????##?#?? 1,1,2,1,1,4
????#?.?#. 1,1,1
????#???#???.? 3,3
.??#?.???###???? 3,1,3,1
??...????##? 2,1,5
.??#????.????..?..? 2,1
??##.#.#?.?. 4,1,2,1
???#?###.??.?##??#?? 5,6,1
.?...##?#?????.###? 1,8,3
?#??#?#....?.?#?.??? 6,1,3,1
?.?.??#???#?.. 1,8
?.????#?#??#..#?? 8,1,2
#?#??#?..??.????#? 6,2,1,1
?..#???#?#???#?.?.#? 1,1,5,1,1,1
?.?#????#????#? 1,4,3
?.?????.??? 2,1,1
???????????.???#???? 1,1,2,3,3
?????????###.? 4,5
??????#?#?##??#? 9,5
.???###?.##??.?. 5,3,1
?#??????#.#???#??.? 6,1,1,2,1
???#??..??#????. 6,4
????.??????#??????? 1,1,3,4,1
????????###??????#. 1,2,7,4
##????#?#????#????.# 9,7,1
???#?#?#????#???? 5,6,1
?#????#??#?##???# 6,1,2,1
?????.????????????# 1,2,9
?.#?.?#.#??? 1,2,2
?###?#???????.# 6,3,1
??#???#?.?#????? 4,2,3,3
.?#?#???#. 4,2
.?????.???##????? 2,5
?#?.?????#??? 2,2,4
??#????#??????##??# 10,7
?#?.???????#?#?.??. 2,1,2,5,1
?#?#..???##??#??? 3,10
.?????.?#?.??#??? 1,1,1,6
?????????#?#???.. 1,4,4,2
?...?##?.? 1,3
?#??.???.??# 3,1,2
?#??.???????#???.?? 3,2,7
.??#..?##???#? 2,4,2
.??????#??.????? 3,3,1,2
#????##?#? 3,5
??#?????#??????..?? 2,8,1,2
?????.????? 3,2,1
??.?.##?.?#? 1,2,2
???##??#??##??? 6,1,3,1
#??#???.???.? 1,2,1,1
.?????.?#???? 4,1,1
????????..?#??.?? 3,1,2,1,2
..??#?#.?. 1,1
??#???#?.#? 7,2
????????#?#.??? 2,7,2
?#?..????.. 1,2
???????#?. 1,5
??????.?#??####?. 3,8
?##?#??.?##?#?? 4,7
?????.?.#??? 1,1,3
?#?????.??. 5,1
??.?#??###?. 2,1,5
.?#.?#?.???. 2,2,1
???#.??#????? 1,4,1
?.#??????#.?? 3,1
..?.#??##?#????????. 10,1
..??#?????? 3,1,1
#??.??#???#?#??????? 2,3,5,1
?##.#?.??##?#? 3,2,6
?????#?.????? 1,5,4
?#??????.? 4,2,1
.??#.????? 2,1
?????#???..?? 8,1
?#??????.?#?##??? 3,1,8
????#???..? 2,2
#?#.??#???#???.?#? 1,1,1,6,1,1
????#?????????#???? 1,6,9
????#?####???.?? 3,7,1,1
??????#?#..#??? 1,7,1,1
.???.??#????# 1,8
??????##..?? 5,2,2
.????....###??#???.? 4,8
???..????#???.??# 1,1,3,1,1
??#??????? 5,1
?????.?##????.??#?#? 4,2,1,6
.???#?.?#?????#?? 2,2,2,1,3
?#??#?#?#. 6,1
?????????#????#?.#. 1,1,1,8,1
#?.????.????. 1,2,1,1
?.##??????##. 1,10
????.??#??#?..?# 3,3,3,1
??#.?#???.??? 1,1,1,2
????.#.????##.?.?#?? 1,1,6,1,4
????#???#?#???#?## 1,9,4
??.#??###?. 1,7
#??????????.?????? 3,1,1,1,4,1
.???#.????????##???. 3,11
????????.??? 1,1,1,1
?#?.??.??. 3,1,1
??#..???## 2,2,2
??????.???? 1,1,2
.?????##???.##??? 4,4
?.#?????#??? 2,1
#??##?#???#?#???#?#. 9,5,3
??.???###??.???? 1,7,2
??#????#?.? 2,1
????...?#?????# 1,7
.#?.??####??#.?? 1,8,1
???.#???.#???#..?? 1,3,1,1,1,2
??#?.##?#?##? 1,8
????????.#??????#??# 2,3,11
??.?#??.#??????. 3,5
????#?????.?? 3,3,1,2
.????##???.??#...? 8,1
?#.???????? 1,3,1
???..#?????##???#?? 1,10,1
?????????.?#????? 1,2,2,4,1
##????#?#???#?.#.# 4,2,2,2,1,1
???????.#????.#??##? 1,4,1,1,1,4
?.???#??#??.#. 1,6,1
?#?#???..#?.#??.? 6,1,3
??###?#???.??? 1,8,1
????????..???? 2,2,1,2
.#??#??????#???? 1,6,1,1,1
#.?#...??##???.?##?? 1,1,1,4,3,1
.?###?####????.???? 11,2
?.???.??.???.?? 1,2,2,2,2
?##?#??#??.?.???? 9,2
.?#..?..####.??#? 2,1,4,2
.#???.#??.? 3,2
#????.#????? 2,1,1,3
??#.???.??? 2,2,1
?????????#?# 5,4
??????#?###???????? 14,1,1
????.?#?#? 1,4
..??#????#? 1,6
?.?#????#???#.#?? 4,6,3
.#?#?#?#??.?# 1,1,5,1
#????????#? 1,2,5
??#???.###???#????? 3,7,2
.##?#??????#????.##. 14,2
??????????#..?? 1,7,1,1
??.?#????.? 5,1
????#?..?? 1,2,1
??.??#????? 1,5,1
??##?#??.?#? 8,1
.??..#??.??#?. 2,1,3
???.??????#?#?.?.??. 1,1,1,6,1,2
??.???##??.#????? 1,6,1,1,1
.?????#??# 1,1,1
..??.?#?#???? 1,1,2
??.?????#???. 1,7
??????.???????#.? 3,1,1,5
.???????#? 1,3
?#????.?.?#??.? 4,1,1,1,1
.#??????????#... 4,1,1,2
????.??.?##??#??. 2,8
???#???.???#?..? 5,1,1,1
#??#?#.?????????# 2,3,1,1,4
.#.??#??#?#??#?#. 1,6,6
?????##?#???. 1,6,1
????????.??. 1,1,3,2
????###???.#?#???? 7,6
??#???##?.#?#?.## 1,1,4,3,2
?#?.##???. 1,3,1
???#???????#?#??. 7,3,1
??.?#.?..???????# 2,2,1,5
#.?.#??.?? 1,3
..??#??.?? 3,1
.??#?.???#?#?? 1,8
..?.?.???.???? 3,1
???#?##?#?#?.?#???? 10,2
??..?#..??#?? 1,4
????.?.??..##??##??? 2,1,1,9
??##?????.????#?.?? 6,5,2
???#????????#.?#.?# 1,10,1,1
????.?###?? 1,4
.#?.?????? 1,2
?..?.???#?#?#?#? 1,9
????.?#???????. 4,1,1,2
????#?##?.???? 8,2
?????.#??? 1,1,1
.???#?.#??.? 1,3,3,1
#?##??#?.?#?.???? 4,2,2,1
.?#???.??? 1,2,1
???????#?# 2,2,1
?#??.???#???????#.? 3,4,1
.????#????????#???? 8,3
#??#?##.?. 2,4,1
????.?????##?? 1,1,2,4
?????#?#?.????##???? 2,5,1,3,2
???????#???##?.#?? 1,10,1,1
.?.???????#???#???? 1,1,1,1,1,5
????##???#..??.#??#? 1,6,1,2,1,2
?#????????????#?? 6,3,4
.?.?#?????. 1,3,2
.????#?????? 1,3,1,1
??.####???##?????? 11,1
??????#....???#????? 2,5
?#.#.#?#?#??#?#?. 2,1,11
?.#????#.#?#?. 2,2,4
#??#??.##?#?##?????. 2,1,1,4,4,2
???????????.??# 1,1,2,1,2
???.?#???#?#????#?.# 3,4,1,2,2,1
#?#?.?????????? 4,1,3,3
?????#???? 2,1,2
?#?.#.?#??#??#.? 2,1,8
?###??..????#?? 6,5,1
..?##???????# 6,1,1
?#???????.??#???? 1,3,4,1
.????.???????? 1,7
.?????.????#.??? 3,1
#.???##?#??# 1,9
.????#?.#????.?? 2,2,1,3,1
?##?????#??? 4,3,2
?#????.?#?? 2,2
??#.?????????.##??? 1,1,1,2,1,5
.???#???###?##?##??? 16,2
????#.???#???? 2,6
.??##?##?#?. 1,2,2,2
??????..#??#####??? 2,8
#.????..??#????. 1,1,1,7
?##???#?.?#??#.? 5,2,1,1,1
?##?#?#..????..?. 6,4,1
?????#??#. 1,6
#???.##??? 2,3,1
?#??????#???????? 1,5,1,1,1
?#?#?.??##??#.??.??? 5,4,2,1,2
??#?????????..???##. 10,5
???.??##??????##?## 1,13
#??#.??#.#?#??#.#?# 4,2,6,1,1
??.??#?????? 1,5
???##??????.? 6,2
??.???.??. 1,2,1
.?????#???? 5,1
??.??.??????. 1,3,2
??##.?.????? 3,3
.?#??#??#??.???. 5,2,1,1
?#.##?????.?.?? 1,2,2,1,1
??.##????????..??#?? 5,3
?.??????#.#? 3,1,1
.?#???.?#??#?##.?. 4,4,2
??????#?..???. 4,1,2
?.???#???#? 1,5,2
?#????#??????#????? 2,3,5,1
????#?.??#?? 1,1,3
??###??????## 4,1,4
##??#????..##??? 2,1,2,4
????.????..? 2,1
#????.??????.??? 2,1,4,1,1
???????##?.? 1,3
?.#??##.?.#.##?.?.?? 1,1,3,1,3,1
?#.??.??????#???.??# 1,1,2,5,3
.#????#?????.???? 1,1,2,3,2
????..#??#????#? 1,6,2
.##?????#??#??##?? 4,2,6
?#????.??.?#?#?.??? 5,2,5,3
????????????#?? 2,1,1,1,3
.??.??#?????#? 1,2,5
??.#??.?#?????? 2,7
???##?????####???.?. 1,2,9,1
.???.#?.???#???# 2,6
?.????##????. 1,7
???#?#?.?.?#?????.? 4,5
?.?.?#.????? 1,2,1,1
??.???#?..#? 2,2,1
#?#.#??#?..?.????? 1,1,5,1,1,2
???#?.??.?#.?# 2,2,1,1
?.??#?.????.?? 1,2,2,1
???##?.???#?? 1,2,5
???.???????.. 1,5
#??#????#????????# 1,3,2,2,1,1
.????#??#? 1,5
?#????.#?# 4,3
?.??????.?.?#??.?#?. 5,2,2
.#??????#????# 1,1,4,1
???#???#??????#??.? 2,10
#?.?#?.???????#?.?? 1,2,5,3
?#.??.#???##??#.#..# 1,1,1,5,1,1
???#.??#?. 1,3
.????#?#?###?#?#. 13,1
??.##??.?#???.???. 4,3,2
?#?#.##?.????#?#? 3,3,2,1,1
??##???#?#?##.??. 11,1
?????#?#???#???.? 2,1,4,1,2
.#?.##???????##. 2,2,2,3
?#??????###?? 2,5
.??#???##???.???#.?? 8,1,4,1
.??#????.??#???. 1,3,4
?#????.?.????#?.?? 1,1,1,2,2,1
?..##?#...??.##?. 1,2,1,1,3
#?????##???#?????#?? 3,7,3,2
.???##?????#???#.??? 4,1,1
??..???#?????#????.? 1,13
??##?????#????.?? 1,12,1
.?.?#.?#????. 2,3,1
??.???#??????? 1,10
???#??.??##?? 3,2
?#??#?????.??????? 8,4,1
?.#???#????#???????? 11,5
#?######.??????? 1,6,1,1,1
??????.?#?#?. 1,2,4
???..??#?#.. 3,4
?.??.??.#???##???# 1,1,1,10
??#????.##???##?#.? 6,4,4
??????.???? 6,2
??..#??.??# 2,2,1
.?????????.#?? 6,1
##?..???#?#???? 2,8
?...???#?? 1,1
?.?#?.????????? 3,6
#???#.##????#?#.#??? 1,1,1,9,1,1
.???..#??#??#?#? 2,10
#???#?.??.??.?##?#?? 2,3,2,1,2,1
?#.?????????#???? 1,3,1,6
?#?.???????# 2,7
???.#????#????##?### 1,1,1,1,3,7
??.?????????? 4,2
?????.????#?##????? 1,1,13
#???.????. 1,1,1
???##????.? 4,1
?????#?????.??#? 1,7,1,1
.????##.?#????? 1,4,3,1
.?.?#?##????????? 5,1
??#?.###?#?# 2,7
???#???#??#. 1,1,6
????##?#??????.?#? 10,1,2
.?#??????##?.. 2,6
.??#?#???#? 3,1,1
.?#?????????.#?#???? 1,1,1,1,7
??????.?????.?????? 1,4,1,2,3,1
.?.#?????.? 1,6
????#???.????..??? 1,5,1,1,2
.?...?#??.#?.?? 1,3,1,2
???#?#????#?????.?? 3,6,3,1
??.?????.?? 1,4,1
#??????#???#?????? 1,1,10,1
?????????? 3,3
??????????# 1,6
????????.????#? 3,1,1,1,2
.???#?????.?#.??? 4,3,2,1,1
????##?#????#?? 1,12
???.#?????????# 2,6,1,1
??#?????##.????#??.. 4,2,6
?.???##..??#.? 1,1,2,3
#?..????##??????? 2,11
?????#??.??.? 5,2,1
.?.?????????#??. 1,1,1,4
????.????..?.? 2,1,1,1
#?.?.?????# 1,1,3
?.???##?#?.?.? 1,1,6,1
?#???????????..???#? 5,2,1,1,1,3
#????.???# 2,1,3
#????#?#????? 8,1
??.?#..#?..##. 1,2,1,2
??#.?.?.??#?#???##? 1,1,1,7,3
??#?.#.???#.??# 4,1,2,1,2
?##????##?#?#? 3,6,1
???#.???#???## 1,1,4,3
.??#?????###???.? 2,1,6
??????.??? 1,2,1
?#??#?#?##??#? 9,2
?.#?????????.????. 1,1,8,3
.?#?.?#???#???#?##?? 1,14
???????#???#?.?#??#? 1,6,2,4
?.??#?.????#?. 1,2,6
??????.##?.#.??#??.? 1,1,1,2,1,4
???#.???#?#.?#???.# 4,1,4,4,1
??..?????#??? 1,3,3
.?????..????#??????? 2,1,8,2
.?##??#?.??#? 3,1,2
??.????????.??#??? 1,7,4
????#?.#??#? 2,3,2,1
#????##?#????#?..?? 7,3,3,1
???##?#??.????.#?? 8,1,1,3
??...??????#?. 1,3,3
?#.?????????..??#? 1,6,4
.#???#??????#?????.# 1,1,1,6,4,1
.??##??????# 6,2
#.?????.?# 1,5,1
?#?.#???#?. 2,1,1
?.??????#????#.#?? 1,4,1,1,1,3
#?.####??? 1,7
??.#.???#?????#???? 1,1,2,2,3,1
??#?????#??##?##.?? 2,11,1
?#???????.#?#??? 6,4,1
???.#..?..#?? 3,1,1,2
.???#?????.?#????# 1,2,1,1,5,1
?#.?#?#?##??.???? 2,8,1,1
????#.??#???#?#?# 1,3,2,5
?.??.??##????##?? 1,10
#.??#???????????.??? 1,3,4,2,1
???????.???.?#???#? 1,2,1,3,7
??.##??.????#??#???? 3,10
.?#??#?#?#???.????. 2,7,2,1
??#?#?.??#?##?.?# 1,1,1,6,2
??#?????#??#???#. 3,11
?#?#??#?????#???## 1,1,4,3,3
?###?#????##??#??? 13,2
?###?.??##??##.? 3,8
?????????????# 7,2
?????#?###????? 4,6
?..???????? 1,1
#?????..??#.?. 2,1,2,1
???.##??#? 2,3,1
#??#?##?#??#??#.?.? 2,6,1,2,1,1
??????#??###?? 4,4
????#?.????? 5,1
?#????#????#????? 3,5,6
????#.???? 4,4
??????..?##??.?. 3,2
?##???.#?#?.#.?? 3,1,1,1,1
?#?###?#...? 2,5
..#??????? 4,1
?.?????##?#?????#??? 1,10,6
#.???#?.##? 1,4,3
????.?##?.????##?. 2,3,6
???.#?#??##?##????.. 1,10,2
.?????#????????????? 9,7
?#.??#?.?? 1,3,1
?.?..??????.?.???? 6,4
??#.?#???.#?.?# 1,1,5,1,2
?..#????????????#?? 1,2,11
???#?????????#??#?? 5,10
????????#?.???#?#? 2,4,1,1,1
?#?????????#?.? 4,2,3,1
.?#.??????#?? 2,2,2
??.??#??#?????#.?. 7,2
.??????????#.??.???# 6,4,1,1,1
?#?#???#?#??.??# 9,1,1,1
??#????.?.?#??.??#?? 3,2,3,4
???##.??????# 4,1,1,2
????#??#?#???.#?.??? 1,1,5,1,1,1
???#?#??#?.?????? 9,1,1
??????#???? 4,1,3
.?#?????#??.?.??#?# 3,1,3,4
#?.??#?..? 1,3
?.?##??????.?.????. 4,3,2
.??.????.???# 1,2,1,1
???.??#???##?????? 2,7,2
????????..????????? 4,3,4,1,1
?#??#?#.?.?.?. 1,3,1,1
??#?#???????.??? 1,3,5,2
???.?.??????#??? 3,1,1,5,1
??????????#.# 1,1,6,1
?.????????????? 9,1
#?#???.#?.????#???? 6,1,1,3,1
?#??#?????? 5,1,1
??#?#??????????#? 1,3,1,3,2
?.?#?#???#?.? 1,5,2,1
?..?..#??? 1,1,3
???#.?????.?.?? 4,2,1,1
?.??????.?? 2,1,1
??.??#..#?# 1,1,3
????#??.####???.?.?. 3,6,1
?#????##?#? 3,1,4
?.??##?????????? 6,4
??##??..#?.?#??.? 3,1,2,4
??#?.????? 2,1
???????.#? 3,2,1
??#??.????#?..#??? 2,1,1,2,1,1
..??????.?????..? 6,1,1,1
.???##?#?#???##??.?? 8,3
#??????#??##?##?#??? 2,2,8,4
#.?#??#??????.?.#??. 1,7,1,1,1
#??#?#??????.??#? 4,1,1,1,4
??.?#???#????.. 1,6,1
?.??.????#????? 1,1,1,1,6
##?????.?.#??##????? 4,1,1,5,1
???###???????? 4,1,1
.?#??????#??#?#?. 3,1,3,4
#.??#??#????####??.? 1,1,1,1,8
?#???.??#?????#. 1,1,5,1,1
?#???????#???.? 2,2,2,1
????????#?##?. 3,5
?.?.?.#??..# 1,1,3,1
###..??????..??? 3,1,2
??????.###??.?? 2,2,4,2
.???????#?#???#? 3,10
.????#?#.#..?? 7,1
?.???????#??#. 1,1,3,1
?.?##?.?????????#?? 3,12
.#??#.?????? 1,2,3,2
?????##??##???# 2,4,2,1,1
###??#??.???.?#????. 8,2,5
?????##?#??.? 1,3,3,1
?##??##?.#??? 8,1,1
#?#.??#??????#??.?? 3,6,2,1
?#???#?#??????????? 11,2,1
...????????????.? 3,2,2
.????#??.???.?.# 2,2,1,1,1
.??#???#????..?##?? 2,6,4
???##???.???? 5,1,1
#?##?#.?.#?.?. 6,1,2,1
.????#.#.?#?#?.#? 5,1,3,1
??#???.??#??#??.??? 2,1,7,1,1
##?.#.??????#? 3,1,3,2
??#?????#???.? 3,1,2,1
#.???..#?.???.? 1,2,2,1,1
.??????#???.. 4,3
????.???????#??#???? 1,1,1,1,5,1
#.#???#????????? 1,1,1,8
????#.?.??? 4,1
???????.?..????#?? 1,5
??????.????#?###? 3,8
???#.?.??##???#???? 1,10
???#????#???????.? 1,12
?????#?#?##. 1,1,6
??#?#?.??.??#??#?#? 4,1,7
??#.#??????#????# 1,2,4,1,1
?#??#???????.#????. 4,4,2
?#?.???#.? 1,2,1
?#???#??..?.? 2,2
????.??#???#???????? 2,4,1,2,1
??..?##???#?.#?? 7,1
?.??.?.##?#??#?#??# 1,1,1,7,2,1
?#?#.??????. 2,1,2,1
.?#????.#????..?? 3,2,3,1,1
.????..#??##? 1,1,1,2
???.??#??????????? 3,3,5
?#?#.?..#??#????? 3,1,5,2
.?????#???????#? 7,3,1
#??.???#???????.?? 1,1,4,4,1
??.??..???. 2,1,1
.#???.##.?#?? 4,2,4
??..#??#??? 1,4
??????#???? 1,1,5
??#..???.? 1,1,1
?##?#???..#..#??#?# 2,1,2,1,1,4
??#.?.####?#? 3,4,1
.?#.?#?.#.###??# 1,1,1,3,2
.????#??#.#?? 2,1,1,1
#?#???#?.#?????#? 1,6,1,2,1
????..??????... 4,1,2
???#????.???# 4,2
#####????? 7,1
##.?.?.?#?????? 2,4
????.???.#?#???#?? 1,1,1,7,1
.?#??????.???#??? 4,1,2,1,1
?#??##?#?.##??????#? 1,4,5,1
.????.?#????? 3,4,1
?#.#??#????.###..? 1,6,1,3,1
???.##???. 1,4
..?#????.. 1,1
..??.?.???????? 1,1
???.???#?#?.?#?...#? 6,2,1
?????##?#?????#? 5,1,4
?#??????????# 1,7
???.???????????????? 6,4
?#???#??.???.?. 3,1,1,1,1
??????..?#.#?# 2,2,2,3
..??..?#????. 2,3,2
?.?#????...???? 1,2,1,1,3
???.#??#.?.#?#?. 2,1,4
?????.#???????? 3,9
#?###?#????????# 8,1,4
???????.?# 1,1,1
???##?.?#??#????? 5,6,1
?.?#??.???.#? 1,1,3,1
??.?..??????? 1,6
??#??????#??? 2,9
.????.###??#. 1,1,6
??.??##?##???. 2,7,1
???##????#??#????.? 16,1
???#?###??#???? 1,1,4,2,1
.???.##?.??. 3,3,1
??????.??? 1,1,2
?????##??? 1,5,1
?##?#????.?#?#.. 2,3,4
.???..#???.?? 2,1,1,1
???????#?? 3,4
?.?#??????? 3,1
????.??#.#????. 1,2,1,1
??##?#????# 6,1,1
.#?#??..?.?? 5,1
???##?.?###? 5,3
????..#.???????..?? 1,1,1,5,1
??.??????????#. 1,9,1
##?##??.?#??? 7,1
.?.#???#??#?????.# 1,1,10,1
.????..???. 4,3
##??.?#???.? 2,4
..#?##???? 1,4
?.?#???#?#.? 2,1,3,1
?????????.????? 8,2,1
?#??#?.?#?????????? 1,1,2,7
#?????#?#??.#??? 3,1,1,1,1
??#???#??##?.?? 8,2,1
?.?#??????#??.?## 9,3
.?#????.??.? 1,1,1
?????.?.?#. 5,2
.???.?????# 1,5
????..????. 1,1
????#?.?.#??.??#? 2,1,1,1,3
???.???#???#???#??? 1,4,3,4
.??##????. 3,2
?#?#??????.?? 3,1,1,1
?.?##??.??#?##.? 4,6
???????.#?#?##???? 4,1,1,6,1
?..?????.#.?#?? 1,1,1,1,3
#??#???.?#????? 6,2,1,2
.????#..??# 1,2,3
.????????? 5,1
??????.????# 1,2,1,3
??.###??????.??#? 1,5,1,1,2
.????????#?? 1,3,1
#???#??####?##????? 1,1,8,2
.??#??????##???#? 3,4,2
??...#???.##??#????? 2,4,2,4,1
#?.#??#???. 1,2,1
#.??##??????##? 1,5,2,3
????.#.?#.#? 2,1,1,1
???????????#??????#. 8,8
#???????#??#.???. 4,1,4,3
.?#?#?.##??????.? 4,5
.???#.??...#? 1,1,2,2
?.??#.?.#? 3,1
???.?????#???..???? 1,1,7,3
..?.?#???. 1,2
??.##?#.?. 1,4
??.#?#?#??# 5,1
#????#???#?#?.#??? 2,3,1,2,1,1
?????#???#??????.? 1,1,9,1,1
.????????????#? 1,1,1,3
???????#??#???#?#?? 2,1,4,6
??.???.????#?? 2,1,1,3
.??##????#??. 4,1,1
????#??.?#???. 1,1,2,4
???##???.?? 5,1
?????#.??#???##??? 3,1,9
??.#.???.? 1,1,2
????.????#??? 1,1,1,3
?#??#??????.??##..#? 2,1,1,1,3,2
???.???????#..???#.. 8,1
??#??????????#???..? 1,1,2,1,5,1
?.#?##???#?#? 1,4,3,1
?#.?????##????? 1,7,1
?.#????#?? 1,1,2
####?..??###?##????? 4,12
?.???##????????? 5,5
??#???##??.??.?###?? 9,1,5
.??#???#???#????# 4,5,4
???????#?#??????#.?? 3,10,1
?????..#?#???. 2,1,4
?.????.???#?#?? 2,4
?.##??.#?#? 3,3
#.?#??????. 1,6
????##??#.?????#??.? 1,3,1,1,6,1
??.????#??.??#??. 1,1,4,2,1
#??.#?##?####?.?? 1,1,10,1
.??##??#??. 5,1
???.??.?#????.??? 2,1,5,1
???.???.?#???###.?? 1,8
???#??#?.??.#???.. 5,4
..?#?????? 5,1
???#?#.????. 4,2,1
??#?????#?#??..? 3,5
???#?#??..??? 1,2,3
?????.???..? 4,3
?#????????#?.???.#?? 12,1,1,2
??#???..#??????? 1,1,2,1,5
#????????.?.?????.#? 1,4,2,1,1,1
??###?#????..?? 11,1
?#????#..??.? 2,2,2,1
???##??#?#??.??.#.# 10,2,1,1
#??????????.???? 1,5,1,3
??.???#??????.?? 1,3,3,1
???.#?..?????###? 1,1,8
?##????##???#??..#? 9,2,1
.???#?##???#????#? 12,2
..#????.?? 2,2,1
.?#??..#?#??#????#?. 4,1,7,2
?.?????##?? 2,3
??????..???????##?## 2,1,1,1,6
#?##?..?.?#?.??????? 5,2
?#???#???#? 6,1
??.#?.?.?#?? 1,1,2,1
.?#??.??.????.?#?.? 3,1,1,2,2,1
??#???.?####?##? 1,1,1,9
??????.?????#.? 2,6
?.#??#????# 1,1,6
??#???????????? 1,4
?#????#..??##??? 6,5
?#?.?##????? 2,4,2
#?#?????..????#??? 3,2,6
?????#?#?.???#??# 1,6,4,1
??##??.???.. 5,2
##?#??###?#? 2,6,1
?#?.??#?##??#???.# 2,1,10,1
?#.???.###? 1,3
.?#??.#??????? 4,1,4
#?#??##?.??#?????? 8,1,2,3
??#.??????? 1,4,2
.???#?#??????##?? 1,3,7
????#?????#?#???..?? 1,12,1
??##?#????#?#?#?#??# 7,10
?.????#????#??#?.?#? 1,3,6,3
..#?.?????. 1,1,1
#?????#??#?#?# 3,1,2,3
.##?#??????.?..??#.. 10,3
??.?##?.?.?.?????#? 1,4,1,2,3
?.????##?###??????? 1,12
??#..????.??? 1,1,2
#??#???#????#??.?#? 2,11,2
??#?.?##??????##?? 4,5,1,4
?#??#??#???.??.??.? 1,2,3,1,1,1
???..#?#???? 1,3
??.#?##?#?. 1,6
??##??????????? 4,1,4
????..?#?. 1,2
?????.?.#.??##?# 1,1,1,1,4
.?#?##?##???????? 11,1
?#.?.?????. 1,2
##?#?????.? 5,2,1
?.??????..#?.??#???? 1,4,1,1,1,3
##??#??#???.?.? 8,1,1
?????#?????.???#.? 6,3
?#??.????? 2,2
???.#?#?#???? 2,1,5,1
??.?.#?#??? 1,3
????#?..??????.?. 4,6
?#?..??????.? 2,1,1,1
??..###?????.??? 2,6,1,1
??????????###????.?? 8,4,1,1
??#?.?.#.????. 4,1,1,3
????##???#?????##?? 10,3
.?..#??#?.#????? 1,4,1,2,1
?#..?#?????#? 2,4,2
?????.#?#.?##. 2,1,1,3
???.?#?#.??? 1,1,1,1
?.#??..?.????. 1,1
??#?.???#?##?????? 2,9,1
?#?.???..??#??.???? 3,3,1,3,2
?##?#?#?????.#??#. 3,6,1,1,1
????##??.#? 5,1
.?????.???##??#?.??. 1,1,1,1,6,1
.???#????.....??#??? 4,2,4
?.??#???????.??? 2,1
?.#??#?..#???#?.?? 1,1,2,5,2
.???##????????##?#? 1,15
.#?.??.??. 1,1,1
?????#???.?????#??# 2,4,1,7
???#??#??#.???#.??. 4,4,4,1
??.??.#????.??. 1,1,1,2,1
#?.??.?.???.??? 2,1,1,3,2
#?.???#??.??????? 1,6,2,1,1
.??#?.??????## 2,8
???###...????. 5,3
??#.??#?####??#?#. 1,13
.????#???#????? 1,2,2,3
?????##??.????.?.? 3,5,1,1,1,1
?..??.??.??.? 1,1,1,1
.?#??????. 1,2,1
?#??????????????? 2,3,4,1
##???.?.#.? 5,1
??#.????.???????? 2,1,1,7
?????#.??#??#????# 4,1,6,1,1
????#?.??? 1,1,1
??#??.??#?. 3,4
.?.?.#?.?#?#?#?? 1,1,8
????.????#??????? 1,10
??#??????#??#?. 4,8
????#?????#??#?#? 3,8
???.???#?????? 1,1,6
.??.??.???. 1,3
#??#?.#???##??? 1,2,7,1
?#?.##?????### 3,2,6
.#?.?##?.#?? 1,4,1,1
.???#?##?..?.?#?. 5,1
?????.???#??#?? 3,6
??#???##???#????# 3,9,2
?????#???#?.??????? 1,1,3,2,3,3
???#?????#?.?#? 3,1,2,3
.???.???### 3,5
???...????#?# 1,1,5,1
????#?#??.??####?? 5,7
??..??#?????#?##? 1,1,1,1,4
??????#??? 3,1
?###??????? 6,2
##?????##?????#??. 3,4,1,3,1
???????#??.????####? 1,1,1,1,1,6
.###.?????? 3,1
??.#.?????###?##? 1,1,12
?#??..?????#?#??#? 1,11
?..??????#. 1,1,2
??.###???.?.##?.#?#? 1,3,1,1,2,4
.??#???#??? 3,2
.?????#?.??? 1,1,1,3
????.???????###????? 2,1,10,3
??.??#?###? 1,7
??#?????.???. 1,5,2
#?.??..???.??? 2,1,1,3
..?.????#??#? 1,1,5
#??#????.#???.# 5,2,1,1,1
.#.#???#??? 1,1,5
..?#???#???.?#???#? 9,6
?#?????.?.?#????##.? 1,2,1,1,2,4
???#?.?#?#.?#???#..? 4,4,5,1
"""


def solve1(inp):
    inp = inp.strip().split('\n')
    total = 0
    for line in inp:
        parts = line.split(" ")
        counts = [int(i) for i in parts[1].split(',')]
        springs = parts[0]
        result = count_arrangements(springs, counts)
        total += result
    return total


def count_arrangements(springs, counts):
    total_springs = sum(counts)
    filled = sum(1 for c in springs if c == '#')
    left = total_springs - filled
    if left == 0:
        return 1
    # otherwise, attempt to fill in various combinations
    questions = []
    for i, c in enumerate(springs):
        if c == '?':
            questions.append(i)

    attempts = combinations(questions, left)
    cnt = 0
    for a in attempts:
        s = [c for c in springs]
        for i, c in enumerate(s):
            if c == '?':
                char = '#' if i in a else '.'
                s[i] = char
        if valid(''.join(s), counts):
            cnt += 1
    return cnt


def valid(springs, counts):
    px = [s.strip('.') for s in springs.split('.')]
    parts = [x for x in px if x != '']
    if len(parts) != len(counts):
        return False
    for p, c in zip(parts, counts):
        if len(p) != c:
            return False
    return True


def solve2(inp):
    inp = inp.strip().split('\n')
    total = 0
    for line in inp:
        parts = line.split(" ")
        counts = tuple([int(i) for i in parts[1].split(',')])

        springs = parts[0]
        actual_parts = '?'.join(springs for x in range(5))
        actual_counts = []
        for i in range(5):
            actual_counts.extend(counts)
        result = valid_arrangements(actual_parts, tuple(actual_counts))
        total += result
    return total


@cache
def valid_arrangements(springs, counts):
    min_len_springs = sum(counts) + len(counts) - 1
    if len(springs) == 0:
        return 1 if len(counts) == 0 else 0

    min_len_springs = sum(counts) + len(counts) - 1
    if len(springs) < min_len_springs:
        return 0

    first = springs[0]
    if first == '?':
        # Branch between the two possibilities
        return valid_arrangements('.' + springs[1:], counts) + valid_arrangements('#' + springs[1:], counts)
    if first == '.':
        return valid_arrangements(springs[1:], counts)
    if first == '#':
        if len(counts) == 0:
            return 0
        first_length = counts[0]
        if len(springs) < first_length:
            return 0
        if '.' in springs[:first_length]:
            return 0
        # Need to special case this otherwise the end condition doesn't work
        if len(counts) == 1:
            return valid_arrangements(springs[first_length:], counts[1:])
        else:
            # Match is too long
            if springs[counts[0]] == '#':
                return 0
            return valid_arrangements(springs[first_length+1:], counts[1:])



if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

