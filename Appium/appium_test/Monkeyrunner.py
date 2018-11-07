
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object

device = MonkeyRunner.waitForConnection(3, "127.0.0.1:65555");


recorder.start(device)
