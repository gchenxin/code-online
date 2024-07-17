from mitmproxy import ctx

class Modify:
    def request(self, flow):
        flow.request.url = flow.request.url + "?id=5"

addons = [Modify()]