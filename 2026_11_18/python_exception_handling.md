# Python 例外處理教學講義（Exception Handling）

本教學由淺入深，帶你完整掌握 Python 的錯誤與例外處理機制，寫出強健（Robust）、不易崩潰的程式碼。

---

## 目錄
1. [什麼是例外？為什麼需要處理？](#1-什麼是例外為什麼需要處理)
2. [基礎語法：try 與 except](#2-基礎語法try-與-except)
3. [捕捉特定例外與多個例外](#3-捕捉特定例外與多個例外)
4. [取得錯誤詳細資訊：as e](#4-取得錯誤詳細資訊as-e)
5. [完整結構：else 與 finally](#5-完整結構else-與-finally)
6. [主動引發例外：raise](#6-主動引發例外raise)
7. [進階：自訂例外（Custom Exception）](#7-進階自訂例外custom-exception)
8. [實戰演練：使用者註冊系統驗證](#8-實戰演練使用者註冊系統驗證)
9. [常見例外速查表與最佳實踐](#9-常見例外速查表與最佳實踐)

---

## 1. 什麼是例外？為什麼需要處理？

在寫程式時，通常會遇到兩種錯誤：
1. **語法錯誤（SyntaxError）**：程式在執行前解析階段就失敗（例如漏了冒號、括號沒對齊）。
2. **執行期錯誤 / 例外（Exception / Runtime Error）**：語法完全正確，但在程式執行到某一行時發生意外情況導致程式中斷。

### 常見執行期錯誤範例
```python
# 1. ZeroDivisionError: 除以零
result = 10 / 0

# 2. ValueError: 型態轉換失敗
number = int("abc")

# 3. IndexError: 索引超出清單範圍
fruits = ["apple", "banana"]
print(fruits[5])

# 4. KeyError: 字典中找不到對應鍵
person = {"name": "Alice"}
print(person["age"])
```

> **為什麼需要例外處理？**  
> 如果沒有處理例外，程式會立即終止並拋出 Traceback（錯誤追蹤訊息）。在正式系統或使用者介面中，我們希望即使出錯也能優雅應對（例如提示使用者重新輸入、記錄錯誤日誌），而不是直接崩潰閃退。

---

## 2. 基礎語法：try 與 except

最基礎的結構是 `try...except`：
- **`try` 區塊**：放置「可能會出錯」的程式碼。
- **`except` 區塊**：當 `try` 區塊發生錯誤時，立即跳入執行的備用程式碼。

### 範例 1：避免程式因錯誤而崩潰
```python
print("--- 程式開始 ---")

try:
    number = int(input("請輸入一個整數: "))
    result = 100 / number
    print(f"100 除以 {number} 的結果是: {result}")
except:
    print("發生錯誤！請確認輸入是否正確。")

print("--- 程式結束（順利執行到最後）---")
```

> 💡 **觀察**：即便使用者輸入 `0` 或 `"abc"`，程式不會閃退，而是印出錯誤提示後繼續執行後續流程。

---

## 3. 捕捉特定例外與多個例外

不指定任何型態的 `except:` 雖然方便，但會把所有錯誤一網打盡（包括打錯變數名稱的 `NameError`），容易掩蓋真正的 bug。**最佳做法是明確指定要捕捉的例外型態**。

### 範例 2：分開處理不同類型的錯誤
```python
try:
    dividend = int(input("請輸入被除數: "))
    divisor = int(input("請輸入除數: "))
    result = dividend / divisor
    print(f"結果: {result}")
except ValueError:
    print("【錯誤】輸入格式錯誤！請務必輸入阿拉伯數字。")
except ZeroDivisionError:
    print("【錯誤】除數不能為 0！")
```

### 範例 3：將多個相同處理方式的例外合併捕捉
```python
try:
    data = [10, 20, 30]
    idx = int(input("請輸入要查詢的索引 (0~2): "))
    print(f"數值為: {data[idx]}")
except (ValueError, IndexError):
    print("【錯誤】請輸入有效的整數索引，且範圍須在 0 到 2 之間。")
```

---

## 4. 取得錯誤詳細資訊：as e

透過 `except ExceptionType as 變數名:`，可以取得 Python 原生的錯誤物件與錯誤說明文字。

### 範例 4：印出系統內建的錯誤訊息
```python
try:
    with open("not_found_file.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError as err:
    print(f"捕捉到錯誤: {type(err).__name__}")
    print(f"系統錯誤描述: {err}")
```
**輸出範例：**
```text
捕捉到錯誤: FileNotFoundError
系統錯誤描述: [Errno 2] No such file or directory: 'not_found_file.txt'
```

---

## 5. 完整結構：else 與 finally

Python 的例外處理具備完整的四部曲：
```text
try      -> 嘗試執行主要程式碼
except   -> 發生錯誤時執行
else     -> 沒有發生任何錯誤時執行
finally  -> 無論成功或出錯，最後一定會執行
```

### 流程對照表
| 關鍵字 | 執行時機 | 常見用途 |
| :--- | :--- | :--- |
| `try` | 每次必進 | 放置可能失敗的操作 |
| `except` | **有發生錯誤**時 | 錯誤處理、容錯降級、日誌紀錄 |
| `else` | **完全無錯誤**時 | 成功後的接續操作（避免混在 try 造成誤捕） |
| `finally` | **不管有無錯誤都執行** | 清理資源、關閉檔案、釋放連線 |

### 範例 5：四部曲完整展示
```python
def safe_divide(a, b):
    print(f"\n[計算開始] a = {a}, b = {b}")
    try:
        result = a / b
    except ZeroDivisionError:
        print("  -> except: 除數不可為零！")
    else:
        print(f"  -> else: 計算成功，結果為 {result}")
    finally:
        print("  -> finally: 本次計算流程結束（釋放資源）。")

safe_divide(10, 2)  # 成功案例
safe_divide(10, 0)  # 失敗案例
```

**輸出結果：**
```text
[計算開始] a = 10, b = 2
  -> else: 計算成功，結果為 5.0
  -> finally: 本次計算流程結束（釋放資源）。

[計算開始] a = 10, b = 0
  -> except: 除數不可為零！
  -> finally: 本次計算流程結束（釋放資源）。
```

---

## 6. 主動引發例外：raise

除了被動接收 Python 拋出的錯誤，我們也可以依據業務邏輯，在條件不合符時**主動拋出例外**。

### 範例 6：資料驗證時主動 raise
```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年齡必須是整數！")
    if age < 0 or age > 130:
        raise ValueError(f"不合常理的年齡數值: {age}，必須介於 0 到 130 歲。")
    print(f"年齡設定成功: {age} 歲")

try:
    set_age("十八歲")
except (TypeError, ValueError) as e:
    print(f"驗證失敗: {e}")

try:
    set_age(-5)
except (TypeError, ValueError) as e:
    print(f"驗證失敗: {e}")
```

### 範例 7：重新引發例外（Re-raising）
有時在 `except` 中處理完部分工作（例如記錄 log）後，仍希望把例外往外拋給上一層調用者處理：
```python
def process_data(data):
    try:
        return data["score"] * 2
    except KeyError:
        print("[Log] 記錄：找不到 score 欄位，準備重新拋出例外！")
        raise  # 不帶參數直接寫 raise，會原封不動往外拋出剛剛捕捉到的例外
```

---

## 7. 進階：自訂例外（Custom Exception）

在大型專案或模組開發時，內建的 `ValueError` 等往往無法精準表達領域概念。透過繼承 Python 內建的 `Exception` 類別，可以定義專屬的例外類型。

### 範例 8：銀行帳戶自訂例外
```python
# 1. 定義自訂例外類別（繼承自 Exception）
class BankError(Exception):
    """銀行系統基礎例外"""
    pass

class InsufficientBalanceError(BankError):
    """餘額不足例外"""
    def __init__(self, current_balance, withdraw_amount):
        super().__init__(f"提款失敗！目前餘額 ${current_balance}，不足以提領 ${withdraw_amount}。")
        self.current_balance = current_balance
        self.withdraw_amount = withdraw_amount


# 2. 模擬銀行帳戶
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("提款金額必須大於 0")
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        print(f"[{self.owner}] 提款 ${amount} 成功，剩餘餘額: ${self.balance}")


# 3. 測試呼叫
account = BankAccount("小明", 1000)

try:
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print(f"自訂例外觸發: {e}")
    print(f"差額為: ${e.withdraw_amount - e.current_balance}")
```

---

## 8. 實戰演練：使用者註冊系統驗證

結合 `try...except...else...finally`、`raise` 與自訂例外的綜合實戰。

```python
# 定義自訂驗證例外
class ValidationError(Exception):
    pass

class PasswordTooShortError(ValidationError):
    pass

class InvalidEmailError(ValidationError):
    pass


def register_user(username, email, password):
    print(f"\n--- 開始註冊流程: {username} ---")
    try:
        # 帳號檢查
        if not username.strip():
            raise ValidationError("使用者名稱不能為空。")
            
        # Email 檢查
        if "@" not in email or "." not in email:
            raise InvalidEmailError(f"Email 格式不正確: '{email}'")
            
        # 密碼長度檢查
        if len(password) < 8:
            raise PasswordTooShortError(f"密碼長度不足（需至少 8 碼，目前 {len(password)} 碼）。")
            
    except ValidationError as err:
        print(f"[註冊失敗] 原因: {err}")
        return False
    else:
        print(f"[註冊成功] 歡迎使用者 {username} 加入系統！")
        return True
    finally:
        print("[系統訊息] 註冊驗證流程結束，寫入稽核紀錄。")


# 測試不同情境
register_user("", "test@example.com", "12345678")     # 名稱空白
register_user("Alice", "alice_gmail.com", "12345678") # Email 格式錯誤
register_user("Bob", "bob@example.com", "12345")      # 密碼太短
register_user("Charlie", "charlie@gmail.com", "secret2026") # 成功
```

---

## 9. 常見例外速查表與最佳實踐

### 常見例外速查表
| 例外名稱 | 發生情境 | 範例 |
| :--- | :--- | :--- |
| `ZeroDivisionError` | 任何數除以 0 | `10 / 0` |
| `ValueError` | 傳入數值正確型別但內容不合規格 | `int("xyz")` |
| `TypeError` | 型別不相容的運算或傳參 | `"2" + 2` |
| `IndexError` | 序列索引超出有效範圍 | `[1, 2][5]` |
| `KeyError` | 字典查找不存在的鍵 | `{"a": 1}["b"]` |
| `FileNotFoundError` | 找不到指定的檔案路徑 | `open("ghost.txt")` |
| `AttributeError` | 物件沒有該屬性或方法 | `"hello".push()` |
| `StopIteration` | 迭代器已無下一個元素可取 | `next(iter([]))` |

### 例外處理最佳實踐（Best Practices）

1. **避免裸寫 `except:` 或 `except Exception: pass`**
   - 這樣會「靜默吃掉」所有錯誤，甚至讓鍵盤中斷（`KeyboardInterrupt`）無法停下程式，極度難以除錯。
2. **捕捉精準的例外型態**
   - 只捕捉預期可能發生且你能夠處理的例外（例如檔案不存在、使用者輸入格式錯誤）。
3. **保持 `try` 區塊簡短**
   - 只把「真正會產生例外的那幾行」放入 `try` 中，其餘安全邏輯放在 `else` 或 `try` 外部，避免意外捕捉到不該抓的錯誤。
4. **善用 `finally` 或 `with` 釋放資源**
   - 開啟檔案、資料庫連線、網路通訊時，務必確保資源即使出錯也能正確關閉。
