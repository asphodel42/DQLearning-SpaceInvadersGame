score_points = [8, 0, 6, 16, 7, 21, 3, 12, 11, 5, 3, 8, 1, 10, 2, 6, 5, 4, 1, 5, 1, 3, 5, 4, 8, 3, 4, 2, 2, 9, 2, 7, 7, 2, 6, 2, 6, 3, 0, 5, 1, 5, 4, 9, 11, 1, 10, 2, 5, 7, 8, 1, 4, 6, 7, 4, 7, 9, 2, 6, 3, 5, 7, 9, 6, 5, 4, 4, 7, 1, 7, 2, 9, 8, 1, 3, 3, 4, 5, 5, 6, 6, 6, 4, 1, 12, 4, 3, 1, 5, 7, 4, 2, 4, 2, 5, 2, 10, 6, 6, 7, 4, 5, 5, 6, 8, 5, 9, 6, 4, 5, 13, 9, 9, 5, 5, 1, 5, 10, 5, 6, 4, 15, 10, 7, 8, 11, 2, 8, 6, 12, 1, 9, 7, 3, 3, 6, 0, 4, 7, 5, 6, 10, 10, 8, 2, 3, 13, 6, 4, 9, 7, 6, 14, 6, 2, 7, 0, 15, 1, 5, 7, 5, 2, 6, 5, 5, 3, 18, 6, 1, 15, 8, 5, 3, 4, 5, 1, 12, 2, 2, 4, 5, 1, 7, 5, 5, 6, 2, 11, 2, 3, 2, 3, 5, 3, 2, 10, 6, 5, 12, 0, 6, 10, 1, 7, 10, 4, 4, 6, 2, 8, 4, 5, 2, 5, 2, 3, 6, 10, 5, 3, 11, 6, 11, 4, 4, 3, 4, 12, 8, 5, 5, 8, 7, 3, 10, 5, 3, 2, 1, 8, 9, 8, 3, 7, 17, 7, 1, 4, 5, 8, 19, 5, 11, 7, 4, 2, 0, 5, 8, 8, 6, 4, 3, 6, 2, 2, 11, 5, 9, 5, 23, 1, 8, 4, 4, 3, 5, 7, 1, 5, 1, 2, 6, 12, 5, 9, 1, 3, 8, 5, 6, 0, 5, 5, 4, 7, 3, 4, 7, 4, 12, 17, 3, 10, 4, 11, 5, 6, 8, 9, 9, 5, 9, 8, 3, 4, 15, 21, 4, 9, 3, 4, 2, 3, 5, 4, 9, 9, 2, 2, 11, 10, 3, 4, 4, 5, 1, 7, 2, 5, 3, 4, 13, 1, 7, 2, 6, 6, 2, 4, 10, 4, 3, 9, 6, 3, 7, 6, 4, 4, 8, 9, 7, 3, 4, 4, 5, 7, 4, 14, 6, 7, 7, 5, 10, 3, 3, 11, 6, 2, 13, 9, 1, 2, 3, 9, 9, 12, 2, 5, 1, 4, 1, 10, 2, 7, 4, 3, 9, 3, 2, 4, 1, 1, 2, 3, 5, 6, 7, 13, 1, 4, 5, 1, 3, 5, 6, 6, 4, 10, 7, 17, 8, 3, 6, 3, 6, 2, 0, 4, 2, 9, 2, 4, 8, 7, 4, 7, 7, 1, 5, 4, 4, 5, 6, 3, 6, 5, 7, 4, 1, 0, 6, 7, 2, 4, 1, 3, 6, 1, 3, 15, 4, 5, 9, 4, 8, 4, 12, 5, 9, 9, 4, 0, 10, 5, 8, 6, 5, 4, 2, 3, 6, 3, 5, 5, 9, 2, 3, 1, 2, 1, 8, 5, 4, 5, 2, 4, 9, 15, 2, 0, 6, 3, 1, 7, 7, 12, 1, 12, 9, 2, 6, 3, 4, 4, 3, 5, 9, 1, 2, 3, 4, 1, 4, 2, 6, 7, 1, 11, 2, 9, 4, 5, 4, 5, 3, 4, 3, 19, 2, 5, 7, 11, 11, 2, 4, 2, 15, 9, 8, 3, 3, 4, 5, 4, 3, 9, 2, 5, 9, 23, 11, 4, 9, 3, 3, 9, 10, 7, 8, 2, 9, 9, 5, 5, 4, 3, 15, 5, 7, 6, 14, 3, 3, 12, 8, 8, 6, 3, 3, 7, 2, 8, 8, 11, 3, 5, 1, 2, 6, 0, 11, 1, 5, 1, 3, 2, 25, 1, 5, 17, 10, 2, 6, 2, 2, 2, 4, 5, 2, 6, 6, 10, 15, 9, 6, 14, 0, 4, 3, 14, 12, 3, 2, 10, 9, 8, 0, 3, 14, 1, 3, 3, 7, 8, 10, 4, 13, 14, 12, 3, 3, 12, 5, 10, 11, 32, 8, 10, 5, 10, 2, 9, 4, 4, 5, 4, 0, 4, 9, 5, 9, 12, 3, 1, 6, 13, 1, 1, 5, 9, 2, 1, 0, 8, 10, 13, 8, 7, 17, 8, 8, 2, 10, 4, 2, 3, 4, 5, 1, 7, 2, 4, 11, 7, 7, 3, 2, 2, 1, 13, 2, 6, 1, 1, 6, 2, 4, 7, 5, 4, 11, 3, 26, 10, 6, 1, 2, 3, 5, 9, 2, 8, 4, 1, 5, 5, 6, 1, 1, 6, 3, 2, 10, 3, 3, 6, 4, 17, 4, 2, 0, 14, 3, 0, 4, 4, 3, 10, 3, 11, 6, 0, 6, 8, 2, 11, 4, 13, 4, 4, 5, 2, 2, 6, 5, 6, 4, 0, 4, 4, 2, 9, 5, 8, 2, 13, 3, 10, 10, 1, 10, 4, 4, 15, 2, 4, 9, 5, 6, 2, 13, 4, 4, 6, 5, 15, 2, 6, 3, 3, 13, 5, 5, 10, 3, 6, 8, 6, 1, 3, 29, 11, 11, 12, 13, 5, 8, 12, 4, 3, 1, 4, 6, 2, 2, 14, 8, 10, 1, 5, 1, 9, 8, 2, 7, 4, 5, 4, 5, 10, 8, 1, 1, 8, 6, 8, 2, 7, 1, 4, 1, 6, 11, 4, 3, 7, 4, 4, 5, 5, 3, 7, 0, 3, 1, 5, 8, 11, 8, 12, 9, 4, 3, 7, 13, 1, 2, 2, 4, 3, 2, 7, 5, 3, 4, 1, 5, 3, 12, 1, 8, 1, 4, 3, 7, 24, 7, 15, 12, 13, 4, 4, 3, 5, 4, 6, 7, 8, 0, 6, 0, 1, 2, 3, 5, 8, 7, 1, 8, 3, 24, 4, 1, 5, 34, 2, 11, 3, 4, 10, 7, 16, 6, 1, 8, 5, 10, 4, 0, 6, 2, 9, 7, 7, 2, 5, 6, 4, 4, 8, 4, 2, 9, 7, 11, 19, 5, 20, 6, 1, 9, 11, 3, 2, 6, 2, 2, 18, 20, 7, 6, 0, 4, 6, 2, 5, 2, 4, 3, 0, 19, 1, 7, 5, 0, 19, 2, 19, 10, 1, 3, 4, 5, 5, 5, 23, 8, 4, 4, 7, 4, 7, 4, 3, 62, 13, 23, 12, 2, 10, 8, 11, 7, 6, 8, 8, 5, 5, 7, 6, 2, 8, 2, 3, 2, 1, 19, 5, 7, 0, 7, 13, 3, 4, 6, 2, 8, 1, 9, 5, 7, 8, 8, 11, 5, 10, 8, 13, 14, 4, 12, 8, 10, 5, 6, 9, 1, 7, 17, 5, 7, 2, 3, 3, 10, 6, 16, 3, 2, 8, 9, 3, 5, 20, 16, 8, 9, 8, 9, 11, 26, 4, 6, 1, 10, 10, 16, 6, 9, 2, 8, 9, 3, 16, 3, 2, 8, 3, 3, 0, 10, 2, 15, 12, 11, 4, 5, 6, 7, 3, 5, 4, 2, 9, 3, 3, 5, 10, 9, 7, 14, 4, 8, 4, 4, 4, 5, 20, 10, 14, 9, 18, 7, 7, 4, 3, 9, 5, 3, 13, 7, 0, 7, 8, 13, 6, 5, 13, 12, 4, 10, 10, 13, 4, 7, 14, 5, 7, 11, 12, 9, 15, 3, 6, 1, 5, 10, 8, 9, 1, 10, 15, 0, 8, 9, 13, 7, 2, 2, 4, 9, 1, 3, 1, 6, 7, 4, 10, 2, 4, 6, 6, 7, 7, 9, 11, 5, 9, 8, 4, 4, 4, 15, 12, 3, 15, 7, 10, 20, 5, 9, 4, 12, 2, 17, 10, 13, 3, 10, 5, 11, 11, 4, 5, 6, 5, 8, 7, 8, 3, 5, 7, 9, 3, 5, 9, 6, 8, 4, 1, 7, 2, 12, 8, 5, 13, 12, 3, 6, 3, 11, 4, 15, 6, 8, 0, 1, 4, 13, 24, 7, 2, 12, 3, 16, 11, 3, 6, 3, 1, 1, 4, 14, 5, 4, 11, 2, 14, 4, 3, 6, 4, 5, 27, 13, 3, 9, 3, 17, 12, 12, 10, 5, 3, 14, 4, 17, 6, 13, 6, 2, 4, 4, 8, 11, 9, 17, 14, 7, 5, 9, 2, 18, 2, 9, 7, 6, 4, 2, 19, 2, 8, 26, 2, 2, 11, 26, 22, 3, 15, 9, 14, 6, 3, 9, 10, 4, 3, 5, 10, 10, 11, 12, 4, 10, 14, 8, 3, 15, 27, 4, 18, 2, 4, 8, 5, 12, 6, 6, 5, 5, 0, 9, 5, 10, 3, 4, 0, 5, 16, 10, 5, 4, 10, 14, 8, 2, 2, 18, 3, 9, 8, 6, 9, 6, 1, 1, 10, 3, 7, 7, 1, 4, 4, 5, 15, 12, 6, 5, 10, 8, 7, 5, 9, 5, 7, 28, 8, 22, 6, 3, 8, 3, 20, 2, 6, 13, 12, 25, 3, 4, 10, 4, 13, 3, 8, 3, 0, 5, 3, 10, 29, 3, 8, 5, 16, 11, 10, 5, 26, 5, 16, 10, 0, 1, 12, 4, 0, 23, 7, 8, 9, 12, 14, 2, 12, 12, 5, 12, 11, 1, 11, 12, 8, 8, 19, 7, 9, 5, 1, 21, 7, 15, 8, 13, 25, 14, 8, 5, 13, 5, 62, 13, 11, 3, 31, 7, 5, 6, 9, 19, 21, 9, 12, 2, 2, 6, 2, 4, 7, 8, 9, 8, 20, 12, 7, 7, 9, 20, 10, 9, 4, 13, 14, 7, 14, 5, 22, 14, 12, 3, 22, 15, 4, 20, 15, 12, 3, 4, 9, 19, 6, 16, 11, 13, 3, 11, 12, 18, 7, 13, 5, 15, 6, 5, 21, 19, 10, 28, 30, 4, 1, 24, 8, 13, 6, 42, 11, 2, 9, 13, 9, 12, 5, 8, 15, 12, 16, 20, 6, 11, 7, 8, 9, 12, 6, 6, 5, 4, 4, 6, 10, 5, 8, 12, 10, 19, 2, 5, 0, 10, 29, 27, 23, 6, 13, 12, 6, 10, 17, 2, 7, 14, 11, 10, 12, 7, 9, 7, 4, 18, 12, 5, 15, 23, 15, 8, 14, 5, 14, 4, 2, 8, 8, 4, 12, 6, 4, 14, 18, 6, 30, 31, 22, 8, 2, 26, 11, 5, 13, 13, 26, 11, 35, 19, 11, 3, 18, 9, 10, 27, 34, 6, 10, 11, 8, 11, 1, 3, 2, 14, 10, 3, 9, 11, 13, 4, 12, 10, 10, 1, 16, 12, 5, 1, 4, 5, 12, 4, 12, 5, 28, 7, 20, 29, 26, 11, 16, 36, 9, 6, 8, 4, 5, 7, 4, 7, 14, 17, 7, 4, 10, 30, 19, 11, 5, 3, 4, 3, 3, 22, 32, 11, 7, 2, 1, 12, 10, 10, 13, 22, 9, 3, 10, 9, 7, 4, 8, 7, 7, 14, 3, 5, 7, 10, 14, 15, 7, 10, 8, 12, 8, 2, 17, 18, 9, 4, 6, 4, 9, 2, 9, 29, 3, 0, 4, 3, 5, 9, 5, 18, 1, 3, 9, 8, 3, 3, 7, 9, 7, 9, 4, 9, 9, 18, 11, 26, 9, 5, 11, 4, 2, 4, 14, 3, 3, 5, 1, 9, 9, 7, 10, 1, 7, 13, 4, 17, 2, 16, 10, 6, 4, 2, 5, 8, 11, 9, 9, 10, 8, 6, 11, 7, 20, 8, 7, 9, 12, 9, 7, 9, 16, 6, 12, 13, 2, 7, 10, 8, 21, 15, 1, 10, 14, 48, 9, 7, 15, 8, 15, 16, 19, 3, 2, 14, 9, 17, 5, 5, 11, 14, 3, 9, 8, 9, 12, 11, 9, 1, 2, 17, 10, 7, 7, 2, 4, 6, 11, 5, 12, 5, 0, 4, 6, 6, 21, 4, 7, 6, 7, 17, 4, 15, 13, 3, 12, 3, 4, 7, 11, 10, 4, 0, 0, 8, 7, 1, 20, 7, 12, 11, 6, 11, 11, 10, 9, 5, 4, 13, 11, 12, 11, 4, 10, 21, 4, 12, 7, 5, 5, 20, 3, 14, 14, 14, 5, 12, 7, 3, 4, 8, 7, 7, 7, 18, 5, 9, 3, 9, 11, 2, 4, 7, 11, 4, 10, 13, 5, 1, 11, 2, 13, 7, 7, 10, 8, 4, 6, 5, 10, 5, 6, 16, 5, 6, 6, 18, 11, 4, 7, 11, 4, 1, 3, 5, 1, 26, 9, 20, 12, 7, 2, 14, 24, 22, 6, 10, 4, 8, 7, 5, 1, 11, 16, 8, 6, 6, 13, 10, 14, 1, 8, 3, 1, 4, 8, 12, 12, 7, 7, 8, 3, 3, 15, 9, 7, 6, 9, 8, 24, 6, 4, 1, 10, 2, 7, 3, 1, 6, 5, 8, 7, 4, 6, 6, 6, 5, 14, 11, 5, 30, 7, 9, 7, 5, 9, 5, 10, 15, 18, 4, 9, 5, 3, 21, 10, 11, 21, 3, 11, 36, 34, 7, 9, 8, 26, 7, 3, 4, 8, 8, 11, 13, 4, 21, 24, 17, 9, 8, 26, 14, 15, 10, 16, 2, 15, 1, 5, 23, 23, 3, 3, 7, 13, 7, 4, 4, 11, 8, 19, 12, 12, 8, 12, 7, 11, 15, 13, 5, 18, 9, 13, 15, 11, 0, 11, 1, 10, 11, 19, 7, 4, 4, 4, 11, 9, 23, 8, 5, 22, 11, 29, 5, 1, 14, 16, 15, 10, 15, 2, 16, 5, 4, 4, 10, 8, 3, 11, 10, 3, 7, 16, 13, 22, 2, 5, 11, 5, 6, 8, 14, 6, 2, 4, 5, 12, 13, 10, 10, 6, 21, 10, 5, 2, 7, 4, 9, 7, 7, 9, 3, 14, 8, 8, 27, 4, 28, 16, 1, 9, 0, 2, 2, 8, 18, 3, 17, 16, 4, 12, 9, 9, 13, 30, 20, 4, 8, 7, 8, 12, 10, 7, 2, 1, 5, 5, 8, 11, 13, 5, 9, 15, 1, 13, 26, 9, 7, 9, 7, 2, 1, 2, 5, 5, 17, 12, 10, 3, 9, 10, 7, 4, 6, 8, 3, 8, 21, 11, 14, 12, 12, 4, 2, 15, 8, 8, 4, 9, 14, 9, 13, 23, 7, 7, 11, 15, 12, 11, 4, 6, 14, 2, 4, 11, 23, 2, 6, 15, 2, 1, 21, 1, 10, 18, 4, 25, 5, 9, 10, 14, 5, 5, 4, 19, 4, 6, 2, 7, 12, 51, 3, 4, 3, 5, 2, 8, 5, 15, 10, 14, 13, 6, 26, 7, 15, 18, 23, 5, 12, 9, 9, 10, 9, 3, 13, 15, 12, 5, 5, 11, 7, 2, 15, 10, 21, 9, 13, 6, 12, 4, 5, 5, 6, 6, 8, 44, 10, 19, 7, 16, 20, 7, 5, 1, 12, 4, 10, 15, 24, 18, 25, 5, 9, 0, 15, 23, 5, 4, 10, 4, 10, 11, 10, 16, 17, 7, 8, 17, 12, 6, 12, 12, 14, 10, 7, 19, 12, 14, 10, 22, 4, 12, 5, 51, 9, 17, 4, 15, 17, 12, 3, 4, 8, 4, 5, 11, 12, 6, 10, 8, 5, 7, 14, 15, 7, 13, 6, 59, 8, 2, 8, 6, 18, 10, 9, 10, 27, 24, 6, 13, 6, 1, 2, 7, 20, 18, 14, 9, 8, 14, 10, 4, 4, 20, 8, 26, 7, 6, 23, 6, 5, 14, 28, 34, 5, 2, 18, 6, 17, 6, 28, 17, 12, 14, 15, 13, 6, 9, 9, 7, 16, 9, 8, 13, 0, 12, 8, 10, 14, 3, 3, 11, 15, 13, 12, 4, 14, 4, 2, 12, 18, 19, 10, 23, 9, 11, 11, 4, 9, 13, 7, 9, 19, 1, 4, 24, 8, 9, 6, 3, 1, 15, 2, 6, 18, 7, 4, 4, 9, 18, 22, 11, 3, 11, 6, 3, 40, 2, 5, 15, 11, 14, 3, 8, 4, 10, 12, 4, 15, 18, 8, 11, 20, 13, 23, 3, 15, 4, 3, 8, 15, 4, 2, 7, 8, 7, 5, 26, 11, 20, 4, 6, 7, 15, 22, 6, 9, 8, 5, 6, 9, 14, 8, 3, 8, 8, 11, 3, 16, 15, 5, 22, 0, 11, 4, 6, 13, 9, 15, 12, 15, 15, 13, 10, 7, 3, 1, 10, 5, 6, 1, 9, 10, 19, 14, 10, 5, 7, 1, 10, 8, 6, 23, 5, 11, 15, 11, 4, 9, 8, 12, 4, 3, 9, 11, 12, 7, 9, 9, 11, 15, 5, 25, 7, 12, 2, 12, 12, 9, 8, 13, 6, 13, 9, 17, 9, 14, 5, 3, 8, 6, 5, 9, 5, 2, 13, 13, 8, 10, 3, 26, 7, 3, 8, 13, 12, 5, 10, 4, 10, 6, 26, 12, 5, 2, 18, 2, 11, 8, 9, 2, 8, 3, 4, 5, 10, 11, 21, 10, 14, 22, 1, 9, 15, 14, 18, 2, 3, 12, 5, 13, 6, 11, 14, 4, 7, 12, 11, 7, 6, 5, 32, 1, 1, 5, 19, 11, 5, 1, 11, 14, 25, 34, 2, 5, 6, 8, 4, 7, 8, 8, 13, 6, 4, 7, 2, 18, 10, 4, 9, 5, 13, 8, 1, 8, 3, 5, 5, 12, 5, 12, 11, 6, 17, 15, 25, 9, 14, 16, 9, 28, 16, 1, 18, 12, 6, 11, 6, 4, 6, 5, 1, 12, 9, 3, 8, 4, 2, 24, 11, 23, 2, 8, 8, 7, 9, 23, 7, 11, 12, 7, 5, 9, 11, 39, 18, 7, 3, 22, 14, 3, 6, 12, 13, 7, 7, 8, 11, 13, 8, 14, 10, 8, 16, 9, 13, 13, 5, 16, 22, 17, 4, 3, 2, 8, 20, 13, 2, 9, 5, 5, 13, 9, 13, 14, 13, 5, 10, 20, 4, 6, 13, 6, 15, 9, 9, 6, 4, 12, 1, 12, 8, 2, 8, 6, 7, 12, 3, 18, 14, 4, 13, 13, 13, 17, 16, 12, 11, 8, 6, 10, 11, 4, 10, 13, 15, 12, 8, 4, 5, 7, 7, 5, 8, 19, 6, 19, 11, 8, 2, 5, 7, 19, 5, 5, 4, 9, 13, 7, 3, 8, 9, 5, 7, 14, 13, 9, 8, 13, 9, 2, 10, 21, 15, 7, 14, 3, 4, 8, 7, 8, 4, 7, 5, 20, 11, 7, 7, 9, 11, 8, 10, 5, 19, 2, 14, 58, 26, 13, 2, 8, 10, 8, 12, 18, 5, 4, 7, 11, 17, 8, 14, 14, 26, 13, 6, 2, 4, 14, 17, 13, 6, 5, 12, 22, 6, 2, 4, 3, 11, 15, 7, 7, 8, 5, 12, 4, 7, 5, 2, 5, 4, 26, 10, 59, 15, 9, 2, 14, 8, 14, 6, 8, 4, 2, 28, 1, 3, 6, 9, 9, 8, 16, 7, 3, 5, 11, 12, 8, 9, 14, 47, 2, 10, 16, 5, 32, 19, 13, 12, 12, 9, 6, 10, 12, 4, 18, 6, 7, 11, 5, 6, 6, 20, 17, 9, 11, 11, 2, 4, 10, 4, 4, 13, 14, 11, 1, 9, 8, 12, 9, 3, 8, 5, 7, 30, 5, 9, 5, 15, 1, 17, 2, 3, 12, 30, 6, 17, 20, 3, 7, 10, 13, 11, 16, 19, 2, 13, 22, 6, 3, 12, 12, 3, 12, 12, 3, 3, 26, 8, 13, 10, 15, 11, 17, 6, 22, 6, 4, 6, 13, 7, 24, 14, 11, 6, 25, 11, 4, 5, 10, 5, 10, 9, 8, 21, 8, 9, 8, 6, 5, 1, 19, 10, 11, 3, 6, 16, 10, 3, 15, 8, 16, 5, 17, 5, 12, 8, 12, 9, 6, 5, 3, 41, 3, 17, 16, 7, 11, 3, 9, 22, 4, 4, 24, 6, 12, 10, 16, 21, 10, 8, 13, 14, 31, 8, 7, 11, 5, 19, 9, 22, 11, 3, 8, 4, 26, 14, 7, 3, 15, 17, 3, 3, 24, 14, 9, 7, 4, 7, 18, 12, 20, 11, 6, 9, 28, 3, 4, 10, 14, 11, 20, 37, 2, 10, 8, 35, 7, 14, 14, 5, 27, 9, 6, 26, 6, 9, 11, 17, 16, 7, 14, 25, 6, 4, 18, 14, 17, 5, 9, 7, 6, 6, 6, 2, 6, 6, 14, 6, 5, 7, 2, 7, 12, 9, 1, 6, 19, 7, 15, 17, 12, 3, 28, 3, 11, 7, 11, 29, 18, 23, 18, 7, 5, 8, 6, 10, 13, 14, 7, 7, 11, 6, 28, 17, 17, 8, 18, 10, 7, 4, 26, 8, 8, 13, 14, 4, 8, 43, 9, 8, 13, 5, 13, 0, 11, 7, 12, 2, 20, 8, 4, 19, 11, 20, 12, 3, 8, 5, 13, 2, 5, 15, 3, 10, 7, 17, 20, 18, 15, 5, 13, 15, 8, 9, 11, 6, 5, 1, 12, 7, 10, 7, 20, 9, 36, 10, 15, 13, 6, 13, 7, 7, 6, 17, 8, 11, 9, 4, 9, 8, 24, 14, 13, 6, 4, 5, 23, 1, 8, 7, 9, 8, 6, 7, 8, 4, 21, 4, 5, 6, 7, 4, 27, 27, 18, 8, 11, 8, 7, 3, 14, 14, 16, 19, 11, 13, 5, 5, 9, 11, 8, 14, 22, 4, 11, 7, 12, 3, 5, 11, 7, 13, 8, 10, 9, 8, 3, 17, 20, 9, 9, 16, 13, 10, 10, 14, 18, 10, 4, 10, 1, 2, 4, 4, 0, 15, 10, 12, 13, 3, 4, 5, 16, 11, 7, 10, 13, 6, 14, 10, 4, 7, 4, 7, 1, 5, 1, 8, 5, 12, 5, 13, 7, 8, 6, 9, 16, 7, 13, 3, 7, 7, 3, 12, 12, 17, 12, 2, 6, 3, 12, 6, 6, 13, 4, 13, 16, 6, 6, 16, 17, 10, 9, 11, 4, 16, 16, 4, 15, 5, 9, 4, 17, 5, 6, 13, 14, 14, 13, 16, 6, 24, 11, 5, 10, 12, 41, 7, 25, 18, 14, 8, 15, 3, 11, 12, 9, 5, 2, 7, 14, 9, 10, 6, 7, 13, 11, 2, 8, 11, 17, 4, 3, 9, 1, 3, 9, 11, 12, 3, 8, 5, 14, 22, 7, 23, 16, 3, 12, 6, 0, 2, 21, 11, 20, 23, 1, 6, 10, 6, 10, 10, 8, 17, 13, 9, 14, 16, 2, 22, 14, 34, 22, 10, 6, 5, 11, 9, 1, 10, 4, 12, 4, 19, 8, 17, 17, 35, 15, 25, 9, 26, 4, 5, 8, 11, 19, 20, 8, 10, 13, 7, 10, 18, 24, 14, 10, 10, 8, 8, 17, 8, 3, 8, 12, 15, 16, 3, 12, 10, 9, 8, 18, 15, 7, 9, 35, 7, 4, 10, 5, 12, 7, 25, 5, 18, 38, 12, 14, 17, 3, 8, 5, 15, 3, 6, 18, 18, 16, 25, 5, 21, 4, 11, 7, 7, 10, 9, 7, 24, 1, 16, 15, 3, 1, 6, 25, 9, 4, 3, 23, 15, 34, 4, 27, 9, 23, 14, 16, 3, 21, 2, 9, 9, 18, 9, 10, 4, 16, 8, 9, 5, 10, 3, 14, 11, 9, 5, 5, 5, 6, 5, 3, 29, 6, 16, 6, 10, 8, 13, 10, 21, 4, 14, 7, 14, 7, 10, 8, 9, 26, 6, 8, 7, 2, 5, 6, 9, 14, 5, 10, 7, 6, 9, 9, 10, 6, 5, 19, 9, 16, 13, 5, 7, 18, 9, 12, 12, 5, 16, 6, 12, 1, 14, 8, 5, 16, 13, 12, 4, 6, 4, 3, 9, 5, 20, 4, 19, 10, 11, 16, 28, 7, 3, 7, 46, 16, 7, 28, 15, 13, 29, 11, 20, 17, 9, 7, 6, 3, 4, 14, 19, 20, 10, 19, 14, 19, 7, 14, 5, 7, 5, 1, 16, 27, 5, 13, 4, 5, 11, 15, 8, 8, 23, 6, 9, 3, 10, 29, 11, 17, 5, 5, 4, 20, 14, 3, 4, 12, 5, 5, 8, 1, 10, 5, 6, 8, 6, 6, 8, 10, 14, 5, 7, 26, 12, 3, 11, 26, 6, 4, 17, 14, 29, 5, 17, 14, 14, 25, 6, 6, 9, 29, 26, 10, 14, 2, 6, 6, 14, 8, 9, 20, 6, 10, 2, 7, 2, 6, 3, 4, 13, 11, 4, 25, 4, 12, 7, 17, 6, 11, 7, 7, 15, 10, 4, 33, 13, 12, 2, 3, 19, 9, 9, 6, 29, 23, 7, 12, 6, 17, 6, 10, 6, 1, 2, 5, 7, 1, 2, 4, 8, 9, 22, 4, 8, 25, 10, 23, 8, 29, 28, 5, 8, 35, 4, 2, 17, 10, 20, 9, 6, 52, 4, 18, 15, 23, 11, 6, 27, 2, 9, 13, 12, 3, 9, 17, 9, 6, 8, 3, 9, 6, 9, 9, 6, 17, 19, 13, 5, 1, 10, 11, 13, 17, 5, 7, 17, 6, 4, 17, 12, 9, 14, 9, 8, 14, 9, 6, 20, 5, 13, 7, 13, 4, 28, 10, 11, 10, 5, 3, 7, 16, 13, 7, 15, 6, 5, 15, 43, 13, 25, 9, 4, 14, 8, 9, 19, 5, 10, 11, 20, 11, 7, 16, 18, 8, 14, 9, 5, 31, 1, 3, 4, 14, 17, 8, 18, 12, 8, 5, 25, 2, 13, 16, 4, 7, 15, 7, 13, 4, 9, 20, 5, 10, 12, 23, 13, 5, 11, 33, 5, 11, 15, 7, 16, 20, 24, 8, 15, 19, 13, 23, 15, 7, 14, 7, 20, 3, 28, 13, 6, 6, 2, 9, 3, 1, 20, 8, 31, 3, 11, 9, 4, 3, 27, 4, 9, 12, 6, 27, 7, 13, 6, 17, 13, 7, 6, 4, 48, 5, 14, 9, 11, 10, 4, 9, 21, 24, 8, 28, 14, 18, 24, 3, 28, 10, 5, 9, 2, 7, 13, 23, 11, 13, 18, 9, 21, 10, 28, 13, 4, 11, 12, 5, 21, 2, 7, 9, 17, 34, 8, 4, 13, 6, 2, 7, 19, 20, 25, 37, 10, 5, 15, 5, 2, 9, 24, 16, 16, 4, 8, 6, 10, 12, 5, 15, 36, 3, 14, 21, 17, 0, 6, 0, 2, 10, 14, 5, 7, 13, 15, 10, 6, 3, 5, 5, 15, 2, 4, 7, 15, 7, 11, 4, 14, 6, 22, 12, 2, 2, 9, 0, 5, 4, 3, 10, 7, 2, 3, 6, 4, 4, 11, 2, 15, 7, 17, 1, 4, 6, 17, 3, 0, 6, 3, 11, 8, 14, 6, 10, 5, 12, 5, 16, 23, 3, 5, 5, 3, 2, 8, 12, 13, 7, 7, 5, 0, 5, 1, 13, 5, 12, 8, 15, 8, 2, 5, 14, 5, 11, 1, 19, 6, 9, 3, 16, 3, 2, 4, 2, 14, 8, 7, 5, 6, 7, 2, 10, 8, 11, 10, 8, 3, 4, 12, 10, 11, 4, 2, 9, 10, 5, 4, 12, 2, 9, 9, 2, 5, 15, 11, 7, 7, 5, 7, 2, 16, 5, 6, 13, 4, 13, 2, 2, 24, 11, 18, 9, 4, 14, 15, 20, 8, 21, 13, 19, 20, 8, 10, 8, 4, 18, 15, 5, 8, 14, 2, 14, 13, 6, 4, 20, 7, 6, 20, 9, 10, 16, 14, 16, 9, 2, 13, 27, 1, 3, 8, 12, 3, 5, 15, 2, 9, 4, 1, 7, 21, 5, 12, 13, 5, 9, 7, 8, 4, 5, 3, 2, 6, 12, 9, 0, 0, 8, 33, 10, 11, 23, 12, 3, 13, 12, 18, 11, 7, 5, 23, 14, 5, 7, 7, 10, 4, 4, 15, 10, 4, 13, 4, 11, 8, 13, 14, 1, 4, 8, 5, 3, 7, 5, 21, 7, 3, 3, 4, 8, 6, 4, 9, 7, 0, 26, 7, 15, 21, 11, 14, 4, 12, 10, 15, 11, 16, 8, 20, 17, 9, 14, 7, 10, 22, 17, 2, 8, 6, 9, 6, 8, 22, 12, 3, 19, 14, 4, 3, 10, 9, 5, 15, 44, 6, 10, 11, 27, 9, 14, 6, 2, 22, 4, 6, 8, 14, 3, 6, 8, 10, 10, 11, 4, 7, 3, 2, 1, 9, 15, 19, 1, 10, 32, 6, 5, 2, 4, 4, 13, 1, 24, 19, 23, 9, 13, 4, 14, 19, 3, 1, 9, 4, 12, 13, 15, 9, 37, 10, 12, 6, 6, 1, 10, 6, 3, 9, 6, 18, 14, 3, 3, 8, 17, 6, 9, 37, 7, 9, 6, 16, 8, 1, 13, 11, 21, 4, 12, 2, 3, 7, 18, 4, 8, 6, 14, 13, 16, 2, 19, 11, 13, 4, 12, 16, 5, 3, 4, 19, 4, 23, 1, 22, 10, 14, 13, 8, 6, 20, 15, 14, 6, 7, 10, 6, 13, 17, 7, 20, 1, 13, 4, 12, 6, 5, 25, 17, 6, 8, 12, 10, 8, 11, 3, 13, 5, 12, 16, 4, 8, 21, 6, 7, 3, 8, 14, 4, 6, 10, 7, 10, 2, 13, 3, 13, 11, 11, 5, 5, 14, 7, 7, 12, 15, 2, 9, 9, 17, 10, 18, 5, 7, 10, 5, 5, 8, 6, 18, 3, 18, 5, 16, 4, 8, 6, 11, 4, 3, 16, 24, 6, 7, 11, 6, 7, 8, 11, 1, 6, 5, 3, 6, 6, 1, 13, 8, 3, 0, 3, 1, 5, 3, 12, 10, 5, 17, 4, 0, 4, 6, 6, 7, 9, 7, 14, 8, 9, 6, 62, 6, 15, 0, 13, 13, 1, 3, 6, 7, 8, 5, 14, 5, 10, 3, 4, 13, 4, 14, 28, 9, 10, 6, 11, 7, 6, 4, 18, 8, 11, 9, 8, 14, 3, 0, 12, 6, 3, 8, 1, 10, 29, 14, 14, 1, 13, 16, 8, 12, 8, 37, 4, 10, 6, 18, 16, 4, 25, 20, 7, 13, 3, 18, 12, 5, 17, 13, 6, 11, 7, 10, 10, 3, 18, 22, 19, 7, 18, 9, 23, 11, 11, 9, 8, 23, 9, 7, 11, 3, 6, 11, 11, 11, 10, 9, 4, 10, 3, 10, 1, 5, 7, 10, 4, 12, 14, 15, 14, 7, 35, 14, 11, 8, 16, 11, 10, 10, 13, 6, 8, 16, 10, 30, 6, 7, 16, 6, 14, 7, 14, 4, 8, 21, 14, 7, 17, 4, 12, 7, 22, 9, 5, 8, 23, 16, 6, 5, 5, 7, 13, 7, 8, 7, 4, 10, 7, 4, 4, 9, 3, 10, 16, 4, 13, 10, 7, 9, 11, 4, 3, 12, 11, 6, 8, 16, 9, 10, 27, 7, 8, 8, 12, 7, 6, 34, 8, 16, 9, 8, 5, 4, 29, 2, 19, 4, 21, 5, 10, 7, 9, 11, 4, 8, 9, 2, 4, 8, 6, 24, 23, 7, 20, 17, 36, 8, 5, 11, 7, 15, 17, 7, 13, 7, 10, 9, 10, 21, 8, 2, 6, 17, 4, 7, 5, 21, 21, 22, 6, 10, 9, 10, 22, 15, 8, 5, 6, 30, 6, 13, 5, 9, 3, 7, 29, 22, 3, 10, 8, 2, 10, 10, 14, 7, 7, 4, 4, 2]