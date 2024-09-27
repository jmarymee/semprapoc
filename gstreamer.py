import gi
from gi.repository import Gst, GObject

gi.require_version('Gst', '1.0')

Gst.init(None)

def on_message(bus, message):
    t = message.type
    if t == Gst.MessageType.EOS:
        print("End-Of-Stream reached")
        loop.quit()
    elif t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        print(f"Error: {err}, {debug}")
        loop.quit()

def main():
    pipeline = Gst.parse_launch("rtspsrc location=rtsp://your_rtsp_url ! decodebin ! autovideosink")

    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect("message", on_message)

    pipeline.set_state(Gst.State.PLAYING)

    global loop
    loop = GObject.MainLoop()
    try:
        loop.run()
    except:
        pass

    pipeline.set_state(Gst.State.NULL)

if __name__ == "__main__":
    main()