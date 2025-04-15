# Python 的五十道練習：資料科學的敲門磚

> 使用資料類別運算顯示與判斷

## 轉換公里為英里

定義函數 `convert_km_to_mile()` 能夠將以公里（km）為單位的距離轉換為以英里（mile）為單位的距離。

\begin{equation}
1 \; \text{km} = 0.62137 \; \text{mile}
\end{equation}

- 運用數值運算符。
- 將預期輸出寫在 `return` 之後。

## 轉換華氏為攝氏

定義函數 `convert_fahrenheit_to_celsius()` 能夠將以華氏為單位的溫度轉換為以攝氏為單位的溫度。

\begin{equation}
\text{Celsius}(^{\circ} \text{C}) = (\text{Fahrenheit}(^{\circ} \text{F}) - 32) \times \frac{5}{9}
\end{equation}

- 運用數值運算符。
- 注意數值運算符作用的優先順序。
- 將預期輸出寫在 `return` 之後。

## 計算 BMI

定義函數 `calculate_bmi()` 能夠計算身高（公分）與體重（公斤）換算為身體質量指數（Body Mass Index, BMI）。

\begin{equation}
\text{BMI} = \frac{\text{weight}_{kg}}{\text{height}_{m}^2}
\end{equation}

- 運用數值運算符。
- 注意數值運算符作用的優先順序。
- 將預期輸出寫在 `return` 之後。

## 顯示逗號與兩位小數格式

定義函數 `show_integer_with_commas_and_digits()` 能夠將整數以千分位逗號與兩位浮點數顯示。

- 運用 `str` 的特定顯示格式：f-string 語法。
- 將預期輸出寫在 `return` 之後。

## 轉換 1 美元為其他貨幣

定義函數 `convert_one_usd_to_another_currency()` 能夠將 1 美元與兌換其他貨幣以千分位逗號與兩位浮點數顯示。

- 運用 `str` 的特定顯示格式：f-string 語法。
- 將預期輸出寫在 `return` 之後。