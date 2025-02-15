
#from flask import Flask
import pydevd_pycharm
#app = Flask(__name__)

# Start debugpy and wait for the debugger to attach
# debugpy.listen(("0.0.0.0", 9000))


#debugpy.wait_for_client()  # Pause execution until debugger attaches
# debugpy.breakpoint()       # Optional: Initial breakpoint

def test():
    g = 12
    h =13
#@app.route('/')
def home():
    print("home called ...")

    print("in hello....")
    return "Hello, Debugging with PyCharm!"

if __name__ == '__main__':
    print("before settrace....")
    #pydevd_pycharm.settrace('host.docker.internal', port=9000, stdoutToServer=True, stderrToServer=True, suspend=False)
    pydevd_pycharm.settrace('host.docker.internal', port=9000, stdoutToServer=True, stderrToServer=True, suspend=False)
    print("after settrace....")
    test()
    #app.run(host='0.0.0.0', port=8000)

