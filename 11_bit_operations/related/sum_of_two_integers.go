func getSum(a, b int) int {
	for b != 0 {
		carry := uint(a&b) << 1
		a ^= b
		b = int(carry)
	}
	return a
}

// 在 Python 的实现中，因为 Python 的整数类型为是无限长的，所以无论怎样左移位都不会溢出。因此，我们需要对 Python 中的整数进行额外处理，以模拟用补码表示的 32 位有符号整数类型。具体地，我们将整数对 2
// 32
//   取模，从而使第 33 位及更高位均为 0；因为此时最终结果为用补码表示的包含符号位的 32 位整数，所以我们还需要再次将其换算为 Python 的整数。

// MASK1 = 4294967296  # 2^32
// MASK2 = 2147483648  # 2^31
// MASK3 = 2147483647  # 2^31-1

// class Solution:
//     def getSum(self, a: int, b: int) -> int:
//         a %= MASK1
//         b %= MASK1
//         while b != 0:
//             carry = ((a & b) << 1) % MASK1
//             a = (a ^ b) % MASK1
//             b = carry
//         if a & MASK2:  # 负数
//             return ~((a ^ MASK2) ^ MASK3)
//         else:  # 正数
//             return a
