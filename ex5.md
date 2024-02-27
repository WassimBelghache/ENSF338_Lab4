**These approaches are designed to deal with different types of
measurement noise. Think about what happens when we try to time
a program, and which types of issues may result in an incorrect
measurement. Reflect on how the two approaches (timeit and
repeat) attempt to address these issues. Discuss when it is
appropriate to use one or the other.**

When measuring the performance of a program or specific code segments, there are numerous external factors that can influence the execution time, which are unrelated to the code itself. These factors include Python's garbage collection, the specifications of the computer running the code, differences in compilers, and so on. To mitigate the impact of these external factors, both the `timeit()` and `repeat()` functions disable garbage collection to prevent overhead from affecting the measured execution time. Additionally, they repeat the execution of the code snippet (typically one million times by default) to obtain a statistically significant measurement of the code's execution time. In summary, `timeit()` is suitable for quick, single measurements, while `repeat()` is more appropriate when multiple measurements are needed to analyze the variability in execution time.



**Typically, the output of timeit is post-processed to compute some
sort of aggregate statistics. Let’s only consider three: average, min,
and max. Which one is the appropriate statistic to apply to the output
of timeit.timeit()? What is the appropriate statistics to apply to
the output of timeit.repeat()? Discuss why. [0.5 pts]**

When looking at `timeit.timeit()`, the average execution time is what you should really be focusing on, but for `timeit.repeat()`, it's the minimum and maximum stats that matter more. The average time gives you a fair view of how the code performs overall, showing you the usual time it takes to run. Since `timeit()` already runs the code multiple times, it's good for this purpose. On the flip side, `repeat()` is better for seeing the full range of execution times. When you're dealing with specific values, like for best or worst-case scenarios, having a bunch of average times helps you deal with differences and odd results better than just using `timeit()`.