from patterns.SlidingWindow import SlidingWindowSolutions



if __name__ == "__main__":
    sliding_window = SlidingWindowSolutions()
    #ans = sliding_window.findMaxAverage()
    ans = sliding_window.minSubArrayLen()
    print(ans)