'''
Дана строка `s` и число `k`. Подсчитать количество подстрок длины `k`, в которых все символы различны.
'''

from collections import Counter

def input_s_k():
    s = input('s = ')
    k = int(input('k = '))

    return s, k
def counter_window(s, k):
    if len(s) < k:
        return None
    
    left = 0
    right = k
    result = 0

    while right != len(s) + 1:
        window = s[left:right]
        cnt = Counter(window)
        flag = 0
        for ch in cnt:
            if cnt[ch] != 1:
                flag = 1
        if not flag:
            result += 1

        left += 1
        right += 1

    return result

def main():
    s, k = input_s_k();
    #s = "havefunonleetcode"
    #k = 5 
    print(counter_window(s, k))

if __name__ == "__main__":
    main()
