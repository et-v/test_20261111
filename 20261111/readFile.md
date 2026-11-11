# Python 檔案讀取：一步一步練習

這份練習會帶你使用 Python 讀取文字檔。請先把本教材與 `sample.txt` 放在同一個資料夾；範例程式也請在該資料夾執行。

## 開始前

確認資料夾中有以下兩個檔案：

```text
你的資料夾/
├── readFile.md
└── sample.txt
```

`sample.txt` 是本練習提供的範例檔，內容包含中文、英文和多行文字。請不要先修改它，這樣比較容易對照練習結果。

## 第 1 步：開啟檔案並讀取全部內容

`open()` 可以開啟檔案。使用 `"r"` 表示「讀取」模式：

```python
file = open("sample.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print(content)
```

你會看到 `sample.txt` 的全部內容。這裡的 `encoding="utf-8"` 指定文字編碼，讀取含中文的文字檔時很重要。

## 第 2 步：使用 `with` 安全地開啟檔案

上一步需要自己呼叫 `close()`。如果程式中途發生錯誤，可能忘記關閉檔案。更常用的寫法是 `with`：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

離開 `with` 區塊後，Python 會自動關閉檔案。**建議讀取檔案時使用這種寫法。**

注意：`with` 區塊中的程式要縮排（通常是 4 個空格）。

## 第 3 步：一次讀一行

`readline()` 每次讀取一行：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print("第一行：", first_line, end="")
print("第二行：", second_line, end="")
```

行尾通常包含換行字元 `\n`。上例的 `end=""` 是為了避免 `print()` 再額外多印一個換行。

## 第 4 步：用迴圈逐行讀取

檔案很大時，逐行處理通常比一次把全部內容讀進記憶體更合適：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

試著改成加上行號：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}: {line}", end="")
```

`enumerate(..., start=1)` 會同時提供行號和該行內容。

## 第 5 步：讀取後分行處理

`readlines()` 會把每一行放進一個清單：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("總行數：", len(lines))
print("第一行：", lines[0].strip())
```

`.strip()` 會移除字串前後的空白及換行字元。注意：如果檔案是空的，`lines[0]` 會出錯。

## 第 6 步：使用 `pathlib` 組合檔案路徑

前面的範例假設 Python 執行時的目前資料夾正好有 `sample.txt`。如果從其他資料夾執行程式，就可能找不到檔案。

如果你把程式存成 `.py` 檔，並讓它和 `sample.txt` 放在同一個資料夾，可以用 `pathlib` 以程式所在位置組合路徑：

```python
from pathlib import Path

sample_path = Path(__file__).parent / "sample.txt"

with sample_path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

`Path(__file__).parent` 代表目前這個 Python 程式檔所在的資料夾。若是在互動式環境（例如某些 Notebook）執行，可能沒有 `__file__`；此時可先使用 `"sample.txt"`，並確認 Notebook 的目前資料夾有該檔案。

## 第 7 步：處理檔案不存在的情況

檔名拼錯或檔案不在預期位置時，Python 會引發 `FileNotFoundError`。你可以明確提示使用者：

```python
from pathlib import Path

sample_path = Path("sample.txt")

try:
    with sample_path.open("r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print(f"找不到檔案：{sample_path.resolve()}")
else:
    print(content)
```

`try` 中放可能發生錯誤的讀取程式；`except` 則處理指定的錯誤。練習時若遇到 `FileNotFoundError`，先確認檔名、檔案位置，以及程式從哪個資料夾執行。

## 動手練習

請使用提供的 `sample.txt`，自己完成以下任務：

1. 讀取並印出全部內容。
2. 逐行印出內容，並在每行前加上行號。
3. 計算檔案有幾行。
4. 計算文字中 `Python` 出現幾次（提示：`content.count("Python")`）。
5. 只印出含有「檔案」兩個字的行（提示：逐行檢查 `if "檔案" in line:`）。
6. 把檔名改成 `missing.txt`，觀察錯誤訊息；再使用第 7 步的方式處理錯誤。

## 小抄

| 寫法 | 用途 |
|---|---|
| `open("sample.txt", "r", encoding="utf-8")` | 以讀取模式開啟文字檔 |
| `file.read()` | 讀取全部內容 |
| `file.readline()` | 讀取一行 |
| `for line in file:` | 逐行讀取 |
| `file.readlines()` | 讀取所有行並回傳清單 |
| `with ... as file:` | 自動管理檔案開啟與關閉 |
| `line.strip()` | 移除行首、行尾空白與換行 |
| `Path(__file__).parent / "sample.txt"` | 以程式檔位置組合路徑 |

