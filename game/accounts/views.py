# Create your views here.
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        backends = grouped_backends()
        return render_to_response('login.html', {'version': version,
                                                'backends': backends},
                                  RequestContext(request))

@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {'accounts': request.user.social_auth.all(),
           'version': version,
           'last_login': request.session.get('social_auth_last_login_backend'),
           'backends': grouped_backends()}
    return render_to_response('main_page.html', ctx, RequestContext(request))

def error(request):
    """Error view"""
    error_msg = request.session.pop(settings.SOCIAL_AUTH_ERROR_KEY, None)
    return render_to_response('error.html', {'version': version,
                                             'error_msg': error_msg},
                              RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')


def grouped_backends():
    """Group backends by type"""
    backends = {'oauth': [],
                'oauth2': [],
                'openid': []}

    for name, backend in BACKENDS.iteritems():
        if issubclass(backend, BaseOAuth2):
            key = 'oauth2'
        elif issubclass(backend, BaseOAuth):
            key = 'oauth'
        elif issubclass(backend, OpenIdAuth):
            key = 'openid'
        else:
            print name, backend
        backends[key].append((name, backend))
    return backends
