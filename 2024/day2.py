from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

actual = r"""
65 68 71 72 71
31 34 36 37 37
80 83 84 86 87 90 92 96
30 33 36 39 45
21 22 25 23 24
66 68 69 71 72 71 72 69
2 3 5 4 4
77 78 77 79 82 83 86 90
6 9 10 7 9 12 17
25 27 28 28 30 32
61 63 66 68 68 66
51 54 54 57 60 60
50 52 52 53 56 60
73 75 76 76 83
19 20 24 26 28
36 38 41 42 45 49 47
56 59 63 64 64
26 29 32 36 40
70 72 74 75 77 80 84 89
81 83 88 89 92 95 96
79 80 85 87 89 92 93 90
77 80 85 87 89 92 92
29 31 33 38 40 42 46
49 52 57 58 59 65
14 11 14 17 18 19
43 40 41 44 47 50 51 50
31 30 32 35 35
43 40 42 43 46 49 51 55
9 7 9 12 15 17 18 23
74 71 74 71 73 76 79 80
50 49 50 49 52 50
51 48 51 49 49
23 22 23 25 22 26
45 43 44 47 45 50
42 39 41 43 43 45 48
97 94 96 98 98 99 97
48 47 50 51 54 55 55 55
33 30 31 31 33 37
17 14 17 19 19 24
41 40 41 43 45 47 51 52
65 62 64 67 71 70
77 76 80 81 84 85 86 86
18 16 20 22 26
58 56 59 63 64 65 67 72
18 17 22 24 26
27 25 28 29 30 36 39 36
53 52 58 60 60
41 40 45 47 49 53
49 46 47 49 50 57 60 66
43 43 44 45 47 50 53 56
79 79 80 81 83 84 81
68 68 70 71 71
15 15 17 18 19 20 21 25
58 58 59 62 64 66 71
67 67 70 72 73 71 72 75
83 83 81 83 80
93 93 95 97 94 94
5 5 8 7 9 11 15
8 8 11 8 15
59 59 62 62 65
9 9 10 10 13 16 15
72 72 75 76 76 79 79
6 6 6 7 9 13
27 27 29 29 35
40 40 44 47 49 52
85 85 87 88 90 94 92
55 55 59 60 60
36 36 40 41 42 46
62 62 66 68 70 75
44 44 45 46 47 52 55
85 85 88 95 93
33 33 35 36 39 44 44
18 18 19 21 28 29 31 35
58 58 60 62 69 74
15 19 22 23 25 27
20 24 27 28 29 30 29
44 48 49 52 54 57 57
41 45 48 50 54
8 12 15 17 20 27
48 52 51 53 55
78 82 81 84 83
8 12 9 12 15 18 18
56 60 63 61 62 66
2 6 8 7 10 13 20
8 12 12 14 17 18
52 56 58 59 59 57
73 77 79 82 82 83 83
58 62 63 63 67
44 48 48 51 54 61
63 67 68 71 73 77 80 82
65 69 71 75 74
84 88 90 93 97 97
62 66 70 73 77
26 30 34 37 39 45
31 35 38 41 43 49 51 54
3 7 13 16 17 20 23 21
42 46 49 55 55
71 75 78 84 88
53 57 60 62 69 71 77
66 72 74 77 79 80
46 53 55 56 55
6 11 12 14 14
36 41 44 46 49 51 54 58
66 71 73 75 78 80 81 87
55 62 63 64 66 63 65
22 27 28 25 22
90 95 93 94 95 95
35 41 43 46 45 49
74 80 83 86 88 87 88 95
39 44 46 47 49 49 52
73 78 80 80 82 81
81 86 89 91 91 94 95 95
28 34 37 38 40 43 43 47
72 77 80 80 82 83 84 91
76 81 82 84 88 89 91
36 43 47 49 50 47
74 79 80 83 84 87 91 91
48 55 58 62 65 67 69 73
14 20 24 27 28 31 38
33 39 40 45 47 50 52
71 78 84 85 88 89 87
46 52 59 60 63 65 67 67
27 32 35 37 40 47 48 52
66 71 72 78 81 83 90
42 39 37 35 36
46 45 43 40 39 36 33 33
31 28 27 24 22 18
27 24 23 22 19 14
51 50 49 52 51 49 46 44
78 77 75 74 75 77
14 12 13 12 10 7 5 5
41 38 35 38 34
50 48 49 47 40
70 69 69 67 65
55 52 52 51 54
73 70 68 65 65 62 59 59
99 96 95 95 91
76 73 70 68 68 63
13 11 8 4 2
26 23 22 19 16 12 9 10
95 92 89 85 85
25 24 22 18 15 13 10 6
87 86 82 79 78 73
92 90 88 85 78 77 75 72
50 48 47 42 40 42
75 74 73 67 65 63 60 60
63 60 59 52 50 47 44 40
43 40 39 34 27
27 30 29 28 25
29 30 27 24 23 21 24
66 67 65 63 61 61
93 96 95 93 89
90 92 91 90 89 88 85 78
15 17 15 12 9 8 10 8
23 25 23 22 25 26
77 78 77 78 75 75
12 15 13 16 12
23 26 24 21 22 17
92 93 93 91 89 88 85 84
92 93 90 89 88 86 86 88
29 31 31 29 27 27
31 34 34 32 28
87 88 87 85 84 84 77
74 75 74 72 68 67
52 54 52 50 46 48
75 78 75 71 69 69
28 31 28 25 21 17
70 72 69 65 58
80 83 82 76 75 73 71
9 11 9 3 2 5
53 56 55 52 47 47
14 17 15 14 11 6 2
41 42 37 35 28
83 83 80 77 74 71 68 65
20 20 18 17 16 18
76 76 74 71 69 66 64 64
40 40 37 34 32 31 27
63 63 62 59 58 57 55 50
63 63 60 61 59
24 24 25 22 21 23
24 24 22 20 19 21 21
17 17 15 14 17 16 14 10
56 56 54 52 51 48 51 46
41 41 41 39 36
36 36 34 34 37
28 28 26 23 23 21 18 18
69 69 68 65 65 64 61 57
81 81 79 79 76 74 67
35 35 33 30 27 23 21
81 81 80 76 74 73 74
51 51 47 45 42 41 39 39
89 89 87 83 79
27 27 24 22 20 16 13 6
82 82 79 73 71 68 66
63 63 60 55 54 52 49 52
17 17 12 11 9 9
40 40 39 36 31 28 26 22
85 85 82 81 79 74 67
61 57 54 51 49 46
38 34 32 31 29 27 26 28
32 28 27 26 26
49 45 42 40 38 35 31
36 32 29 27 25 22 16
73 69 68 67 65 62 65 63
19 15 14 17 20
95 91 89 87 88 86 86
29 25 23 21 19 20 18 14
21 17 16 13 12 9 10 4
85 81 80 79 77 74 74 71
95 91 90 88 88 87 90
80 76 76 73 70 69 69
88 84 83 81 79 76 76 72
67 63 61 61 59 54
50 46 42 39 38 35 32
39 35 31 29 26 23 26
17 13 12 11 8 7 3 3
96 92 91 87 84 80
19 15 13 12 8 1
25 21 19 14 11 9 8 6
30 26 24 18 19
45 41 40 33 31 31
72 68 61 60 58 54
96 92 91 90 84 82 76
44 37 36 34 33 32 30
43 38 35 32 33
33 27 24 21 18 18
67 62 59 57 54 52 49 45
99 92 90 88 82
64 58 57 59 57
80 75 74 71 72 69 72
12 7 4 5 3 3
13 7 5 6 2
79 74 75 73 71 68 63
42 37 36 34 34 33 31
52 45 43 40 39 39 40
36 30 30 29 27 27
27 21 19 16 13 13 12 8
63 58 58 57 55 52 47
65 59 56 52 51 49 47 45
17 10 8 7 3 5
88 82 80 79 75 75
26 19 18 14 13 9
37 32 31 30 26 23 18
19 12 10 9 3 1
51 44 41 38 33 32 34
44 39 36 33 31 25 25
21 16 14 11 6 2
53 47 46 44 37 34 28
35 38 40 42 43 44 41
83 85 87 89 89
37 40 42 45 46 47 48 52
25 27 29 30 32 34 39
85 87 88 90 92 89 92 93
71 74 75 73 76 78 76
34 36 38 35 37 37
40 42 43 46 44 48
15 16 18 17 19 20 26
8 9 11 14 14 15 18 19
71 73 76 76 73
17 18 19 21 23 23 26 26
52 53 55 55 57 58 59 63
19 21 23 23 30
4 5 7 8 12 15 18
58 60 64 66 63
4 6 10 13 13
42 45 48 52 53 56 60
21 24 26 30 32 33 35 40
75 78 81 87 88 90
54 56 57 63 61
42 44 47 48 55 57 60 60
73 76 77 79 86 90
45 46 51 52 58
49 47 50 52 55 56 57
57 55 58 61 58
15 13 16 19 21 23 23
63 62 63 66 68 69 73
63 61 62 63 65 72
92 89 87 89 92
7 6 8 9 12 11 8
14 11 10 11 11
26 24 27 28 29 26 30
32 29 30 32 34 36 35 41
19 16 16 19 20
74 73 76 76 75
65 63 63 64 64
43 42 42 44 45 48 52
63 61 62 62 63 66 68 75
63 61 65 66 68 70 72 73
21 18 20 24 27 24
18 16 20 23 24 26 29 29
30 28 32 33 36 40
23 20 23 24 28 31 37
63 61 63 65 72 75
41 39 40 47 48 49 48
29 27 32 34 34
36 34 36 37 38 44 48
38 37 40 45 46 49 50 56
49 49 52 55 56 57
68 68 71 72 73 72
47 47 48 51 51
87 87 89 92 95 99
47 47 48 49 51 52 57
86 86 88 87 90
74 74 75 78 79 78 77
55 55 57 55 57 58 58
85 85 86 87 86 88 91 95
46 46 47 46 48 49 54
80 80 80 83 84 86 89
73 73 74 76 78 81 81 79
93 93 95 96 96 96
28 28 30 30 34
24 24 27 27 29 30 32 37
80 80 84 87 89
48 48 51 55 57 56
43 43 44 48 49 50 51 51
78 78 81 85 86 88 89 93
62 62 65 69 71 74 79
25 25 27 29 30 37 39
82 82 85 88 90 96 93
35 35 36 39 44 44
48 48 53 55 59
68 68 70 73 74 80 81 86
11 15 16 19 20
78 82 83 84 87 90 91 90
32 36 37 39 39
15 19 21 24 28
21 25 27 28 30 33 40
16 20 23 26 27 25 26
8 12 10 11 9
44 48 47 49 50 50
2 6 8 11 8 12
78 82 85 87 89 91 89 95
58 62 62 64 66 68
36 40 40 41 42 44 42
39 43 46 46 46
38 42 45 46 49 52 52 56
53 57 57 60 62 67
15 19 22 23 26 30 33 34
36 40 44 46 48 45
54 58 59 60 63 67 67
54 58 62 64 68
31 35 38 41 45 48 50 57
19 23 24 27 29 36 37 38
23 27 33 36 34
16 20 21 26 27 30 32 32
79 83 84 91 94 95 99
59 63 65 72 78
34 40 43 46 47 48
8 14 16 18 19 18
29 34 36 38 39 40 41 41
20 25 28 29 30 34
48 53 55 58 60 65
38 44 47 46 49
83 89 91 93 91 94 96 93
16 22 20 22 22
78 84 83 84 86 87 90 94
10 15 18 19 16 18 24
34 40 40 43 44
10 15 18 21 24 24 23
9 15 15 18 21 21
70 75 76 76 80
15 22 25 28 29 29 36
54 59 62 63 67 68 69
80 85 86 90 88
45 50 54 57 57
35 40 44 46 47 51
2 9 12 13 17 18 23
69 75 80 81 82 85 87
3 8 13 16 13
74 81 88 89 90 90
35 40 41 43 50 54
50 55 58 63 66 69 75
65 62 60 58 61
17 15 13 11 10 9 8 8
82 80 79 76 73 71 68 64
63 61 59 56 54 51 50 43
44 42 40 42 39 37 34
43 41 44 42 45
48 47 45 44 46 44 41 41
91 88 85 82 79 80 76
81 78 81 78 75 70
16 14 13 13 10 7
69 67 66 66 65 68
70 67 67 66 66
89 88 87 85 84 84 83 79
87 84 84 83 81 74
15 14 11 7 4 3 2
26 23 19 17 20
72 70 68 64 63 63
46 45 43 41 37 35 31
27 26 25 24 20 18 17 10
42 40 37 32 30 29 26 25
91 89 87 85 80 78 75 77
83 81 79 77 76 70 70
95 94 93 90 89 86 80 76
49 46 39 36 34 31 29 22
58 59 57 56 55 53 52 49
88 91 88 86 84 87
82 84 83 80 77 74 73 73
22 25 24 21 17
17 20 19 16 10
4 5 3 2 5 4 2
27 29 32 31 32
52 54 52 49 47 44 47 47
45 48 46 47 43
84 86 88 86 83 80 77 72
9 11 8 8 5
39 40 37 36 34 34 33 35
45 47 44 44 44
38 39 39 38 34
70 71 69 69 64
20 23 19 18 17
27 29 25 23 21 19 22
15 17 13 11 10 7 7
96 97 96 92 89 86 82
62 64 63 59 58 55 49
53 54 47 44 42 40 37 36
82 84 79 77 79
30 32 30 25 24 22 22
36 37 36 33 27 23
80 81 80 77 71 68 62
59 59 58 56 54 53 52
48 48 45 42 40 38 40
63 63 62 60 57 55 53 53
27 27 25 24 20
28 28 25 23 18
68 68 67 64 63 64 62 60
49 49 50 47 46 45 42 44
39 39 40 38 38
83 83 81 80 79 77 79 75
86 86 84 87 84 78
99 99 99 98 95 92
34 34 31 31 29 27 24 25
37 37 34 32 32 32
16 16 13 12 9 9 5
25 25 25 22 20 17 11
70 70 66 64 61
71 71 68 65 62 58 59
64 64 60 59 57 57
89 89 88 84 80
83 83 79 78 73
26 26 19 16 13 12
46 46 39 36 37
52 52 50 47 40 37 37
58 58 57 52 49 45
68 68 65 64 59 57 50
68 64 63 60 59 57
21 17 16 15 13 10 8 10
68 64 63 61 59 58 58
86 82 79 77 76 72
49 45 44 42 41 36
94 90 88 85 84 85 82 79
86 82 80 78 81 83
49 45 46 45 43 43
78 74 75 73 71 68 65 61
57 53 52 50 48 50 43
78 74 72 69 69 67
8 4 3 2 1 1 3
27 23 23 22 22
27 23 23 21 20 16
85 81 80 78 75 74 74 68
15 11 8 4 3 2
68 64 62 60 56 55 53 55
82 78 75 71 68 66 66
57 53 52 48 47 46 44 40
38 34 30 29 24
29 25 20 18 17 14
28 24 21 16 17
94 90 83 81 79 77 77
60 56 53 50 43 39
36 32 27 26 21
36 30 29 26 25 23
16 9 8 6 5 3 2 5
92 87 84 81 78 75 75
26 21 20 17 16 13 9
33 26 23 22 21 18 17 10
95 89 86 85 83 86 84
54 47 45 44 43 44 43 45
22 15 12 9 10 8 8
92 87 84 85 82 81 77
88 83 80 79 76 78 75 68
22 15 15 13 11 9 8
82 77 77 76 74 76
90 83 80 79 79 78 78
70 64 62 60 59 59 55
87 80 80 78 76 74 71 66
31 25 21 19 16
90 85 82 81 79 78 74 75
64 59 56 52 52
63 58 57 53 51 47
64 57 53 51 50 47 45 38
60 53 52 46 43
85 78 75 69 67 65 64 66
35 29 22 20 20
37 32 27 24 23 22 19 15
67 60 57 56 54 47 41
14 17 15 12 12 8
10 10 11 14 17 20 22 22
98 96 95 93 92 86
73 71 72 74 78
50 54 58 60 62
57 59 62 62 63 61
88 84 78 76 73
49 49 45 44 43 39
47 47 50 51 52 54
59 57 56 52 49
13 12 11 10 10 7 7
94 90 89 88 87 88 88
24 24 22 16 14 8
45 46 48 49 50 52 52
64 64 64 65 67 69 73
53 58 60 61 62 64 64 68
52 55 57 54 53
71 68 64 62 58
64 68 70 71 71 74 75 79
54 55 55 57 57
89 92 85 82 79 78 78
81 80 83 84 90 91
14 20 22 25 29 32 36
46 46 48 48 49 51 57
18 14 13 9 7 5
92 87 84 84 81 82
50 49 46 46 45 43 44
82 85 86 87 89 86
44 49 51 54 56 63 63
88 90 90 87 85 82 77
64 71 72 76 75
97 98 97 95 97 95 94 90
46 45 48 50 54 54
24 20 18 16 15 14 13 8
53 56 59 58 55 58
49 49 50 55 58
47 41 38 38 37 33
25 31 28 30 33 35 37 40
64 63 65 67 70 67 70 70
53 49 47 47 44 43 37
30 37 43 45 44
53 48 47 45 41
65 69 73 76 80
58 52 48 46 45 44 41 43
9 7 7 10 15
82 82 83 90 90
63 63 60 57 53 52 46
31 27 25 24 20 19 12
5 4 7 6 5 3 1
86 82 81 84 80
86 81 79 76 75 73 69 67
54 57 59 60 62 66
52 48 46 41 37
46 46 43 41 40 39 35
49 50 51 53 59 64
25 27 30 32 32 33
59 62 59 57 56
16 16 16 13 12 10 8 11
34 28 24 22 20 17 13
57 57 57 60 63 62
53 59 57 58 62
29 27 25 24 18 16 9
50 54 57 57 58 60 60
41 35 32 32 30 29 23
66 69 68 62 59 56 52
49 44 45 42 41 37
61 61 60 57 50
3 1 2 9 11 11
29 26 24 23 21 20 19 19
59 60 61 63 63 65 69
97 95 91 88 85 82 83
4 11 13 20 21 22 24
72 74 69 66 65 59
62 68 71 74 74 77 78 78
69 65 62 61 63 61 54
15 17 14 11 10 12 12
83 80 79 75 74 74
75 70 69 63 61 62
65 69 70 73 76 75 77 77
34 29 27 25 24 21 18 21
6 6 7 9 12 16 20
50 50 47 45 44 45 45
69 70 72 69 72 76
80 80 78 74 73 72 71 71
28 24 20 17 14 15
51 51 54 56 61
38 34 33 33 32
23 23 25 27 31 28
39 37 39 42 44 46 48
56 62 63 63 65 67 69 67
74 74 80 81 78
73 71 70 67 63 58
32 36 38 40 43 50 56
87 83 81 75 69
69 65 62 62 64
85 88 89 93 98
20 13 11 10 10
52 53 56 60 62 66
58 58 59 62 62 65 67
75 81 83 85 87 87
38 32 29 24 21 19 14
93 89 82 80 79 77 75 78
11 11 13 14 13 14 13
50 50 45 44 43 40 38
86 82 79 76 72 72
81 88 89 92 95 96 96 97
39 37 42 43 42
22 21 24 21 17
24 23 22 22 21
38 35 35 38 42
61 61 64 66 68 70 67 67
92 92 90 88 90 89 88 89
4 4 5 9 15
78 82 84 87 91
63 62 61 59 57 54 54 50
51 55 60 61 63 65 68
43 48 54 56 58 63
47 49 53 54 54
81 85 88 91 96
44 44 42 44 46 49 52 59
84 86 85 83 80 78 81 80
13 13 12 8 7
66 70 72 73 74 75 74
85 87 86 83 79
19 24 25 27 24 27 30 30
17 20 23 24 30 27
15 10 11 10 8 5 6
81 85 91 94 97 94
75 72 75 78 78 81 83 81
49 51 48 48 45 44 42 45
59 57 60 60 62
91 84 82 77 77
27 27 25 24 22 24
52 55 51 49 49
70 70 72 79 80 84
74 78 79 83 85 86 88 88
76 70 73 72 71 69
47 43 41 40 39 41 39
82 81 84 86 85 89
21 25 26 29 26 27 28 25
41 36 35 33 30 28 22
37 37 39 41 43 47
13 20 21 24 26 29 34
38 38 36 35 30 26
14 18 19 20 20 27
85 81 78 74 70
17 15 16 15 16 18
96 99 95 94 93 91 88 81
74 79 80 82 85 83 89
41 38 39 44 46 51
23 19 13 11 9 9
72 79 80 81 78 80 82 80
93 93 95 98 96 97 99
27 23 22 20 19 16 16
83 83 85 88 90 92 89
58 55 52 49 42 42
45 39 37 37 35 34 31
40 44 47 45 46
3 3 4 1 5
11 13 8 6 5 3 2
43 40 42 41 40 39 36 37
34 31 29 28 24
25 23 24 25 28 25 23
94 89 88 84 82 80 79 79
76 72 75 74 75
17 20 21 18 21 24 27 28
59 55 54 51 50 46
11 11 10 8 8 5 4 3
15 19 21 24 26 27 28 28
11 18 20 24 26 27 27
58 56 58 61 63 64 66 73
68 67 68 69 72 76 77 79
2 9 12 16 19
38 38 37 37 32
28 28 31 30 23
67 67 66 65 62 59
1 7 8 11 12 15 19
40 39 41 43 47 54
72 65 62 60 53 49
98 99 97 93 91 87
56 59 58 56 54 47
19 19 15 12 9 11
36 38 36 39 40 47
8 9 10 12 13 17 15
55 62 64 67 70 72 70
19 21 20 18 19
78 81 82 86 87 90 93 96
30 28 31 32 35 34
42 40 37 32 30 29 27 26
78 78 81 82 85 85 85
31 35 37 38 40 41
72 74 75 78 78 80 82 87
14 14 11 8 9 6
1 5 6 7 10 14 16 14
47 51 54 54 57 54
3 3 3 2 2
28 34 35 39 44
25 25 28 33 39
82 85 82 81 78 78
83 87 90 91 93 93 96 97
80 81 78 74 76
31 31 31 28 26 23 19
39 45 48 51 54 60 64
73 76 73 73 72 69
55 59 63 66 69 70 72 79
72 68 65 64 62 62 62
49 49 44 41 41
70 74 77 78 77 80 82 87
49 53 50 52 53 54 57 61
98 93 91 88 90 89 84
64 66 61 59 62
88 86 88 87 82
46 44 43 40 35 37
28 24 21 18 15 13 10 7
53 52 54 55 57 57
93 89 87 84 82 82 80 76
93 87 89 86 86
9 10 11 14 15 13 15 15
10 11 13 20 21 24 25 29
71 74 79 80 80
39 43 46 47 48 55 55
85 81 78 77 76 73 75
66 73 76 77 78 78 85
80 78 79 77 79 85
33 34 33 31 27 26
69 66 69 73 75 77 76
36 30 27 25 23 23 23
70 67 66 64 62 65
23 25 23 20 19 20 17 11
24 24 25 29 30 32 34 35
76 77 80 83 86 92 94
62 60 58 55 53 53 51 45
14 16 13 12 10 10 7 7
74 74 73 70 69 66 63 63
50 53 56 59 60 65
89 88 85 82 81 80
27 25 22 21 20
71 72 75 78 80 82
58 55 54 53 52 51 50 49
44 41 39 37 34 33
78 81 84 86 88 91 94
25 26 28 31 32 34
47 46 43 40 38
10 13 14 17 19 22
80 82 83 84 86 89
79 80 82 84 85 86 88
52 55 57 60 61
58 61 62 64 65 68 69 70
82 83 86 89 91 93
24 23 22 21 18 17
23 26 27 28 31 32
19 18 16 14 12 9
70 68 65 62 60 58 57
50 52 55 56 58
18 21 23 25 27 29 30
44 47 50 52 53
96 95 92 90 87
43 46 49 50 52
12 13 16 19 21 22 24 25
52 55 56 57 58 59 62 63
25 23 21 18 16 13
89 86 84 81 80
55 53 50 47 46
65 64 63 60 57 54
14 15 17 18 19 20 22 25
30 29 26 23 22 21
29 27 24 21 19 16 15 13
40 39 38 37 36 33 32 31
24 25 28 29 32
87 84 82 79 78 77
18 21 22 25 27 30 32 35
81 82 83 84 87 89 92
7 8 11 13 14 17 19 22
10 7 6 5 4 1
66 65 64 61 58 57
78 76 74 73 71 68 66
63 65 68 69 71 73 74 77
63 65 67 69 70 71 72 73
90 88 86 85 82 81
49 47 46 45 42 41 38
76 75 73 72 70 68 67
79 81 82 83 84
76 75 73 72 69
64 61 59 58 56 54 53 52
87 85 83 80 79 76
30 29 26 24 22 19 16 14
56 58 61 64 66
21 19 17 14 11
75 78 79 81 84 86
76 79 80 83 85
66 65 64 61 58
56 53 50 48 47 45 43
34 32 30 27 25
10 13 16 19 20 23 26 28
41 44 45 48 50 51 52 53
28 25 24 21 19 17 14
36 34 32 30 28 25 24
38 40 42 44 47 49 50
1 3 4 6 8 10
37 35 32 30 28 27 26
37 35 34 31 29 28 26 24
94 91 90 89 88
70 69 68 65 62 60
81 83 86 88 90 92 95 98
90 89 86 84 82 80
52 51 48 47 46 43
47 44 41 38 37 35 32
38 37 34 33 30 28
58 56 55 54 51
19 17 14 13 11 8
33 31 29 26 24 23 22 19
40 42 43 45 46 47 49 50
77 75 73 71 70 67 64 61
43 42 39 36 33
4 6 9 10 12 14 15 18
14 13 12 9 8 5
43 41 39 38 37 35 33
70 72 73 76 77
80 82 84 85 86 89
65 66 67 69 72
17 20 22 23 26
85 86 87 88 89
50 47 44 42 41 38
6 7 9 12 14 16 18
89 91 92 95 97
45 47 49 51 53
61 60 58 56 55 52 51 48
64 63 60 58 55
62 64 65 66 69 72 73 76
57 59 60 63 66 69
74 71 70 67 65 63 60 58
51 53 54 57 59
86 88 90 91 94
68 71 74 77 79 81 83
76 74 71 68 67
81 79 78 76 74
43 45 48 51 54 55 58 59
84 82 81 80 79 78 76 75
49 51 53 54 57 60
37 39 41 44 47 50
65 68 69 70 73 74 77 79
91 90 88 85 82
23 25 26 29 32 34
41 42 45 48 50
64 61 59 57 54 51 50
23 25 26 29 30 33 35
19 16 14 12 10
79 80 81 82 85
36 37 38 40 43 44 46 49
60 61 62 63 66
46 45 43 42 40
49 52 55 57 60
14 15 18 19 20 21
98 96 95 94 93 90 89 86
76 77 78 79 81
18 15 13 11 10 7 6 4
34 35 37 38 41 44 46 48
35 32 29 28 27 25
78 80 83 86 88
87 84 82 80 79 78 77
75 72 70 69 67
90 92 94 95 97 98
36 33 31 28 26 25 23
50 52 54 56 57 58 59 62
56 57 58 61 62 63 66
81 80 79 78 75 74
20 21 22 23 24 26
45 47 48 49 51 53
39 41 43 45 47 49 51 52
18 20 22 23 26
18 20 21 24 26 29
25 23 20 17 14 12 9 6
12 15 16 18 20 23 25 27
10 13 16 19 22 23 24
98 95 92 91 89 86 85 83
14 16 17 19 21 23 25
5 6 9 11 12 13 14
66 64 63 62 60
50 49 46 45 43
87 86 83 82 81 80
34 31 30 29 27 24 21 20
28 25 24 23 22 19 18
66 64 62 60 58
57 56 53 52 50
48 50 52 54 57 58 61
65 68 70 72 74
11 8 6 5 2
30 29 27 25 22 21
52 55 56 57 59 62 65 67
78 76 75 72 70 69 66 63
5 8 10 13 16 18 19 20
31 28 27 24 21 19
32 34 35 38 40 43
23 26 29 30 32
87 86 83 81 78 77 75
35 37 39 42 45
72 73 76 78 79 82 85 86
78 75 73 71 70 67 66 63
72 70 69 66 63
48 46 43 40 39 36 35
2 4 6 7 8 10
88 90 91 93 96 98
66 69 70 73 75
28 26 23 22 21 18 15
12 14 17 19 20 21 24 25
20 17 16 14 13 11 8
30 27 25 22 21 19
50 47 46 44 43 42 40
91 88 85 83 80 78
59 60 63 66 68
42 44 45 46 49 51 53 55
82 80 77 74 71 70
13 11 10 9 7 6 3
69 66 64 61 58
61 58 55 54 53 52 51
25 23 20 19 16
21 23 26 29 32 34 35
22 23 25 26 29
25 24 21 20 19 18
48 51 54 55 57 58 59
23 25 28 31 34 36
40 41 44 46 49 50
83 81 78 75 74
16 19 20 23 26 29 30 31
14 13 12 9 6
77 76 74 71 70 69
75 73 72 69 66 63
50 52 54 56 59 60
53 50 49 46 44 43 41
18 16 13 12 9 8
26 24 22 19 16
44 42 39 36 34
37 40 41 44 47 49 50 52
8 9 10 13 14 17
54 56 57 59 61 62 64
54 56 59 61 63
14 13 11 10 9 6 5 2
63 65 68 69 72 74 75
70 69 67 66 63 61 58
64 67 70 73 74 76
40 39 37 36 35 34 31 30
45 42 41 39 36 33 30
61 59 57 54 53 50
31 33 34 35 37
38 40 43 44 46 49
36 38 41 43 44 46 49 50
63 62 61 60 58 56
15 12 10 8 7 6 5
42 45 47 50 53 55
57 56 54 53 50 48 47
13 10 8 7 6
86 85 83 81 78 76 74 71
44 43 42 40 38
33 31 28 27 24 22 21
72 70 69 68 67 66 63 62
58 60 63 66 68 71 72 73
29 30 33 36 38 39
11 8 6 3 1
33 32 31 29 27 25 24
53 56 58 61 64
60 58 56 55 54 51
67 70 71 73 75
3 5 7 9 12 13 16
28 29 30 33 36
40 37 36 33 32 30
22 19 16 13 11
25 28 30 33 34 36 37
32 34 36 37 40 42 44
23 22 20 19 18 16 13
59 61 63 64 66 69 71
30 29 28 26 25 22 20
60 61 62 65 68
61 64 67 70 72
48 47 45 44 42 39 37 36
77 79 80 83 85 87
29 31 33 34 36 38
6 8 11 13 16 17 18 21
98 97 94 92 91 88 87 84
35 34 33 32 30 27 26
87 89 90 92 95
10 9 8 5 4 3
68 69 70 73 74 77 79
63 60 58 55 53 50
68 71 72 75 77
34 36 39 40 43 44
20 22 23 26 28
48 46 44 42 39 38
96 94 91 88 85 83 80 78
79 76 74 73 71 70 67 64
26 24 21 20 19 16
67 69 71 73 76 77 80
72 71 70 67 65
60 57 55 54 53 51 50 47
72 73 76 78 79 80 81 83
64 67 69 70 72 73 74
41 42 45 48 49 51 52 55
85 88 89 90 91 94 95 98
96 93 91 89 86 85 83
72 71 68 66 63
86 89 91 92 95 96
35 38 39 41 44 45
12 15 16 18 21 22 24
65 63 60 59 57 54 52
37 34 31 29 27 25 22 19
"""
sign = lambda x: copysign(1, x)

def is_safe(r):
    s = sign(r[0] - r[1])
    
    for r1, r2 in zip(r[:-1], r[1:]):
        delta = r1 - r2
        if sign(delta) != s:
            return False
        if abs(delta) < 1 or abs(delta) > 3:
            return False
    return True

def solve1(inp):
    inp = inp.strip().split('\n')

    reports = [i.split() for i in inp]
    reports = [list(map(lambda x: int(x), r)) for r in reports]
    num_safe = 0
    for r in reports:
        if is_safe(r):
            num_safe +=1
    return num_safe

def is_safe2(r):
    if is_safe(r):
        return True

    # Otherwise try removing each level position
    for i in range(len(r)):
        new_r = r[:]
        new_r.pop(i)
        if is_safe(new_r):
            return True
    return False

def solve2(inp):
    inp = inp.strip().split('\n')

    reports = [i.split() for i in inp]
    reports = [list(map(lambda x: int(x), r)) for r in reports]
    num_safe = 0
    for r in reports:
        if is_safe2(r):
            num_safe +=1
    return num_safe


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

