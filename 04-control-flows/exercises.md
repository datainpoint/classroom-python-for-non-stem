# Python 的五十道練習：資料科學的敲門磚

> 使用流程控制管理程式區塊的執行

## 判斷 BMI 分類

定義函數 `find_bmi_category()` 能夠將輸入 BMI 值所對應的分類以文字輸出。

|BMI|Category|
|---|--------|
|BMI < 18.5|Underweight|
|18.5 <= BMI < 25|Normal weight|
|25 <= BMI  < 30|Overweight|
|BMI >= 30|Obese|

來源：<https://en.wikipedia.org/wiki/Body_mass_index>

- 運用條件敘述。
- 將預期輸出寫在 `return` 之後。

## 判斷資料類別

定義函數 `check_data_type()` 能夠將輸入的資料類別以 `str` 輸出。

- 運用 `type()` 函數判斷資料類別。
- 運用條件敘述。
- 將預期輸出寫在 `return` 之後。

## 判斷資料結構類別

定義函數 `check_data_structure_type()` 能夠將輸入的資料類別以 `str` 輸出。

- 運用 `type()` 函數判斷資料結構類別。
- 運用條件敘述。
- 將預期輸出寫在 `return` 之後。

## 取出中位元素

定義函數 `retrieve_middle_elements()` 能夠將輸入 `list` 的中位元素取出（奇數長度取出中間元素、偶數長度取出中間的兩個元素）。

- 使用 `len()` 函數得知 `list` 長度。
- 運用條件敘述判斷長度為奇數或者偶數。
- 運用 Indexing/Slicing
- 將預期輸出寫在 `return` 之後。

## 計算中位數

定義函數 `calculate_median()` 能夠計算輸入 `list` 的中位數。

\begin{equation}
Median(x) =
  \begin{cases}
    x[\frac{n-1}{2}]       & \quad \text{if } n \text{ is odd}\\
    \frac{x[\frac{n-2}{2}] + x[\frac{n}{2}]}{2}  & \quad \text{if } n \text{ is even}
  \end{cases} \\
\text{where} \, x= \, \text{ordered list of values in data set} \\
\text{where} \, n= \, \text{number of values in data set}
\end{equation}

來源：<https://en.wikipedia.org/wiki/Median>

- 遞增排序 `list`
- 使用 `len()` 函數得知 `list` 長度。
- 運用條件敘述判斷長度為奇數或者偶數。
- 運用 Indexing/Slicing 計算中位數。
- 將預期輸出寫在 `return` 之後。