# LEGB
# - local
# - enclosing
# - global
# - built-in

# global
g = 10
def fn1():
    # enclosed
    e = 8
    def fn2():
        # local
        l = 1
        print(f"Access global {g}.")
        print(f"Access enclosed {e}.")
    fn2()

fn1()
