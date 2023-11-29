import random


def show(m, side_j, side_i):  # prints matrix in comfortable way
    print("\n")
    for j in range(side_j):
        print("|", end="")
        for i in range(side_i):
            print(f"{m[j][i]:>4}", end=" ")
        print("|", end="\n")


def run_quarter_function(m, part_j, part_i, check, handly=0):
    # B C
    # D E
    # in m(8, 8) part_j can be: [0, 1, 2, 3] , & part_i can be: [4, 5, 6, 7]
    # (--> then it'll be 2nd quarter "C")

    # gets matrix; number of columns, number of elements to change;
    # and "handly" goes for "fill in numbers on your own" (if handly == 1)
    # (defolt handly = 0)
    if check:
        part_j = [n for n in range(check)]
        part_i = [n for n in range(check)]

    if handly:  # if == 1
        print(f"Quarter parameters: columns' indexes - {part_j}, elements' indexes - {part_i}\n\
        Write number ONLY in [-10, 10] interval pls: \n")
        for j in part_j:
            for i in part_i:
                m[j][i] = int(input())
    else:       # if remains 0
        for j in part_j:
            for i in part_i:
                m[j][i] = random.randint(-10, 11)
                # [-10, 10 + 1] - including last
    return m


def Check_part_of_quarter(size, quarter):  #  _____________________
    s = 0  #                                 |  *      2          |
    k_nulls = 0  #                           |     *              |
    summ_od = 0  #                           | 1       *        3 |
    # check 4rth part as it is said in task: |     *   4   *      |
    beg, end = 0, size  #                    |__*______________*__|
    if size % 2 != 0:
        s = 1
    for j in range(size - 1, size // 2 - 1, -1):
        for i in range(beg, end):
            if i % 2 != 0 and quarter[j][i] == 0:  # odd column (i) and element is '0'
                k_nulls += 1
        beg += 1
        end -= 1
    # check 1st part as it is said in task:
    beg, end = 0, size
    for i in range(size // 2 + s):
        for j in range(beg, end):
            if j % 2 != 0:
                summ_od += quarter[j][i]
        beg += 1
        end -= 1
    print(f"\nIn this quater number of nulls = {k_nulls}, sum of numbers = {summ_od}\n")
    if k_nulls > summ_od:
        return 1
    else:
        return 0


def num_multiply(k, m_c, k_j, k_i):  # (for every matrix, like m(x, y))
    m = m_c
    for j in range(k_j):
        for i in range(k_i):
            m[i][j] *= k  # multiplies each element of 'm_c' on exact number 'k'
    return m
# example of using THIS FUNCTION in further code:
# mtx = [ [9, 8, ...], [...] ]
# num_multiply(6, mtx, len(mtx), len(mtx[0]))


def mat_multiply(m1, m2):  # (for every matrixes, like m(a, y) and m(y, b))
    jm1, im1 = len(m1), len(m1[0])
    jm2, im2 = len(m2), len(m2[0])
    s = 0
    if im1 == jm2:
        remade_m = create_matrix(im1, jm2)
        for j in range(jm1):
            for i in range(im2):
                for k in range(jm2):
                    s += m1[j][k] * m2[k][i]
                    remade_m[j][k] = s
                    s = 0
        return remade_m
    else:
        print(f"This matrixes cannot be multiplied : {im1} != {jm2}\n")
        return 0

def create_matrix(i, j):  # copy
    mtx = []
    for n in range(i):
        mtx.append([])
        for m in range(j):
            mtx[-1].append(0)
    return mtx


# MAIN EXAMPLE with m(8, 8):
#                     j                i                  j                i
# B C        B: [0, 1, 2, 3]  &  [0, 1, 2, 3]    C: [0, 1, 2, 3]  &  [4, 5, 6, 7]
# D E        D: [4, 5, 6, 7]  &  [0, 1, 2, 3]    E: [4, 5, 6, 7]  &  [4, 5, 6, 7]

# index 0  1  2  3   4  5  6  7
# 0 [ [0, 0, 0, 0, | 0, 0, 0, 0],
# 1   [0, 0, 0, 0, |  0, 0, 0, 0],
# 2   [0, 0, 0, 0, |  0, 0, 0, 0],
# 3   [0, 0, 0, 0, |  0, 0, 0, 0],
#      - - - - - - - - - - - - -
# 4   [0, 0, 0, 0, |  0, 0, 0, 0],
# 5   [0, 0, 0, 0, |  0, 0, 0, 0],
# 6   [0, 0, 0, 0, |  0, 8, 5, 0],
# 7   [0, 0, 0, 0, |  1, 0, 2, 9] ]


class Quadro_Matrix:
    def __init__(self, m_ray, size, ):
        # generate/write down main information about matrix:
        self.n = size

        if self.n % 2 == 0:
            self.m = m_ray
            self.quarter_size = self.n // 2
            # *example( for m(6, 6) : q_s = 3, for m(8, 8) : q_s = 4 )
        else:
            # if size is odd, adds extra nulls to make it even number
            # in order to devide into equal 4 little matrixes
            self.m = [line.append(0) for line
                      in m_ray] + [0] * (self.n + 1)
            # [ [3, 5, 6],       [ [3, 5, 6, 0],
            #   [0, 9, 2],   ->    [0, 9, 2, 0],
            #   [2, 7, 7] ]        [2, 7, 7, 0],
            #      3*3 :(          [0, 0, 0, 0] ]  4*4 ;)
            self.quarter_size = (self.n + 1) // 2
            self.n += 1

        self.m_T = []  # self.T(self.m)
        self.B, self.C, self.D, self.E = [], [], [], []


    def showAll(self):  # prints matrix in comfortable way
        show(self.m, self.n, self.n)


    def mat_mult(self, an_m):
        # multiplies this object (self.m) with another matrix (an_m)
        return mat_multiply(self.m, an_m)


    def T(self, m_c):  # transpaniruyshiy* method (for m [n x n] only)
        s = 1
        # do not need to count first line(j), so: (1, n)
        # do not need to count last column(i), so: (0, n - 1) /-> s < n-1
        for j in range(1, self.n):
            for i in range(s):
                v = m_c[j][i]
                m_c[j][i] = m_c[i][j]
                m_c[i][j] = v
            s += 1
        self.m_T = m_c
        return m_c


    def get_copy(self):
        copy = []
        for arr in self.m:
            copy.append(arr[:])
        return copy


    def update(self, letter, c=0):
        fill_in = 0
        # B C  (-> see main example with m(8, 8) !!!)
        # D E
        if letter == "B":  #   [0, 1, 2, 3]  &  [0, 1, 2, 3]
            fill_in = int(input("\nB : If you wanna write numbers by yourself choose '1' (else - '0'): "))
            lev, el = [j for j in range(self.quarter_size)], [i for i in range(self.quarter_size)]

            self.m = run_quarter_function(self.m, lev, el, c, fill_in)
            self.B = [self.m[j][:self.quarter_size] for j in lev]

        elif letter == "C":  # [0, 1, 2, 3]  &  [4, 5, 6, 7]
            fill_in = int(input("\nC : If you wanna write numbers by yourself choose '1' (else - '0'): "))
            lev, el = [j for j in range(self.quarter_size)], [i for i in range(self.quarter_size, self.n)]

            self.m = run_quarter_function(self.m, lev, el, c, fill_in)
            self.C = [self.m[j][self.quarter_size:] for j in lev]

        elif letter == "D":  # [4, 5, 6, 7]  &  [0, 1, 2, 3]
            fill_in = int(input("\nD : If you wanna write numbers by yourself choose '1' (else - '0'): "))
            lev, el = [j for j in range(self.quarter_size, self.n)], [i for i in range(self.quarter_size)]

            self.m = run_quarter_function(self.m, lev, el, c, fill_in)
            self.D = [self.m[j][:self.quarter_size] for j in lev]

        elif letter == "E":  # [4, 5, 6, 7]  &  [4, 5, 6, 7]
            fill_in = int(input("\nE : If you wanna write numbers by yourself choose '1' (else - '0'): "))
            lev, el = [j for j in range(self.quarter_size, self.n)], [i for i in range(self.quarter_size, self.n)]

            self.m = run_quarter_function(self.m, lev, el, c, fill_in)
            self.E = [self.m[j][self.quarter_size:] for j in lev]

        else:
            print(f"There is no quarter named '{letter}', try again.")


def quadro_m_subtraction(m1, m2, n):
    for j in range(n):
        for i in range(n):
            m1[j][i] -= m2[j][i]
    return m1


if __name__ == '__main__':
    check = 0
    k, n = map(int, input().split())
    if n % 2 != 0:
        check = n
        n += 1
    m = [[0] * n for x in range(n)]  # null matrix: [ [0, 0, ...], [0, 0, ...], ... ]
    # also the already done matrix can be written and be the first value of class Matrix()
    M_obj = Quadro_Matrix(m, n)

    # to FILL one of the quarter ("B", "C", "D", "E") use 'update' method:
    # letter = input("Choose one of the letter to change this quater: 'B', 'C', 'D', 'E'\n")
    # M_obj.update(letter)
    # wanna update more? dublicate/write the upper code again with your own changes/wishes
    # for example: M_obj.update("E")
    # OR:
    for let in ["B", "C", "D", "E"]:
        M_obj.update(let, check)

    M_obj.showAll()

    size = M_obj.quarter_size
    """
    show(M_obj.B, size, size)
    show(M_obj.C, size, size)
    show(M_obj.D, size, size)
    show(M_obj.E, size, size)
    """

    # checking 4rth and 1st parts as it's said in the task
    res = Check_part_of_quarter(size, M_obj.E)
    F = M_obj.get_copy()

    q_E = [M_obj.E[j] for j in range(size)]
    if res:  # kol_vo '0's > sum   (--> symmetrically 1part <-> 2part of E)
        p = 0
        for j in range(1, size):
            p += 1
            for i in range(p):
                if j + i < size:
                    v = q_E[j][i]
                    q_E[j][i] = q_E[i][j]
                    q_E[i][j] = v
                else:
                    break
        for j in [n for n in range(size, size * 2)]:
            for i in [n for n in range(size, size * 2)]:
                F[j][i] = q_E[j - size][i - size]

    else:  # C <-> E   C: [0, 1, 2, 3] & [4, 5, 6, 7]  E: [4, 5, 6, 7] & [4, 5, 6, 7]
        for j in [n for n in range(size)]:
            for i in [n for n in range(size, size * 2)]:
                F[j][i] = M_obj.E[j][i - size]

        for j in [n for n in range(size, size * 2)]:
            for i in [n for n in range(size, size * 2)]:
                F[j][i] = M_obj.C[j - size][i - size]

    #                first       second
    # --------- k * (A * F) - k * A(t) ----------
    print("F:")
    show(F, n, n)

    print("\nA:")
    M_obj.showAll()

    # (A * F)
    print("A * F :")
    first = M_obj.mat_mult(F)
    show(first, n, n)
    # A(t)
    print("A(t) :")
    M_obj.m_T = M_obj.T(M_obj.m)
    second = M_obj.m_T
    show(second, n, n)

    print("k * (A * F) :")
    m_k1 = num_multiply(k, first, n, n)
    show(m_k1, n, n)
    print("k * A(t) :")
    m_k2 = num_multiply(k, second, n, n)
    show(m_k2, n, n)

    print("!!!result :")
    answer = quadro_m_subtraction(m_k1, m_k2, n)
    show(answer, n, n)