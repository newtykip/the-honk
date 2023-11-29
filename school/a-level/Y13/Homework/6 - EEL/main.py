import eel

eel.init("www")
eel.start("index.html", block=False)

@eel.expose
def send(msg):
    print("Received Message: " + msg)
    return "ok"

while True:
    text = eel.read_text_box()()
    print("Text box contents: {}".format(text))
    eel.sleep(2.0)
