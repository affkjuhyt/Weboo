from rest_framework.throttling import SimpleRateThrottle


class RequestMethodThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a given user.

    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the transfer will
    be used.
    """
    scope = 'user'

    def __init__(self):
        self.rate = 1
        self.num_requests = None
        self.duration = None
        pass

    def get_cache_key(self, request, view):
        if hasattr(view, "custom_throttle_rate") and getattr(view,
                                                             "custom_throttle_rate") and request.method.lower() in getattr(
                view, "custom_throttle_rate"):
            extra_throttle_name = None
            if hasattr(view, "extra_throttle_name"):
                extra_throttle_name = getattr(view, "extra_throttle_name")
            self.scope = "user_{}_{}".format(request.method.lower(), str(view.__class__))
            if extra_throttle_name:
                self.scope = "{}_{}".format(self.scope, extra_throttle_name)
            self.rate = getattr(view, "custom_throttle_rate").split("_")[1]
        else:
            method_scope = "user_{}".format(request.method.lower())
            self.scope = method_scope
            self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
