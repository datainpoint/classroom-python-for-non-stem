# Python 的五十道練習：資料科學的敲門磚

> 資料科學模組 NumPy 入門

## 前十個質數

定義函數 `create_first_ten_primes_array()` 回傳一個外型為 `(10,)`、儲存了前十個質數的 `ndarray`

- 使用 `np.array()` 函數。
- 將預期輸出寫在 `return` 之後。

## 前十個偶數

定義函數 `create_first_ten_evens_array()` 回傳一個外型為 `(10,)`、儲存了前十個偶數的 `ndarray`

- 使用 `np.arange()` 函數。
- 將預期輸出寫在 `return` 之後。

## 方塊矩陣（Square matrix）

定義函數 `create_a_square_matrix()` 回傳外型為 `(n, n)`、元素皆為 `fill_int` 的 `ndarray`

- 使用 `np.full()` 函數。
- 將預期輸出寫在 `return` 之後。

## 將數個距離由公里轉換英里

定義函數 `convert_kilometers_to_miles()` 能夠將數個單位為公里的距離轉換為英里。

\begin{equation}
1 \; \text{km} = 0.62137 \; \text{mile}
\end{equation}

- 運用 `ndarray` 的 Elementwise 特性。
- 將預期輸出寫在 `return` 之後。

## 對角矩陣

定義函數 `create_a_diagonal_matrix()` 回傳一個外型為 `(n, n)`、對角線上的數字為 `fill_int`、其餘數字為 0 的 `ndarray`

- 使用 `np.eye()` 函數。
- 運用 `ndarray` 的 Elementwise 特性。
- 將預期輸出寫在 `return` 之後。