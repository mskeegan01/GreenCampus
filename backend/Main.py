import _thread, time
import Website, NetworkManager

_thread.start_new_thread(Website.Start, ())
NetworkManager.Listen()