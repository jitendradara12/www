+++
date = '2026-05-31T23:13:27+05:30'
title = 'Solving Leetcode'
banner = '/logos/leetcode.svg'
+++

Leetcode is _mostly_ boring and not fun. But not always. Especially, when you have solved over 400 of these problems.
The most fun ones made me write the most bizarre of the solutions.

---

## 273. [Integer to English Words](https://leetcode.com/problems/integer-to-english-words)

Looks easy enough but there're a lot of things which needs to to taken in consideration.
Although, my solution here is total ass, It works.

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0: return 'Zero'
        h = {0: '',1: 'One',2: 'Two',3: 'Three',4: 'Four',5: 'Five',6: 'Six',7: 'Seven',8: 'Eight',9: 'Nine',10: 'Ten',11: 'Eleven',12: 'Twelve',13: 'Thirteen',14: 'Fourteen',15: 'Fifteen',16: 'Sixteen',17: 'Seventeen',18: 'Eighteen',19: 'Nineteen',20: 'Twenty',30: 'Thirty',40: 'Forty',50: 'Fifty',60: 'Sixty',70: 'Seventy',80: 'Eighty',90: 'Ninety',100: 'Hundred'}


        def three(n: str):
            if int(n) in h:
                if int(n)==100: return h[1]+' '+h[100]
                return h[int(n)]
            ans = ''
            a = ''

            if n[0]!='0': ans+= h[int(n[0])]+' '+h[100]+' '
            if int(n[1:]) in h:
                a = h[int(n[1:])]
            else:
                a = h[int(n[1])*10]+' '+h[int(n[2])]

            ans += a if a!='Zero' else ""
            return ans

        s = str(num)
        l = len(s)
        if l%3!=0: s = '0'*(3-l%3)+s
        l = len(s)
        sig = l//3
        ans = []

        for i in range(0,l,3):
            this = three(s[i:i+3]).strip()

            if this=='' and sig>1:
                sig-=1
                continue

            if sig>3: this= this+' Billion'
            elif sig==3: this= this+' Million'
            elif sig==2: this= this+' Thousand'

            sig-=1
            ans.append(this)
        return " ".join(ans).strip()
```

---

## 11. [Container With Most Water](https://leetcode.com/problems/container-with-most-water)

This one is a great way to **feel** the pain of maintaining bad legacy code. I mean the legacy code which I wrote 5 minutes ago and don't wanna start from scratch. The code feels haunted. I can definitely write a better solution now but this one should keep me grounded.

```C

#include <math.h>
int maxArea(int* height, int heightSize) {
    int max1 = height[0], max2 = height[heightSize - 1], i1 = 0,
        i2 = heightSize - 1, i, maxwater;
    if (height[i1] < height[i2])
        maxwater = height[i1] * (abs(i1 - i2));
    else
        maxwater = height[i2] * (abs(i1 - i2));

    while (1) {
        if (abs(i1 - i2) == 1) {
            if (height[i1] < height[i2] && maxwater < height[i1])
                maxwater = height[i1];
            else if (height[i2] <= height[i1] && maxwater < height[i2])
                maxwater = height[i2];
            return maxwater;
        }

        if (max2 > max1) {
            i1++;
            if (height[i1] > max1) {
                max1 = height[i1];

                if ((height[i2] * (abs(i1 - i2)) > maxwater &&
                     height[i1] * (abs(i1 - i2)) > maxwater)) {
                    max1 = height[i1];

                    if (height[i1] > height[i2])
                        maxwater = height[i2] * (abs(i1 - i2));
                    else
                        maxwater = height[i1] * (abs(i1 - i2));
                }
            }

        } else {
            i2--;
            if (height[i2] > max2) {
                max2 = height[i2];

                if ((height[i2] * (abs(i1 - i2)) > maxwater &&
                     height[i1] * (abs(i1 - i2)) > maxwater)) {

                    if (height[i2] > height[i1])
                        maxwater = height[i1] * (abs(i1 - i2));
                    else
                        maxwater = height[i2] * (abs(i1 - i2));
                    // maxwater= height[i2] * (abs(i1-i2));
                }
            }
        }
    }
}
```
