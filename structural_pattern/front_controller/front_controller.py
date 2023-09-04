#!/usr/local/bin/python
#--*-- coding: utf-8 --*--

class MobileView():
    def show_view(self):
        print('Mobile view')

class TabletView():
    def show_view(self):
        print('Tablet View')


class Dispatch():
    def __init__(self):
        self.mobileview = MobileView()
        self.tabletview = TabletView()

    def dispatch(self, request):
        if request.type == Request.mobile_type:
            self.mobileview.show_view()
        elif request.type == Request.tablet_type:
            self.tabletview.show_view()
        else:
            print('cant dispatch request')

class RequestController(object):
    def __init__(self):
        self.dispacher = Dispatch()

    def dispatch_request(self, request):
        if isinstance(request, Request):
            self.dispacher.dispatch(request)
        else:
            print('request must be Request obj')

class Request(object):
    mobile_type = 'mobile'
    tablet_type = 'tablet'

    def __init__(self, request):
        reqeust = request.lower()
        self.type = None
        if request == self.mobile_type:
            self.type = self.mobile_type
        if request == self.tablet_type:
            self.type = self.tablet_type

def main():
    dispatch_controller = RequestController()
    dispatch_controller.dispatch_request(Request('mobile'))

if __name__ == '__main__':
    main()