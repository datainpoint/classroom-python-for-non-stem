# Python 的五十道練習：資料科學的敲門磚

> 使用函數組織程式碼

## 計算圓面積

定義函數 `calculate_circle_area()` 能夠對輸入的半徑計算圓面積，我們使用圓周率 $\pi = 3.14$

\begin{equation}
\text{Circle area} = \pi r^2
\end{equation}


- 運用數值運算符。
- 將預期輸出寫在 `return` 之後。

## 計算圓柱體積

定義函數 `calculate_cylinder_volume()` 能夠對輸入的半徑、高度計算圓柱體積，我們使用圓周率 $\pi = 3.14$

\begin{equation}
\text{Cylinder volume} = \pi r^2 h
\end{equation}


- 運用數值運算符。
- 使用 `calculate_circle_area()` 函數。
- 將預期輸出寫在 `return` 

## 因數個數

定義函數 `count_number_of_divisors()` 能夠回傳輸入整數的因數個數。

- 運用迴圈走訪所有可能因數。
- 運用條件敘述是否為因數來計數。
- 將預期輸出寫在 `return` 之後。

## 是否為質數

定義函數 `is_prime()` 能夠回傳輸入正整數是否為質數的判斷。

來源：<https://en.wikipedia.org/wiki/Prime_number>

- 使用 `count_number_of_divisors()` 函數。
- 運用條件敘述依據因數個數是否為 2 判斷。
- 將預期輸出寫在 `return` 

## 彈性參數是否為質數

定義函數 `is_args_prime()` 能夠回傳輸入的彈性參數是否為質數的判斷。

- 運用彈性參數 `*args`
- 使用 `is_prime()` 函數。
- 將預期輸出寫在 `return` 之後。