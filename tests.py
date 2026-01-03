import intermodule
import test2


x = intermodule.SharedGlobal.set_global("x", 10)
x = intermodule.SharedGlobal.set_global("x", 20)


if intermodule.patch_and_reload_module():
    x += intermodule.SharedGlobal.set_global("y", 50)
    print(x)
    test2.func()
    print(test2.x)
    print(x)
