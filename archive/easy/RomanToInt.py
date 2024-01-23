import pretty_errors

class Solution():
    def romanToInt(self, s: str) -> int:
        symbol_value = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000
                        }
        prev_value = 0
        total = 0
        
        for i in reversed(s):
            print(i)
            current_value = symbol_value[i]
            # If the previous value is less than the current value, subtract it
            print(f"Prev_value: {prev_value}. Current value: {current_value}")
            if prev_value > current_value:
                total -= current_value
                print(f"Total (substraction): {total}\n")
            else:
                total += current_value
                print(f"Total (addition): {total}\n")


            prev_value = current_value

        return total



# Create an instance of the Solution class
solution = Solution()

result = solution.romanToInt("MCMXCIV")

print(f"\nResult: {result}")