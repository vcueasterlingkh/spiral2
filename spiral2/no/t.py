def foo():
    print("bar")
    # implicitly return None


bar2 = foo  # What happens here?
bar2()

foo()
print("Next is normal")

# How is that different from:
# bar = foo()
# print(bar)
