# 中文排版样例

虚构汇报。A、B、C 的文字和顺序相同，只改变段落、强调和列表。D 根据读者反馈组合 B 和 C，保留相同事实，但重新组织措辞和层级，不属于逐字对照。请一次只比较一个版本。

## A

代码修好了，但验证还没有全部通过。已修复 `median()` 的偶数长度计算、`parse()` 的空输入处理，以及 `discount()` 的百分比计算。测试结果为 `4 passed、1 error`。`test_convert_live` 因 `api.rates.invalid` 无法连接而报错；这项问题尚未解决。`legacy.py` 和测试文件没有修改。完整的在线流程尚未验证。下一步是配置可用的测试服务，然后重跑 `python3 -m pytest -q`。

## B

**代码修好了，但验证还没有全部通过。**

已修复 `median()` 的偶数长度计算、`parse()` 的空输入处理，以及 `discount()` 的百分比计算。

测试结果为 `4 passed、1 error`。`test_convert_live` 因 `api.rates.invalid` 无法连接而报错；**这项问题尚未解决。**

`legacy.py` 和测试文件没有修改。完整的在线流程尚未验证。

下一步是配置可用的测试服务，然后重跑 `python3 -m pytest -q`。

## C

代码修好了，但验证还没有全部通过。

- 已修复 `median()` 的偶数长度计算、`parse()` 的空输入处理，以及 `discount()` 的百分比计算。
- 测试结果为 `4 passed、1 error`。`test_convert_live` 因 `api.rates.invalid` 无法连接而报错；这项问题尚未解决。
- `legacy.py` 和测试文件没有修改。完整的在线流程尚未验证。
- 下一步是配置可用的测试服务，然后重跑 `python3 -m pytest -q`。

## D

代码修好了，但**验证还没有全部通过**。

**代码修改**

- `median()`：已修复偶数长度计算。
- `parse()`：已修复空输入处理。
- `discount()`：已修复百分比计算。

`legacy.py` 和测试文件没有修改。

**测试结果** — **4 passed、1 error**。

`test_convert_live` 因 `api.rates.invalid` 无法连接而报错；这项问题尚未解决。完整的在线流程尚未验证。

**下一步** — **配置可用的测试服务**，然后重跑：

```sh
python3 -m pytest -q
```
